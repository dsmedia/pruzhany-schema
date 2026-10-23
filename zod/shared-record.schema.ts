import { z } from 'zod/v4';
import {
	FactSchema,
	NameSchema,
	FateSchema,
	SourceSchema,
	AttributionSchema,
	SourcedDateSchema,
} from './sourced-entities.schema';
import {
	GenderSchema,
	LocationTypesSchema,
	LifeEventTypesSchema,
	vocabularyVersion,
} from './sourced-entities.vocabulary';
import { siteText, siteDay, uniqueIds } from './site-common.schema';
import {
	EventPartsSchema,
	ProposedNameKindsSchema,
	eventPartKinds,
} from './site-content.vocabulary';

// Site-next only: preserve the released Name shape used by enrichment.
export const SharedNameSchema = NameSchema.extend({
	kind: z.union([NameSchema.shape.kind, z.literal('other')]),
	proposed_type: ProposedNameKindsSchema.nullish(),
	attribution: AttributionSchema.nullish(),
}).superRefine((v, ctx) => {
	if ((v.kind === 'other') !== !!v.proposed_type)
		ctx.addIssue({ code: 'custom', message: 'proposed name kind exactly for other' });
	if (v.proposed_type === 'supplied' && (!v.attribution || !v.citations?.length))
		ctx.addIssue({ code: 'custom', message: 'supplied name needs attribution and citations' });
	if (v.attribution && v.proposed_type !== 'supplied')
		ctx.addIssue({ code: 'custom', message: 'supplied attribution needs the proposed name kind' });
});
export type SharedName = z.infer<typeof SharedNameSchema>;
export function isPrintedName(name: SharedName): boolean {
	return name.kind === 'printed' && !name.proposed_type;
}

// Reuse sourced-date field names and ISO parser, without its range/inference semantics.
export const LifeEventDateSchema = z
	.strictObject({
		printed: SourcedDateSchema.shape.printed,
		printed_calendar: SourcedDateSchema.shape.printed_calendar,
		start: SourcedDateSchema.shape.start,
		qualifier: z.literal('reported_in').nullish(),
		reported_in: siteDay.nullish(),
	})
	.superRefine((v, ctx) => {
		const fail = (message: string) => ctx.addIssue({ code: 'custom', message });
		if (v.qualifier === 'reported_in' && v.reported_in) {
			if (v.printed || v.printed_calendar || v.start)
				fail('reported_in cannot carry a printed or normalized event date');
		} else if (!v.printed || !v.printed_calendar || v.qualifier || v.reported_in) {
			fail('event date needs printed words and calendar or reported_in qualifier');
		}
		if (v.start && v.printed_calendar === 'hebrew')
			fail('normalization requires a printed Gregorian date');
	});
export type LifeEventDate = z.infer<typeof LifeEventDateSchema>;
export const LifeEventParticipantSchema = z.strictObject({
	person_id: siteText,
	part: EventPartsSchema,
});
export type LifeEventParticipant = z.infer<typeof LifeEventParticipantSchema>;

// Fact and standing reuse the production contract, including its sources and review.
export const SharedFactSchema = FactSchema.safeExtend({
	subject_id: siteText,
	family_id: siteText.nullish(),
	representation: z.enum(['structured', 'prose', 'image']),
}).superRefine((v, ctx) => {
	if (v.representation !== 'structured' && !v.value)
		ctx.addIssue({ code: 'custom', message: 'prose or image fact needs its value' });
	if (v.representation !== 'structured' && v.type !== 'other')
		ctx.addIssue({ code: 'custom', message: 'prose and image forms use other with proposed_type' });
});
export type SharedFact = z.infer<typeof SharedFactSchema>;

// This identifies prose needing review; it is not a publication permission.
export function isUnreviewedProse(fact: SharedFact): boolean {
	return fact.representation === 'prose' && fact.review.state !== 'approved';
}

// Relation: subject -> relative; unreleased types keep other/proposed_type.
export const SourcedRelationSchema = FactSchema.safeExtend({
	type: z.enum(['kinship', 'other']),
	subject_id: siteText,
	family_id: siteText.nullish(),
	shown: AttributionSchema.nullish(), // Permission to show a relative, never death evidence.
}).superRefine((v, ctx) => {
	if (!(v.related_person_id || v.related_name))
		ctx.addIssue({ code: 'custom', message: 'relation needs a person or an unresolved name' });
	if (v.type === 'other' && v.relationship_type)
		ctx.addIssue({ code: 'custom', message: 'unreleased relation uses proposed_type only' });
	if (
		v.citations.some((c) => c.unit_id && c.edition_date) &&
		(v.relationship_type === 'child_of' || v.proposed_type === 'child_of')
	)
		ctx.addIssue({ code: 'custom', message: 'notice relation must use parent_of, not child_of' });
});
export type SourcedRelation = z.infer<typeof SourcedRelationSchema>;

const identity = { id: siteText, name: siteText, names: z.array(NameSchema) };
export const SharedPersonSchema = z.strictObject({
	...identity,
	names: z.array(SharedNameSchema),
	gender: GenderSchema,
	fate: FateSchema.nullish(),
});
export type SharedPerson = z.infer<typeof SharedPersonSchema>;
export const SharedFamilySchema = z.strictObject(identity);
export type SharedFamily = z.infer<typeof SharedFamilySchema>;
export const SharedPlaceSchema = z.strictObject({
	...identity,
	type: LocationTypesSchema,
	parent_id: siteText.nullish(),
	coordinates: z.tuple([z.number().min(-90).max(90), z.number().min(-180).max(180)]).nullish(),
});
export type SharedPlace = z.infer<typeof SharedPlaceSchema>;
export const SharedOrganizationSchema = z.strictObject(identity);
export type SharedOrganization = z.infer<typeof SharedOrganizationSchema>;
export const SharedEventSchema = z
	.strictObject({
		id: siteText,
		name: siteText,
		type: z.union([LifeEventTypesSchema, z.literal('holocaust_event')]),
		proposed_type: siteText.nullish(),
		participants: z.array(LifeEventParticipantSchema),
		dates: z.array(LifeEventDateSchema).min(1),
		location_id: siteText.nullish(),
		description: z.string().nullish(),
	})
	.superRefine((v, ctx) => {
		const fail = (message: string) => ctx.addIssue({ code: 'custom', message });
		if ((v.type === 'other') !== !!v.proposed_type) fail('event proposed_type exactly for other');
		if (
			v.proposed_type &&
			(LifeEventTypesSchema.options.includes(v.proposed_type as never) ||
				v.proposed_type === 'holocaust_event')
		)
			fail('released event kind cannot be proposed_type');
		for (const message of uniqueIds(
			v.participants.map((p) => p.person_id),
			'event participant'
		))
			fail(message);
		const kind = v.proposed_type ?? v.type;
		for (const p of v.participants)
			if (!eventPartKinds[p.part].includes(kind)) fail('part does not fit event kind');
		if (v.dates.some((d) => d.qualifier === 'reported_in') && v.dates.length !== 1)
			fail('reported_in must be the only date when no date is printed');
	});
export type SharedEvent = z.infer<typeof SharedEventSchema>;

export const SharedRecordSchema = z
	.strictObject({
		version: z.literal('1'),
		vocabulary_version: z.literal(vocabularyVersion),
		persons: z.array(SharedPersonSchema),
		families: z.array(SharedFamilySchema),
		places: z.array(SharedPlaceSchema),
		organizations: z.array(SharedOrganizationSchema),
		events: z.array(SharedEventSchema),
		sources: z.array(SourceSchema),
		facts: z.array(SharedFactSchema),
		relations: z.array(SourcedRelationSchema),
	})
	.superRefine((v, ctx) => {
		for (const message of sharedRecordErrors(v)) ctx.addIssue({ code: 'custom', message });
	});
export type SharedRecord = z.infer<typeof SharedRecordSchema>;

function sharedRecordErrors(v: SharedRecord): string[] {
	const identities = [...v.persons, ...v.families, ...v.places, ...v.organizations];
	const all = [...identities, ...v.events, ...v.sources, ...v.facts, ...v.relations];
	const errors = uniqueIds(
		all.map((x) => x.id),
		'shared id'
	);
	const ids = (xs: { id: string }[]) => new Set(xs.map((x) => x.id));
	const persons = ids(v.persons),
		places = ids(v.places),
		organizations = ids(v.organizations);
	const families = ids(v.families),
		events = ids(v.events),
		sources = ids(v.sources);
	const subjects = ids([...identities, ...v.events, ...v.relations]);
	const facts = new Map(v.facts.map((f) => [f.id, f]));
	const births = new Set<string>(),
		deaths = new Set<string>();
	for (const event of v.events) {
		if (event.location_id && !places.has(event.location_id))
			errors.push('unknown life event place');
		for (const p of event.participants) {
			if (!persons.has(p.person_id)) errors.push('participant must resolve to a person');
			// RiC-CM R070/R072, not an OWL functional-property claim.
			const seen =
				event.type === 'birth' && p.part === 'baby'
					? births
					: event.type === 'death' && p.part === 'deceased'
						? deaths
						: null;
			if (seen?.has(p.person_id)) errors.push(`person has more than one ${event.type}`);
			seen?.add(p.person_id);
		}
	}
	for (const f of [...v.facts, ...v.relations]) {
		if (!subjects.has(f.subject_id)) errors.push('unknown fact subject');
		for (const [id, known, label] of [
			[f.place_id, places, 'place'],
			[f.organization_id, organizations, 'organisation'],
			[f.event_id, events, 'event'],
			[f.related_person_id, persons, 'relative'],
			[f.family_id, families, 'family'],
		] as const)
			if (id && !known.has(id)) errors.push(`unknown fact ${label}`);
		if (f.citations.some((c) => !sources.has(c.source_id))) errors.push('unknown citation source');
	}
	const noticeRelations = new Set<string>();
	for (const relation of v.relations) {
		if (!persons.has(relation.subject_id)) errors.push('relation subject must be a person');
		if (relation.subject_id === relation.related_person_id) errors.push('self relation');
		if (relation.citations.some((c) => c.unit_id && c.edition_date)) {
			const key = JSON.stringify([
				relation.subject_id,
				relation.relationship_type ?? relation.proposed_type,
				relation.related_person_id ?? relation.related_name,
			]);
			if (noticeRelations.has(key)) errors.push('duplicate notice relation');
			noticeRelations.add(key);
		}
	}
	for (const identity of identities)
		if (identity.names.some((n) => n.citations?.some((c) => !sources.has(c.source_id))))
			errors.push('unknown name citation source');
	for (const p of v.persons)
		if (p.fate?.rests_on.some((id) => facts.get(id)?.subject_id !== p.id))
			errors.push('fate must rest on own facts');
	const byPlace = new Map(v.places.map((p) => [p.id, p]));
	for (const place of v.places) {
		const seen = new Set<string>();
		let id: string | null | undefined = place.id;
		while (id) {
			if (seen.has(id)) {
				errors.push('place parent cycle');
				break;
			}
			if (!byPlace.has(id)) {
				errors.push('unknown parent place');
				break;
			}
			seen.add(id);
			id = byPlace.get(id)?.parent_id;
		}
	}
	return errors;
}
