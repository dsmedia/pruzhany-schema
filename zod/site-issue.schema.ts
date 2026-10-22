import { z } from 'zod/v4';
import { PagesDataSchema } from './page.schema';
import { LifeEventSchema } from './life-event.schema';
import { MentionSchema } from './sourced-entities.schema';
import { MentionRolesSchema, ContentUnitRolesSchema } from './sourced-entities.vocabulary';
import { ContentItemsDataSchema } from './content-item.schema';
import { SharedRecordSchema } from './shared-record.schema';
import {
	PrintedAddressSchema,
	siteText,
	siteDay,
	uniqueIds,
	type PrintedAddress,
	type ContentItemBlockRef,
} from './site-common.schema';

// Mention: an addressed printed name, with a derived content item reference.
export const IssueMentionSchema = MentionSchema.omit({ unit_id: true, role: true })
	.extend({
		content_item_id: siteText,
		roles: z.array(MentionRolesSchema).min(1),
		addresses: z.array(PrintedAddressSchema).min(1),
	})
	.superRefine((v, ctx) => {
		for (const message of uniqueIds(v.roles, 'mention role'))
			ctx.addIssue({ code: 'custom', message });
		if (
			!v.addresses
				.map((a) => a.text)
				.join('\n')
				.includes(v.printed_name)
		)
			ctx.addIssue({ code: 'custom', message: 'printed name must occur at the mention address' });
	});
export type IssueMention = z.infer<typeof IssueMentionSchema>;
export const IssueMentionsDataSchema = z
	.strictObject({
		issue_date: siteDay,
		mentions: z.array(IssueMentionSchema),
	})
	.superRefine((v, ctx) => {
		for (const message of uniqueIds(
			v.mentions.map((m) => m.id),
			'mention id'
		))
			ctx.addIssue({ code: 'custom', message });
	});
export type IssueMentionsData = z.infer<typeof IssueMentionsDataSchema>;

export const ContentItemRefSchema = z.strictObject({
	content_item_id: siteText,
	role: ContentUnitRolesSchema, // Role of the content item, not the person's role.
});
export type ContentItemRef = z.infer<typeof ContentItemRefSchema>;
export const IssueLifeEventSchema = LifeEventSchema.omit({ content_units: true })
	.extend({
		id: siteText,
		principal_ids: z.array(siteText), // Persons in the shared record.
		content_items: z.array(ContentItemRefSchema),
	})
	.strict();
export type IssueLifeEvent = z.infer<typeof IssueLifeEventSchema>;
export const IssueLifeEventsDataSchema = z
	.strictObject({
		issue_date: siteDay,
		life_events: z.array(IssueLifeEventSchema),
	})
	.superRefine((v, ctx) => {
		for (const message of uniqueIds(
			v.life_events.map((e) => e.id),
			'life event id'
		))
			ctx.addIssue({ code: 'custom', message });
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
		return texts.join('\n\n');
	};
	const addressErrors = (
		addresses: PrintedAddress[],
		refs: ContentItemBlockRef[],
		checkText: boolean
	) => {
		for (const a of addresses) {
			const found = refs.some((ref) => {
				const page = pages.get(ref.page_id);
				if (!page || page.image_uri !== a.image_uri) return false;
				return page.blocks.some(
					(b) =>
						ref.block_ids.includes(b.id) &&
						a.bbox[0] >= b.bbox[0] &&
						a.bbox[1] >= b.bbox[1] &&
						a.bbox[0] + a.bbox[2] <= b.bbox[0] + b.bbox[2] &&
						a.bbox[1] + a.bbox[3] <= b.bbox[1] + b.bbox[3] &&
						(!checkText || b.transcription.includes(a.text))
				);
			});
			if (!found) errors.push('printed address is outside its content item or heading');
		}
	};
	for (const item of v.content_items.content_items) {
		if (own(item.page_blocks, `item:${item.id}`, item.id) !== item.full_text)
			errors.push('full_text must be the block transcriptions joined by blank lines');
		if (item.printed_title) addressErrors(item.printed_title.addresses, item.page_blocks, true);
		addressErrors(item.supplied_title.based_on.addresses, item.page_blocks, false);
		if (item.translation)
			addressErrors(item.translation.based_on.addresses, item.page_blocks, false);
	}
	for (const section of v.content_items.sections) {
		own(section.heading_blocks, `section:${section.id}`, null);
		addressErrors(section.printed_title.addresses, section.heading_blocks, true);
		addressErrors(section.supplied_title.based_on.addresses, section.heading_blocks, false);
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
		else addressErrors(mention.addresses, item.page_blocks, true);
	}
	for (const event of v.life_events.life_events)
		if (event.content_items.some((r) => !items.has(r.content_item_id)))
			errors.push('unknown life event content item');
	return errors;
}

// Validate joins without embedding any person in an issue's persisted files.
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
		for (const issue of v.issues) {
			if (issue.mentions.mentions.some((m) => !people.has(m.person_id)))
				errors.push('unknown mention person');
			for (const item of issue.content_items.content_items) {
				if (item.location_ids.some((id) => !places.has(id)))
					errors.push('unknown content item place');
				if (item.organization_ids.some((id) => !organizations.has(id)))
					errors.push('unknown content item organisation');
				if (item.event_id && !events.has(item.event_id)) errors.push('unknown content item event');
			}
			for (const event of issue.life_events.life_events) {
				if (event.principal_ids.some((id) => !people.has(id)))
					errors.push('unknown life event person');
				if (event.location_id && !places.has(event.location_id))
					errors.push('unknown life event place');
				if (events.get(event.id)?.type !== event.type)
					errors.push('life event must agree with shared event');
			}
		}
		for (const message of errors) ctx.addIssue({ code: 'custom', message });
	});
export type SiteArchive = z.infer<typeof SiteArchiveSchema>;
