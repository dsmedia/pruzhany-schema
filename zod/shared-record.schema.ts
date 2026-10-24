import { z } from 'zod/v4';
import {
	FactSchema,
	NameSchema,
	FateSchema,
	SourceSchema,
	AttributionSchema,
	SourcedDateSchema,
	CitationSchema,
} from './sourced-entities.schema';
import {
	GenderSchema,
	LocationTypesSchema,
	EventTypesSchema,
	EventPartsSchema,
	eventPartKinds,
	vocabularyVersion,
} from './sourced-entities.vocabulary';
import { PrintedAddressSchema, siteText, siteDay, uniqueIds } from './site-common.schema';

// Located notice evidence written by the site writer. An older Citation without
// addresses retains its locator and quote verbatim, even after a rereading.
export const SiteCitationSchema = CitationSchema.safeExtend({
	addresses: z.array(PrintedAddressSchema).min(1).nullish(),
}).superRefine((v, ctx) => {
	if (!v.addresses) return;
	if (!v.unit_id?.trim() || !siteDay.safeParse(v.edition_date).success || !v.quote?.trim())
		ctx.addIssue({
			code: 'custom',
			message: 'located notice citation needs content item, issue date and quote',
		});
	else if (
		!v.addresses
			.map((a) => a.text)
			.join('\n')
			.includes(v.quote)
	)
		ctx.addIssue({ code: 'custom', message: 'citation quote must occur at its printed address' });
});
export type SiteCitation = z.infer<typeof SiteCitationSchema>;

// Released names with the site's located evidence; supplied attribution is inherited.
export const SharedNameSchema = NameSchema.safeExtend({
	citations: z.array(SiteCitationSchema).nullish(),
});
export type SharedName = z.infer<typeof SharedNameSchema>;
export function isPrintedName(name: SharedName): boolean {
	return name.kind === 'printed';
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
export const LifeEventMainPersonSchema = z.strictObject({
	person_id: siteText,
	part: EventPartsSchema,
});
export type LifeEventMainPerson = z.infer<typeof LifeEventMainPersonSchema>;

// Fact and standing reuse the production contract, including its sources and review.
export const SharedFactSchema = FactSchema.safeExtend({
	citations: z.array(SiteCitationSchema).min(1),
	subject_id: siteText,
	family_id: siteText.nullish(),
	representation: z.enum(['structured', 'prose', 'image']),
}).superRefine((v, ctx) => {
	// Legacy Fact still reads parenthood; the current site writer must use a child person.
	if (v.type === 'parenthood' || v.proposed_type === 'parenthood')
		ctx.addIssue({
			code: 'custom',
			message: 'parenthood is deprecated; use parent_of to a child person',
		});
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
	citations: z.array(SiteCitationSchema).min(1),
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
		v.citations.some((c) => c.addresses) &&
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
// An outside id of a place (rico:Identifier), read on its authority's own pages: the
// authority list is a registered source, so its host and address form are described once.
// Carried only on evidence, never from a name match (vetting §4).
export const PlaceIdentifierSchema = z.strictObject({
	source_id: siteText,
	value: siteText,
	url: z.url({ protocol: /^https$/ }).nullish(),
	accessed: siteDay,
	attribution: AttributionSchema,
});
export type PlaceIdentifier = z.infer<typeof PlaceIdentifierSchema>;
export const SharedPlaceSchema = z
	.strictObject({
		...identity,
		type: LocationTypesSchema,
		parent_id: siteText.nullish(),
		coordinates: z.tuple([z.number().min(-90).max(90), z.number().min(-180).max(180)]).nullish(),
		identifiers: z.array(PlaceIdentifierSchema).min(1).nullish(),
	})
	.superRefine((v, ctx) => {
		for (const message of uniqueIds(
			(v.identifiers ?? []).map((i) => JSON.stringify([i.source_id, i.value])),
			'place identifier'
		))
			ctx.addIssue({ code: 'custom', message });
	});
export type SharedPlace = z.infer<typeof SharedPlaceSchema>;
export const SharedOrganizationSchema = z.strictObject(identity);
export type SharedOrganization = z.infer<typeof SharedOrganizationSchema>;
export const SharedEventSchema = z
	.strictObject({
		id: siteText,
		name: siteText,
		type: EventTypesSchema,
		proposed_type: siteText.nullish(),
		main_people: z.array(LifeEventMainPersonSchema),
		dates: z.array(LifeEventDateSchema).min(1),
		location_id: siteText.nullish(),
		description: z.string().nullish(),
	})
	.superRefine((v, ctx) => {
		const fail = (message: string) => ctx.addIssue({ code: 'custom', message });
		if ((v.type === 'other') !== !!v.proposed_type) fail('event proposed_type exactly for other');
		if (v.proposed_type && EventTypesSchema.safeParse(v.proposed_type).success)
			fail('released event kind cannot be proposed_type');
		for (const message of uniqueIds(
			v.main_people.map((p) => p.person_id),
			'event main person'
		))
			fail(message);
		const kind = v.proposed_type ?? v.type;
		for (const p of v.main_people)
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
	const hosts = new Map(v.sources.map((s) => [s.id, s.host]));
	const subjects = ids([...identities, ...v.events, ...v.relations]);
	const facts = new Map(v.facts.map((f) => [f.id, f]));
	const births = new Set<string>(),
		deaths = new Set<string>();
	for (const event of v.events) {
		if (event.location_id && !places.has(event.location_id))
			errors.push('unknown life event place');
		for (const p of event.main_people) {
			if (!persons.has(p.person_id)) errors.push('main person must resolve to a person');
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
		for (const c of f.citations)
			if (c.url && !onHost(c.url, hosts.get(c.source_id)))
				errors.push('citation off its source host');
	}
	const noticeRelations = new Set<string>();
	for (const relation of v.relations) {
		if (!persons.has(relation.subject_id)) errors.push('relation subject must be a person');
		if (relation.subject_id === relation.related_person_id) errors.push('self relation');
		if (relation.citations.some((c) => c.addresses)) {
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
	const identified = new Map<string, string>();
	for (const place of v.places)
		for (const identifier of place.identifiers ?? []) {
			if (!sources.has(identifier.source_id)) errors.push('unknown identifier source');
			if (identifier.url && !onHost(identifier.url, hosts.get(identifier.source_id)))
				errors.push('identifier off its source host');
			const key = JSON.stringify([identifier.source_id, identifier.value]);
			if ((identified.get(key) ?? place.id) !== place.id)
				errors.push('one identifier on two places');
			identified.set(key, place.id);
		}
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

// An address is on a source's host, or a subdomain of it; a source naming no host takes any.
export function onHost(url: string, host: string | null | undefined): boolean {
	if (!host) return true;
	const name = new URL(url).hostname.replace(/^www\./, '');
	return name === host || name.endsWith(`.${host}`);
}
