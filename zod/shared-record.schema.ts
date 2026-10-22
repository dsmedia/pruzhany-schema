import { z } from 'zod/v4';
import {
	FactSchema,
	NameSchema,
	FateSchema,
	SourceSchema,
	AttributionSchema,
} from './sourced-entities.schema';
import {
	GenderSchema,
	LocationTypesSchema,
	EventTypesSchema,
	vocabularyVersion,
} from './sourced-entities.vocabulary';
import { siteText, uniqueIds } from './site-common.schema';

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
});
export type SourcedRelation = z.infer<typeof SourcedRelationSchema>;

const identity = { id: siteText, name: siteText, names: z.array(NameSchema) };
export const SharedPersonSchema = z.strictObject({
	...identity,
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
export const SharedEventSchema = z.strictObject({
	id: siteText,
	name: siteText,
	type: EventTypesSchema,
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
	for (const relation of v.relations) {
		if (!persons.has(relation.subject_id)) errors.push('relation subject must be a person');
		if (relation.subject_id === relation.related_person_id) errors.push('self relation');
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
