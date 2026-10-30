import {
	ContentItemRefShape,
	IssueLifeEventShape,
	IssueLifeEventsDataShape,
} from './generated/life_events';
import { IssueMentionShape, IssueMentionsDataShape } from './generated/mentions';
import { z } from 'zod/v4';
import { PagesDataSchema, type PagesData } from './page.schema';
import { type Citation } from './sourced-entities.schema';

import { ContentItemsDataSchema } from './content-item.schema';
import { SharedRecordSchema } from './shared-record.schema';
import {
	PrintedAddressSchema,
	siteDay,
	uniqueIds,
	type PrintedAddress,
	type ContentItemBlockRef,
} from './site-common.schema';

// Mention: located words or whole regions, with a derived content item reference.
// Preserve the published files' key order when the site re-serializes parsed mentions.
const {
	id,
	person_id,
	printed_name,
	title,
	function: mentionFunction,
	wkd_id,
	...mentionFields
} = IssueMentionShape.shape;
export const IssueMentionSchema = z
	.strictObject({
		id,
		person_id,
		// known-looser: the printed_name key is required even when its value is null.
		printed_name: printed_name.unwrap(),
		title,
		function: mentionFunction,
		wkd_id,
		...mentionFields,
		addresses: z.array(PrintedAddressSchema).min(1),
	})
	.superRefine((v, ctx) => {
		for (const message of uniqueIds(v.roles, 'mention role'))
			ctx.addIssue({ code: 'custom', message });
		if ((v.address_grain === 'regions') !== (v.printed_name === null))
			ctx.addIssue({
				code: 'custom',
				message: 'printed name must be null exactly when address grain is regions',
			});
		if (
			v.printed_name !== null &&
			!v.addresses
				.map((a) => a.text)
				.join('\n')
				.includes(v.printed_name)
		)
			ctx.addIssue({ code: 'custom', message: 'printed name must occur at the mention address' });
	});
export type IssueMention = z.infer<typeof IssueMentionSchema>;
export const IssueMentionsDataSchema = IssueMentionsDataShape.extend({
	issue_date: siteDay,
	mentions: z.array(IssueMentionSchema),
}).superRefine((v, ctx) => {
	for (const message of uniqueIds(
		v.mentions.map((m) => m.id),
		'mention id'
	))
		ctx.addIssue({ code: 'custom', message });
});
export type IssueMentionsData = z.infer<typeof IssueMentionsDataSchema>;

export const ContentItemRefSchema = ContentItemRefShape;
export type ContentItemRef = z.infer<typeof ContentItemRefSchema>;
export const IssueLifeEventSchema = IssueLifeEventShape.superRefine((v, ctx) => {
	for (const message of uniqueIds(
		v.content_items.map((c) => c.content_item_id),
		'event content item'
	))
		ctx.addIssue({ code: 'custom', message });
});
export type IssueLifeEvent = z.infer<typeof IssueLifeEventSchema>;
export const IssueLifeEventsDataSchema = IssueLifeEventsDataShape.extend({
	issue_date: siteDay,
	life_events: z.array(IssueLifeEventSchema),
}).superRefine((v, ctx) => {
	for (const message of uniqueIds(
		v.life_events.map((e) => e.id),
		'life event id'
	))
		ctx.addIssue({ code: 'custom', message });
	const assigned = new Set<string>();
	for (const event of v.life_events)
		for (const ref of event.content_items) {
			if (assigned.has(ref.content_item_id))
				ctx.addIssue({
					code: 'custom',
					message: 'content item belongs to more than one life event',
				});
			assigned.add(ref.content_item_id);
		}
});
export type IssueLifeEventsData = z.infer<typeof IssueLifeEventsDataSchema>;

// In-memory check of the four documents. Pages keep their existing file shape.
export const SiteIssueSchema = z
	.strictObject({
		pages: PagesDataSchema,
		content_items: ContentItemsDataSchema,
		mentions: IssueMentionsDataSchema,
		life_events: IssueLifeEventsDataSchema,
	})
	.superRefine((v, ctx) => {
		for (const message of siteIssueErrors(v)) ctx.addIssue({ code: 'custom', message });
	});
export type SiteIssue = z.infer<typeof SiteIssueSchema>;

function printedAddressErrors(
	addresses: PrintedAddress[],
	refs: ContentItemBlockRef[],
	pages: Map<string, PagesData['pages'][number]>,
	match: 'bounds' | 'text' | 'whole-region'
): string[] {
	const errors: string[] = [];
	for (const a of addresses) {
		const found = refs.some((ref) => {
			const page = pages.get(ref.page_id);
			if (!page || page.image_uri !== a.image_uri) return false;
			return page.blocks.some((b) => {
				if (!ref.block_ids.includes(b.id)) return false;
				if (match === 'whole-region')
					return a.bbox.every((n, i) => n === b.bbox[i]) && a.text === b.transcription;
				return (
					a.bbox[0] >= b.bbox[0] &&
					a.bbox[1] >= b.bbox[1] &&
					a.bbox[0] + a.bbox[2] <= b.bbox[0] + b.bbox[2] &&
					a.bbox[1] + a.bbox[3] <= b.bbox[1] + b.bbox[3] &&
					(match !== 'text' || b.transcription.includes(a.text))
				);
			});
		});
		if (!found)
			errors.push(
				match === 'whole-region'
					? 'region mention address must equal a whole region of its content item'
					: 'printed address is outside its content item or heading'
			);
	}
	return errors;
}

function siteIssueErrors(v: SiteIssue): string[] {
	const errors: string[] = [];
	const date = v.content_items.issue_date;
	if (
		[
			v.pages.edition_date,
			v.mentions.issue_date,
			v.life_events.issue_date,
			...v.pages.pages.map((p) => p.issue_date),
		].some((d) => d !== date)
	)
		errors.push('issue dates disagree');
	errors.push(
		...uniqueIds(
			v.pages.pages.map((p) => p.id),
			'page id'
		)
	);
	const pages = new Map(v.pages.pages.map((p) => [p.id, p]));
	const items = new Map(v.content_items.content_items.map((i) => [i.id, i]));
	const key = (page: string, block: string) => JSON.stringify([page, block]);
	const owners = new Map<string, string>();
	const own = (refs: ContentItemBlockRef[], owner: string, unit: string | null) => {
		const texts: string[] = [];
		for (const ref of refs)
			for (const id of ref.block_ids) {
				const block = pages.get(ref.page_id)?.blocks.find((b) => b.id === id);
				if (!block) {
					errors.push('unknown page or block');
					continue;
				}
				const k = key(ref.page_id, id);
				if (owners.has(k)) errors.push('region has more than one owner');
				owners.set(k, owner);
				if (block.unit_id !== unit) errors.push('block content item disagrees with owner');
				texts.push(block.transcription);
			}
		return texts;
	};

	for (const item of v.content_items.content_items) {
		const texts = own(item.page_blocks, `item:${item.id}`, item.id);
		if (!textFromRegions(texts, item.full_text, item.block_breaks))
			errors.push(
				`${item.id}: full_text and block_breaks must follow the regions' line breaks and broken-word joins`
			);
		if (item.printed_title)
			errors.push(
				...printedAddressErrors(item.printed_title.addresses, item.page_blocks, pages, 'text')
			);
		errors.push(
			...printedAddressErrors(
				item.supplied_title.based_on.addresses,
				item.page_blocks,
				pages,
				'bounds'
			)
		);
		if (item.translation)
			errors.push(
				...printedAddressErrors(
					item.translation.based_on.addresses,
					item.page_blocks,
					pages,
					'bounds'
				)
			);
	}
	for (const section of v.content_items.sections) {
		own(section.heading_blocks, `section:${section.id}`, null);
		errors.push(
			...printedAddressErrors(
				section.printed_title.addresses,
				section.heading_blocks,
				pages,
				'text'
			)
		);
		if (section.supplied_title)
			errors.push(
				...printedAddressErrors(
					section.supplied_title.based_on.addresses,
					section.heading_blocks,
					pages,
					'bounds'
				)
			);
	}
	for (const page of v.pages.pages) {
		errors.push(
			...uniqueIds(
				page.blocks.map((b) => b.id),
				'block id'
			)
		);
		for (const block of page.blocks)
			if (!owners.has(key(page.id, block.id))) errors.push('region has no owner');
	}
	for (const mention of v.mentions.mentions) {
		const item = items.get(mention.content_item_id);
		if (!item) errors.push('unknown mention content item');
		else
			errors.push(
				...printedAddressErrors(
					mention.addresses,
					item.page_blocks,
					pages,
					mention.address_grain === 'regions' ? 'whole-region' : 'text'
				)
			);
	}
	for (const event of v.life_events.life_events)
		for (const ref of event.content_items) {
			const item = items.get(ref.content_item_id);
			if (!item) errors.push('unknown life event content item');
			else if (item.event_id && item.event_id !== event.id)
				errors.push('content item event disagrees with life event');
		}
	return errors;
}

// Only LF may become a space. At a line-ending - or maqaf, a join may
// retain or drop that sign; every other character stays exact.
function lineTextMatches(source: string, text: string): boolean {
	const lines = source.split('\n');
	let positions = new Set([0]);
	for (let i = 0; i < lines.length; i++) {
		let literal = lines[i];
		let endings = i + 1 < lines.length ? ['\n', ' '] : [''];
		if (i + 1 < lines.length && canJoin(literal, lines[i + 1])) {
			const sign = literal.slice(-1);
			literal = literal.slice(0, -1);
			endings = [sign + '\n', sign + ' ', sign, ''];
		}
		const next = new Set<number>();
		for (const at of positions)
			for (const ending of endings) {
				const fragment = literal + ending;
				if (text.startsWith(fragment, at)) next.add(at + fragment.length);
			}
		positions = next;
		if (!positions.size) return false;
	}
	return positions.has(text.length);
}

function canJoin(before: string, after: string): boolean {
	return (
		before.length > 1 &&
		['-', '־'].includes(before.slice(-1)) &&
		![' ', '\t', '\r', '\n'].includes(before.slice(-2, -1)) &&
		after.length > 0 &&
		![' ', '\t', '\r', '\n'].includes(after[0])
	);
}

function textFromRegions(regions: string[], text: string, breaks: number[]): boolean {
	const starts = breaks.length ? breaks : [0];
	if (starts.length !== regions.length || starts[0] !== 0) return false;
	// Keep the hand-made form, including its exact whitespace and empty regions.
	let offset = 0;
	if (
		text === regions.join('\n\n') &&
		regions.every((region, i) => {
			const matches = starts[i] === offset;
			offset += [...region].length + 2;
			return matches;
		})
	)
		return true;

	const points = [...text]; // block_breaks are Unicode code-point offsets.
	let states = [{ carry: '', end: 0 }];
	for (let i = 0; i < regions.length; i++) {
		const source = regions[i];
		const start = starts[i];
		const ends = i + 1 < starts.length ? [starts[i + 1] - 2, starts[i + 1]] : [points.length];
		const next = new Map<string, { carry: string; end: number }>();
		for (const state of states) {
			const choices = [{ source: state.carry + source, carry: '' }];
			if (i + 1 < regions.length && canJoin(source, regions[i + 1])) {
				const split = Math.max(...[' ', '\t', '\r', '\n'].map((c) => source.lastIndexOf(c)));
				const head = source.slice(0, Math.max(0, split));
				const tail = source.slice(split + 1);
				// text_of emits the whole joined word in the following region.
				// A token already receiving a carry cannot also be deferred.
				if ((split < 0 || [' ', '\n'].includes(source[split])) && (head || !state.carry))
					for (const carry of [tail.slice(0, -1), tail])
						choices.push({ source: state.carry + head, carry });
			}
			for (const end of ends) {
				if (end < start) continue;
				const separator = end > start && state.end > 0 ? '\n\n' : '';
				if (
					start !== state.end + separator.length ||
					points.slice(state.end, start).join('') !== separator
				)
					continue;
				const segment = points.slice(start, end).join('');
				for (const choice of choices)
					if (lineTextMatches(choice.source, segment)) {
						const candidate = { carry: choice.carry, end };
						next.set(JSON.stringify(candidate), candidate);
					}
			}
		}
		states = [...next.values()];
		if (!states.length) return false;
	}
	return states.some((state) => !state.carry && state.end === points.length);
}

// Validate joins without embedding any person in an issue's persisted files.
function noticeKey(c: Citation): string {
	return JSON.stringify([c.source_id, c.edition_date, c.unit_id]);
}

export const SiteArchiveSchema = z
	.strictObject({
		shared_record: SharedRecordSchema,
		issues: z.array(SiteIssueSchema),
	})
	.superRefine((v, ctx) => {
		const errors = uniqueIds(
			v.issues.map((i) => i.content_items.issue_date),
			'issue date'
		);
		const people = new Set(v.shared_record.persons.map((p) => p.id));
		const places = new Set(v.shared_record.places.map((p) => p.id));
		const organizations = new Set(v.shared_record.organizations.map((o) => o.id));
		const events = new Map(v.shared_record.events.map((e) => [e.id, e]));
		const firstIssues = new Map<string, string>();
		const contentItems = new Map<
			string,
			{
				text: string;
				mentions: IssueMention[];
				events: Set<string>;
				pageBlocks: ContentItemBlockRef[];
				pages: Map<string, PagesData['pages'][number]>;
			}
		>();
		const contentItemKey = (date: string, id: string) => JSON.stringify([date, id]);
		for (const issue of v.issues) {
			const date = issue.content_items.issue_date;
			const pages = new Map(issue.pages.pages.map((p) => [p.id, p]));
			const issueEvents = new Set(issue.life_events.life_events.map((e) => e.id));
			if (issue.mentions.mentions.some((m) => !people.has(m.person_id)))
				errors.push('unknown mention person');
			for (const item of issue.content_items.content_items) {
				contentItems.set(contentItemKey(date, item.id), {
					text: item.full_text,
					pageBlocks: item.page_blocks,
					pages,
					mentions: issue.mentions.mentions.filter((m) => m.content_item_id === item.id),
					events: new Set(
						issue.life_events.life_events
							.filter((e) => e.content_items.some((c) => c.content_item_id === item.id))
							.map((e) => e.id)
					),
				});
				if (item.location_ids.some((id) => !places.has(id)))
					errors.push('unknown content item place');
				if (item.organization_ids.some((id) => !organizations.has(id)))
					errors.push('unknown content item organisation');
				if (item.event_id && !events.has(item.event_id) && !issueEvents.has(item.event_id))
					errors.push('unknown content item event');
				if (item.event_id && events.get(item.event_id)?.evidence_basis === 'records_only')
					errors.push('records-only death cannot have an issue selection');
			}
			for (const event of issue.life_events.life_events) {
				if (!events.has(event.id)) errors.push('unknown life event');
				if (events.get(event.id)?.evidence_basis === 'records_only')
					errors.push('records-only death cannot have an issue selection');
				if (!firstIssues.has(event.id) || date < firstIssues.get(event.id)!)
					firstIssues.set(event.id, date);
			}
		}
		for (const event of v.shared_record.events) {
			if (
				event.dates.some((d) => d.record_fact_id) &&
				!firstIssues.has(event.id) &&
				event.evidence_basis !== 'records_only'
			)
				errors.push('record death without an issue selection must say records_only');
			for (const date of event.dates)
				if (
					date.qualifier === 'reported_in' &&
					firstIssues.has(event.id) &&
					date.reported_in !== firstIssues.get(event.id)
				)
					errors.push('reported_in must be the first issue date');
		}
		const citedContentItem = (c: Citation) =>
			c.edition_date && c.unit_id
				? contentItems.get(contentItemKey(c.edition_date, c.unit_id))
				: undefined;
		const assertions = [...v.shared_record.facts, ...v.shared_record.relations];
		const citations = [
			...assertions.flatMap((f) => f.citations),
			...v.shared_record.persons.flatMap((p) => p.names.flatMap((n) => n.citations ?? [])),
		];
		for (const c of citations) {
			// Scope to located evidence written now; older citations keep their reading.
			if (!c.addresses) continue;
			const contentItem = citedContentItem(c);
			if (!contentItem) errors.push('unknown cited content item');
			else {
				if (c.quote && !contentItem.text.includes(c.quote))
					errors.push('citation quote must occur in content item');
				errors.push(
					...printedAddressErrors(c.addresses, contentItem.pageBlocks, contentItem.pages, 'text')
				);
			}
		}
		for (const child of v.shared_record.persons.filter((p) =>
			p.names.some((n) => n.kind === 'supplied')
		)) {
			const births = v.shared_record.facts.filter(
				(f) =>
					f.subject_id === child.id &&
					f.type === 'birth' &&
					f.qualifiers?.child_count === '1' &&
					f.event_id &&
					events.get(f.event_id)?.type === 'birth' &&
					events
						.get(f.event_id)
						?.main_people.some((p) => p.person_id === child.id && p.part === 'baby')
			);
			if (!births.length) errors.push('described child needs a single-child birth fact');
			for (const birth of births) {
				if (events.get(birth.event_id!)!.main_people.filter((p) => p.part === 'baby').length !== 1)
					errors.push('single-child birth must have exactly one baby');
				const notices = birth.citations.filter(
					(c) => c.addresses && c.quote && citedContentItem(c)?.events.has(birth.event_id!)
				);
				if (
					!notices.some((c) =>
						citedContentItem(c)?.mentions.some(
							(m) =>
								m.person_id === child.id &&
								m.address_grain === 'words' &&
								m.roles.includes('subject') &&
								m.printed_name &&
								c.quote!.includes(m.printed_name)
						)
					)
				)
					errors.push('described child needs a cited designation mention');
				const noticeKeys = new Set(notices.map(noticeKey));
				if (
					!child.names.some(
						(n) =>
							n.kind === 'supplied' &&
							n.citations?.some((c) => c.addresses && noticeKeys.has(noticeKey(c)))
					)
				)
					errors.push('supplied name must cite the birth notice');
				const parents = events.get(birth.event_id!)!.main_people.filter((p) => p.part === 'parent');
				if (
					!parents.length ||
					parents.some(
						(p) =>
							!v.shared_record.relations.some(
								(r) =>
									r.subject_id === p.person_id &&
									r.related_person_id === child.id &&
									r.relationship_type === 'parent_of' &&
									r.citations.some((c) => c.addresses && noticeKeys.has(noticeKey(c)))
							)
					)
				)
					errors.push('described child needs each parent relation citing the birth notice');
			}
		}
		for (const message of errors) ctx.addIssue({ code: 'custom', message });
	});
export type SiteArchive = z.infer<typeof SiteArchiveSchema>;
