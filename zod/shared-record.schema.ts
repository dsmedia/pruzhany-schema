import { z } from 'zod/v4';
import {
	FactSchema,
	NameSchema,
	FateSchema,
	SourceSchema,
	AttributionSchema,
	SourcedDateSchema,
	CitationSchema,
	SourceHostSchema,
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
import { MediaSchema, MediaPortraitSchema, mediaReferenceErrors } from './media.schema';

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

// Printed dates keep their original rules. A record date refers to the preferred
// fact, whose SourcedDate retains ranges, inference and even an unknown date.
export const LifeEventDateSchema = z
	.strictObject({
		record_fact_id: siteText.nullish(),
		printed: SourcedDateSchema.shape.printed,
		printed_calendar: SourcedDateSchema.shape.printed_calendar,
		start: SourcedDateSchema.shape.start,
		qualifier: z.literal('reported_in').nullish(),
		reported_in: siteDay.nullish(),
	})
	.superRefine((v, ctx) => {
		const fail = (message: string) => ctx.addIssue({ code: 'custom', message });
		if (v.record_fact_id) {
			if (v.printed || v.printed_calendar || v.start || v.qualifier || v.reported_in)
				fail('record date must only name its fact');
			return;
		}
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
	portrait: MediaPortraitSchema.nullish(),
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
// Same evidence and uniqueness rules as places; a private holder's name is never public.
export const HolderSchema = z.strictObject({
	id: siteText,
	name: siteText,
	short_name: siteText.nullish(),
	kind: z.enum(['institution', 'family', 'private']),
	identifiers: z.array(PlaceIdentifierSchema).min(1).nullish(),
	host: SourceHostSchema.nullish(),
});
export type Holder = z.infer<typeof HolderSchema>;
// Plain object: the site derives its public place with .omit(). The identifiers' own
// rules (once per place, a registered authority, its host) are the shared record's.
export const SharedPlaceSchema = z.strictObject({
	...identity,
	type: LocationTypesSchema,
	parent_id: siteText.nullish(),
	coordinates: z.tuple([z.number().min(-90).max(90), z.number().min(-180).max(180)]).nullish(),
	identifiers: z.array(PlaceIdentifierSchema).min(1).nullish(),
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
		evidence_basis: z.literal('records_only').nullish(),
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
		if (v.dates.some((d) => d.record_fact_id)) {
			if (
				v.type !== 'death' ||
				!v.dates[0].record_fact_id ||
				v.dates.filter((d) => d.record_fact_id).length !== 1
			)
				fail('death must put its one preferred record date first');
			if (v.main_people.length !== 1 || v.main_people[0].part !== 'deceased')
				fail('record death needs one deceased person');
		}
		if (v.evidence_basis === 'records_only' && !v.dates[0]?.record_fact_id)
			fail('records-only death needs its preferred record fact');
		if (v.evidence_basis === 'records_only' && v.dates.length !== 1)
			fail('records-only death takes its date only from its preferred fact');
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
		holders: z.array(HolderSchema).optional(),
		facts: z.array(SharedFactSchema),
		relations: z.array(SourcedRelationSchema),
		media: z.array(MediaSchema).nullish(),
	})
	.superRefine((v, ctx) => {
		for (const message of sharedRecordErrors(v)) ctx.addIssue({ code: 'custom', message });
	});
export type SharedRecord = z.infer<typeof SharedRecordSchema>;

function sharedRecordErrors(v: SharedRecord): string[] {
	const identities = [...v.persons, ...v.families, ...v.places, ...v.organizations];
	const all = [
		...identities,
		...v.events,
		...v.sources,
		...(v.holders ?? []),
		...v.facts,
		...v.relations,
		...(v.media ?? []),
	];
	const errors = uniqueIds(
		all.map((x) => x.id),
		'shared id'
	);
	const ids = (xs: { id: string }[]) => new Set(xs.map((x) => x.id));
	errors.push(
		...mediaReferenceErrors(
			v.media ?? [],
			v.sources,
			ids([...v.persons, ...v.places, ...v.events]),
			v.persons
		)
	);
	const persons = ids(v.persons),
		places = ids(v.places),
		organizations = ids(v.organizations);
	const families = ids(v.families),
		events = ids(v.events),
		sources = ids(v.sources);
	const hosts = new Map(v.sources.map((s) => [s.id, s.host]));
	const paperSources = new Set(v.sources.filter((s) => s.kind === 'the_paper').map((s) => s.id));
	const holders = ids(v.holders ?? []);
	const bySource = new Map(v.sources.map((s) => [s.id, s]));
	for (const source of v.sources) {
		if (source.holder_id && !holders.has(source.holder_id)) errors.push('unknown source holder');
		for (const link of source.derived_from ?? [])
			if (!sources.has(link.source_id)) errors.push('unknown derived source');
	}
	const completed = new Set<string>();
	const visiting = new Set<string>();
	function visit(id: string): void {
		if (visiting.has(id)) {
			errors.push('derived_from cycle');
			return;
		}
		if (completed.has(id)) return;
		visiting.add(id);
		for (const link of bySource.get(id)?.derived_from ?? []) visit(link.source_id);
		visiting.delete(id);
		completed.add(id);
	}
	for (const id of sources) visit(id);
	function checkCitation(c: SiteCitation): void {
		if (c.url && !onHost(c.url, hosts.get(c.source_id)))
			errors.push('citation off its source host');
		if (c.via) {
			const via = bySource.get(c.via);
			if (!via) errors.push('unknown citation via');
			else if (!via.derived_from?.some((d) => d.source_id === c.source_id))
				errors.push('citation via must derive from its source');
		}
	}
	const subjects = ids([...identities, ...v.events, ...v.relations]);
	const facts = new Map(v.facts.map((f) => [f.id, f]));
	const deathEvents = new Map<string, string>();
	const births = new Set<string>(),
		deaths = new Set<string>();
	for (const event of v.events) {
		if (event.location_id && !places.has(event.location_id))
			errors.push('unknown life event place');
		for (const p of event.main_people) {
			if (event.type === 'death' && p.part === 'deceased') deathEvents.set(p.person_id, event.id);
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
		const recordDate = event.dates[0]?.record_fact_id;
		if (recordDate) {
			const fact = facts.get(recordDate);
			if (
				!fact ||
				fact.type !== 'death' ||
				fact.status !== 'accepted' ||
				fact.qualifiers?.support_kind !== 'record' ||
				fact.citations.some(
					(c) => paperSources.has(c.source_id) || (c.edition_date && c.unit_id)
				) ||
				fact.event_id !== event.id ||
				fact.subject_id !== event.main_people[0]?.person_id
			)
				errors.push('record date must name an accepted record statement of this death');
			if ((event.location_id ?? null) !== (fact?.place_id ?? null))
				errors.push('record death place must be its preferred statement place');
		}
	}
	for (const fact of v.facts)
		if (
			fact.type === 'death' &&
			fact.event_id &&
			deathEvents.get(fact.subject_id) !== fact.event_id
		)
			errors.push('death fact must name its person death event');
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
		for (const c of f.citations) checkCitation(c);
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
	for (const identity of identities) {
		if (identity.names.some((n) => n.citations?.some((c) => !sources.has(c.source_id))))
			errors.push('unknown name citation source');
		for (const name of identity.names) for (const c of name.citations ?? []) checkCitation(c);
	}
	for (const p of v.persons)
		if (p.fate?.rests_on.some((id) => facts.get(id)?.subject_id !== p.id))
			errors.push('fate must rest on own facts');
	for (const [entities, label] of [
		[v.places, 'places'],
		[v.holders ?? [], 'holders'],
	] as const) {
		const identified = new Map<string, string>();
		for (const place of entities) {
			errors.push(
				...uniqueIds(
					(place.identifiers ?? []).map((i) => JSON.stringify([i.source_id, i.value])),
					`${label === 'places' ? 'place' : 'holder'} identifier`
				)
			);
			for (const identifier of place.identifiers ?? []) {
				if (!sources.has(identifier.source_id)) errors.push('unknown identifier source');
				if (identifier.url && !onHost(identifier.url, hosts.get(identifier.source_id)))
					errors.push('identifier off its source host');
				const key = JSON.stringify([identifier.source_id, identifier.value]);
				if ((identified.get(key) ?? place.id) !== place.id)
					errors.push(`one identifier on two ${label}`);
				identified.set(key, place.id);
			}
		}
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
