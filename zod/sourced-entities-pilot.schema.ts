// Experimental issue-14 contract; not re-exported by the production index.
import { createHash } from 'node:crypto';
import { z } from 'zod/v4';
import {
	factTypeValues,
	mentionRoleValues,
	nameKindValues,
	pilotEventTypeValues,
	relationshipTypeValues,
	vocabularyVersion,
} from './sourced-entities-pilot.vocabulary';

const confidence = z.enum(['confirmed', 'probable', 'possible']);
const status = z.enum(['accepted', 'disputed', 'rejected']);
const lowerDate = (value: string) =>
	value + ({ 4: '-01-01', 7: '-01', 10: '' }[value.length] ?? '');
const upperDate = (value: string) =>
	value.length === 4
		? `${value}-12-31`
		: value.length === 7
			? `${value}-${new Date(Date.UTC(Number(value.slice(0, 4)), Number(value.slice(5)), 0)).getUTCDate().toString().padStart(2, '0')}`
			: value;
const refs = z.array(z.string()).min(1);
export const PilotReviewSchema = z
	.strictObject({
		state: z.enum(['pending', 'approved']).default('pending'),
		by: z.string().nullish(),
		on: z
			.string()
			.regex(/^\d{4}-\d{2}-\d{2}$/)
			.nullish(),
	})
	.superRefine((v, ctx) => {
		if (v.state === 'approved' && !(v.by?.trim() && v.on))
			ctx.addIssue({ code: 'custom', message: 'approval requires who and when' });
		if (v.on) {
			const d = new Date(`${v.on}T00:00:00Z`);
			if (
				Number.isNaN(d.valueOf()) ||
				d.toISOString().slice(0, 10) !== v.on ||
				Number(v.on.slice(0, 4)) < 1
			)
				ctx.addIssue({ code: 'custom', message: 'invalid approval date' });
		}
	});

const dateString = z.string().regex(/^\d{4}(-\d{2}(-\d{2})?)?$/);
export const PilotDateSchema = z
	.strictObject({
		start: dateString,
		end: dateString.nullish(),
		precision: z.enum(['year', 'month', 'day', 'range']),
		printed: z.string().nullish(),
		printed_calendar: z.enum(['gregorian', 'hebrew']).nullish(),
		inferred: z.boolean().default(false),
	})
	.superRefine((v, ctx) => {
		const lengths = { year: 4, month: 7, day: 10 };
		for (const text of [v.start, v.end]) {
			if (!text) continue;
			const full = text + ({ 4: '-01-01', 7: '-01', 10: '' }[text.length] ?? 'invalid');
			const parsed = new Date(`${full}T00:00:00Z`);
			if (
				Number.isNaN(parsed.valueOf()) ||
				parsed.toISOString().slice(0, 10) !== full ||
				Number(text.slice(0, 4)) < 1
			)
				ctx.addIssue({ code: 'custom', message: 'invalid calendar date' });
		}
		if (v.precision !== 'range' && (v.start.length !== lengths[v.precision] || v.end))
			ctx.addIssue({ code: 'custom', message: 'date precision does not match value' });
		if (v.precision === 'range' && (!v.end || lowerDate(v.start) > upperDate(v.end)))
			ctx.addIssue({ code: 'custom', message: 'range needs ordered start and end' });
		if (v.printed_calendar && !v.printed)
			ctx.addIssue({ code: 'custom', message: 'printed calendar needs printed date' });
	});

export const PilotSourceSchema = z.strictObject({
	id: z.string(),
	kind: z.enum(['newspaper', 'book', 'archive_record']),
	title: z.string(),
	work_id: z.string(),
});
export const PilotCitationSchema = z.strictObject({
	id: z.string(),
	source_id: z.string(),
	edition_date: z.string().nullish(),
	unit_id: z.string().nullish(),
	locator: z.string(),
	quote: z.string().min(1),
	url: z.string().nullish(),
	note: z.string().nullish(),
});
export const PilotNameSchema = z.strictObject({
	value: z.string().min(1),
	kind: z.enum(nameKindValues),
	script: z.enum(['Hebr', 'Latn']),
	lang: z.enum(['yi', 'he', 'en']),
	citation_ids: refs,
});
export const PilotFateSchema = z.strictObject({
	outcome: z.enum(['perished', 'survived', 'died_before', 'unknown']),
	confidence,
	rests_on: z.array(z.string()),
	review: PilotReviewSchema,
});
export const PilotPersonSchema = z
	.strictObject({
		id: z.string(),
		display_name: z.string(),
		original_ids: refs,
		names: z.array(PilotNameSchema).min(1),
		presumed_living: z.boolean().default(true),
		presumption_reason: z
			.enum([
				'death-evidenced',
				'born-110-years-ago',
				'printed-in-old-source',
				'shown-at-word',
				'unknown',
			])
			.default('unknown'),
		fate: PilotFateSchema.nullish(),
	})
	.superRefine((v, ctx) => {
		if (v.presumed_living !== (v.presumption_reason === 'unknown'))
			ctx.addIssue({
				code: 'custom',
				message: 'presumed living exactly when presumption reason is unknown',
			});
	});
export const PilotPlaceSchema = z.strictObject({ id: z.string(), label: z.string() });
export const PilotMentionSchema = z.strictObject({
	id: z.string(),
	entity_id: z.string(),
	original_entity_id: z.string(),
	citation_id: z.string(),
	printed_name: z.string().min(1),
	roles: z.array(z.enum(mentionRoleValues)).min(1),
	text_sha256: z.string().regex(/^[a-f0-9]{64}$/),
});
export const PilotFactSchema = z
	.strictObject({
		id: z.string(),
		subject_id: z.string(),
		type: z.enum(factTypeValues),
		value: z.string().nullish(),
		date: PilotDateSchema.nullish(),
		place_id: z.string().nullish(),
		related_person_id: z.string().nullish(),
		event_id: z.string().nullish(),
		proposed_type: z.string().nullish(),
		holocaust_related: z.boolean().nullish(),
		citation_ids: refs,
		evidence_confidence: confidence,
		identity_confidence: confidence,
		status,
		review: PilotReviewSchema,
		attributed_to: z.string(),
	})
	.superRefine((v, ctx) => {
		const bad = (message: string) => ctx.addIssue({ code: 'custom', message });
		if (v.type === 'residence' && (!v.place_id || !v.date))
			bad('residence requires place and time');
		if (v.type === 'occupation' && !v.value) bad('occupation requires a value');
		if (v.type === 'survival' && !v.date) bad('survival needs a time at which alive');
		if (['birth', 'death'].includes(v.type) && !(v.date || v.place_id || v.value))
			bad('birth/death assertion needs a payload');
		if (v.type === 'parenthood' && !(v.value || v.related_person_id))
			bad('parenthood needs a child or description');
		if (v.type === 'event_participation' && !(v.event_id && v.value))
			bad('event participation requires event and role');
		if (v.type === 'other' && !(v.value && v.proposed_type))
			bad('other requires a value and proposed type');
	});
export const PilotRelationshipSchema = z.strictObject({
	id: z.string(),
	from_id: z.string(),
	to_id: z.string(),
	type: z.enum(relationshipTypeValues),
	citation_ids: refs,
	evidence_confidence: confidence,
	identity_confidence: confidence,
	status,
	review: PilotReviewSchema,
});
export const PilotEventSchema = z.strictObject({
	id: z.string(),
	type: z.enum(pilotEventTypeValues),
	name: z.string(),
	original_ids: refs,
	citation_ids: refs,
});
export const PilotIdentityDecisionSchema = z.strictObject({
	id: z.string(),
	kind: z.enum(['person', 'event']),
	original_ids: z.array(z.string()).min(2),
	target_id: z.string(),
	citation_ids: z.array(z.string()).min(2),
	confidence,
	review: PilotReviewSchema,
	applied_in_preview: z.boolean(),
	reason: z.string(),
});

export const SourcedEntitiesPilotSchema = z
	.strictObject({
		version: z.literal('0.1.0'),
		vocabulary_version: z.literal(vocabularyVersion),
		as_of_year: z.number().int(),
		source_revision: z.string(),
		sources: z.array(PilotSourceSchema),
		citations: z.array(PilotCitationSchema),
		people: z.array(PilotPersonSchema),
		places: z.array(PilotPlaceSchema),
		mentions: z.array(PilotMentionSchema),
		facts: z.array(PilotFactSchema),
		relationships: z.array(PilotRelationshipSchema),
		events: z.array(PilotEventSchema),
		identity_decisions: z.array(PilotIdentityDecisionSchema),
	})
	.superRefine((v, ctx) => {
		const bad = (message: string) => ctx.addIssue({ code: 'custom', message });
		const groups = [
			v.sources,
			v.citations,
			v.people,
			v.places,
			v.mentions,
			v.facts,
			v.relationships,
			v.events,
			v.identity_decisions,
		];
		const ids = groups.flatMap((g) => g.map((x) => x.id));
		if (new Set(ids).size !== ids.length) bad('duplicate id');
		const sources = new Set(v.sources.map((x) => x.id));
		const citations = new Map(v.citations.map((x) => [x.id, x]));
		const people = new Map(v.people.map((x) => [x.id, x]));
		const places = new Set(v.places.map((x) => x.id));
		const events = new Set(v.events.map((x) => x.id));
		const facts = new Map(v.facts.map((x) => [x.id, x]));
		for (const entities of [v.people, v.events]) {
			const originals = entities.flatMap((entity) => entity.original_ids);
			if (new Set(originals).size !== originals.length)
				bad('original identity belongs to more than one entity');
		}
		const check = (values: string[], known: { has: (id: string) => boolean }, label: string) => {
			if (values.some((id) => !known.has(id))) bad(`dangling ${label}`);
		};
		for (const c of v.citations) check([c.source_id], sources, 'source');
		for (const p of v.people) {
			for (const name of p.names) check(name.citation_ids, citations, 'name citation');
			if (!p.fate) continue;
			check(p.fate.rests_on, facts, 'fate fact');
			if (p.fate.outcome !== 'unknown' && !p.fate.rests_on.length)
				bad('known fate needs supporting facts');
			for (const id of p.fate.rests_on) {
				const fact = facts.get(id);
				if (!fact) continue;
				if (fact.subject_id !== p.id || fact.status !== 'accepted')
					bad('fate must rest on own accepted facts');
				if (['perished', 'died_before'].includes(p.fate.outcome) && fact.type !== 'death')
					bad('death outcome requires death evidence');
				if (p.fate.outcome === 'perished' && fact.holocaust_related !== true)
					bad('perished needs Holocaust-related death evidence');
				if (
					p.fate.outcome === 'died_before' &&
					(!fact.date || upperDate(fact.date.end || fact.date.start) >= '1939-09-01')
				)
					bad("died_before needs death evidence before the pilot's 1939-09-01 cutoff");
				if (
					p.fate.outcome === 'survived' &&
					(fact.type !== 'survival' || !fact.date || fact.date.start < '1945-05-08')
				)
					bad("survived needs evidence alive after the pilot's explicit 1945-05-08 cutoff");
				const rank = { possible: 0, probable: 1, confirmed: 2 };
				if (
					rank[p.fate.confidence] >
					Math.min(rank[fact.evidence_confidence], rank[fact.identity_confidence])
				)
					bad('fate confidence exceeds its supporting evidence or identity match');
			}
		}
		for (const m of v.mentions) {
			check([m.entity_id], people, 'mention person');
			check([m.citation_id], citations, 'mention citation');
			const c = citations.get(m.citation_id);
			if (
				c &&
				(!c.quote.includes(m.printed_name) ||
					createHash('sha256').update(c.quote).digest('hex') !== m.text_sha256)
			)
				bad('mention anchor no longer matches source text');
			if (
				people.has(m.entity_id) &&
				!people.get(m.entity_id)!.original_ids.includes(m.original_entity_id)
			)
				bad('mention lost its original identity');
		}
		for (const f of v.facts) {
			check([f.subject_id], people, 'fact subject');
			check(f.citation_ids, citations, 'fact citation');
			if (f.place_id) check([f.place_id], places, 'place');
			if (f.related_person_id) check([f.related_person_id], people, 'related person');
			if (f.event_id) check([f.event_id], events, 'event');
		}
		for (const r of v.relationships) {
			check([r.from_id, r.to_id], people, 'relationship person');
			check(r.citation_ids, citations, 'relationship citation');
			if (r.from_id === r.to_id) bad('self relationship');
		}
		for (const event of v.events) check(event.citation_ids, citations, 'event citation');
		for (const decision of v.identity_decisions) {
			check(decision.citation_ids, citations, 'identity citation');
			if (new Set(decision.original_ids).size !== decision.original_ids.length)
				bad('identity proposal repeats an original id');
			if (decision.applied_in_preview) {
				check(
					[decision.target_id],
					decision.kind === 'person' ? people : events,
					'identity target'
				);
				const entity =
					decision.kind === 'person'
						? people.get(decision.target_id)
						: v.events.find((e) => e.id === decision.target_id);
				if (entity && decision.original_ids.some((id) => !entity.original_ids.includes(id)))
					bad('identity proposal lost its source identities');
			}
		}
	});
export type SourcedEntitiesPilot = z.infer<typeof SourcedEntitiesPilotSchema>;
