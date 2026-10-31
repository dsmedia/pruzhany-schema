import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod/v4';
import * as current from './index';
import * as frozen from './tests/frozen';
import { BlockShape } from './generated/pages';
import { TitleCheckShape, TextBasisShape } from './generated/site_common';
import { SourcedRelationShape } from './generated/shared_record';
import { FactQualifiersShape } from './generated/sourced_entities';

// main e3e80c1, before ticket 20. The baseline copies only shape declarations;
// existing tests continue to exercise the unchanged production refinements.
// tsc checks every public schema, including all six documents and the site's
// .pick/.extend/.shape/.safeExtend dependencies (public.schema.ts, read 30 October 2026).
type Equal<A, B> =
	(<T>() => T extends A ? 1 : 2) extends <T>() => T extends B ? 1 : 2 ? true : false;
type SchemaKey = {
	[K in keyof typeof frozen]: (typeof frozen)[K] extends z.ZodType ? K : never;
}[keyof typeof frozen];
type Inferred<S> = S extends z.ZodType ? z.infer<S> : never;
// Owner-approved site-content 1.1.0, 31 October 2026 (docs/vocabulary-approvals.md).
// Keep the migration baseline frozen; prescribe only this exact version addition.
const titleReleaseVersions = ['0.1.0', '1.0.0', '1.1.0'] as const;
type ApprovedContentVersion<T> = {
	[K in keyof T]: K extends 'vocabulary_version' ? (typeof titleReleaseVersions)[number] : T[K];
};
type ApprovedIssueVersion<T> = {
	[K in keyof T]: K extends 'content_items' ? ApprovedContentVersion<T[K]> : T[K];
};
type ApprovedArchiveVersion<T> = {
	[K in keyof T]: K extends 'issues'
		? T[K] extends (infer Issue)[]
			? ApprovedIssueVersion<Issue>[]
			: never
		: T[K];
};
type ApprovedBaseline<K extends SchemaKey> = K extends 'ContentItemsDataSchema'
	? ApprovedContentVersion<Inferred<(typeof frozen)[K]>>
	: K extends 'SiteIssueSchema'
		? ApprovedIssueVersion<Inferred<(typeof frozen)[K]>>
		: K extends 'SiteArchiveSchema'
			? ApprovedArchiveVersion<Inferred<(typeof frozen)[K]>>
			: Inferred<(typeof frozen)[K]>;
const typeEquality: {
	[K in SchemaKey]: Equal<Inferred<(typeof current)[K]>, ApprovedBaseline<K>>;
} = {
	AttributionSchema: true,
	AuthorshipSchema: true,
	BboxSchema: true,
	BlockSchema: true,
	CitationSchema: true,
	ContentItemBlockRefSchema: true,
	ContentItemRefSchema: true,
	ContentItemSchema: true,
	ContentItemsDataSchema: true,
	ContentTypeSchema: true,
	CrossReferenceSchema: true,
	EditionSchema: true,
	EditionsCatalogSchema: true,
	EnglishCheckSchema: true,
	ExternalReferenceSchema: true,
	FactSchema: true,
	FateSchema: true,
	HistoricalEventSchema: true,
	HolderSchema: true,
	HolidaySchema: true,
	HolocaustFateSchema: true,
	IssueLifeEventSchema: true,
	IssueLifeEventsDataSchema: true,
	IssueMentionSchema: true,
	IssueMentionsDataSchema: true,
	LifeEventDateSchema: true,
	LifeEventMainPersonSchema: true,
	MediaConsentSchema: true,
	MediaConsentScopeSchema: true,
	MediaDecisionSchema: true,
	MediaDepictedSchema: true,
	MediaDerivativeSchema: true,
	MediaFamilyWordsSchema: true,
	MediaFixitySchema: true,
	MediaKindSchema: true,
	MediaMasterSchema: true,
	MediaPortraitSchema: true,
	MediaRegionSchema: true,
	MediaSchema: true,
	MediaTextSchema: true,
	MediaWithdrawalSchema: true,
	MentionSchema: true,
	NameSchema: true,
	PageSchema: true,
	PagesDataSchema: true,
	PlaceIdentifierSchema: true,
	PrintedAddressSchema: true,
	PrintedSectionSchema: true,
	PrintedTitleSchema: true,
	PublicMediaSchema: true,
	ReadingStatusSchema: true,
	ReadingStatusValueSchema: true,
	ReviewSchema: true,
	SharedEventSchema: true,
	SharedFactSchema: true,
	SharedFamilySchema: true,
	SharedNameSchema: true,
	SharedOrganizationSchema: true,
	SharedPersonSchema: true,
	SharedPlaceSchema: true,
	SharedRecordSchema: true,
	SiteArchiveSchema: true,
	SiteCitationSchema: true,
	SiteIssueSchema: true,
	SourceDerivationSchema: true,
	SourceHostSchema: true,
	SourceLanguageSchema: true,
	SourceSchema: true,
	SourcedDateSchema: true,
	SourcedRelationSchema: true,
	SuppliedTitleSchema: true,
	TextBasisSchema: true,
	TitleCheckSchema: true,
	TranslationCheckSchema: true,
	TranslationSchema: true,
	siteDay: true,
	siteText: true,
};
// Negative controls: presence, null, tuple positions and literals must all matter.
const equalityControls: [
	Equal<{ a?: string }, { a: string }>,
	Equal<string | null, string>,
	Equal<[number, number], number[]>,
	Equal<'en', string>,
] = [false, false, false, false];

const titleReleasePaths: Partial<Record<SchemaKey, string[]>> = {
	ContentItemsDataSchema: ['properties', 'vocabulary_version'],
	SiteIssueSchema: ['properties', 'content_items', 'properties', 'vocabulary_version'],
	SiteArchiveSchema: [
		'properties',
		'issues',
		'items',
		'properties',
		'content_items',
		'properties',
		'vocabulary_version',
	],
};

// Ticket 20's revised measure permits generated constraints to tighten exports.
// Normalize only these measured, non-widening changes; everything else must match.
function expectTightening(before: unknown, after: unknown, key = ''): void {
	if (Array.isArray(before) && Array.isArray(after)) {
		if (key === 'required') {
			expect([...after].sort()).toEqual([...before].sort());
			return;
		}
		expect(after).toHaveLength(before.length);
		before.forEach((value, i) => expectTightening(value, after[i], String(i)));
		return;
	}
	if (before && after && typeof before === 'object' && typeof after === 'object') {
		const old = { ...before } as Record<string, unknown>;
		const next = after as Record<string, unknown>;
		if (key === 'properties') expect(Object.keys(next)).toEqual(Object.keys(old));
		if (old.type === 'number' && next.type === 'integer') old.type = 'integer';
		// Positive integer spelling: > 0 and >= 1 have the same accepted values.
		if (old.type === 'integer' && old.exclusiveMinimum === 0 && next.minimum === 1) {
			delete old.exclusiveMinimum;
			old.minimum = 1;
		}
		for (const bound of ['minimum', 'maximum'] as const)
			if (!(bound in old) && typeof next[bound] === 'number' && old.type === 'integer')
				old[bound] = next[bound];
		// The absolute-end pattern implies the previous exact-length annotations.
		if (
			old.pattern === '^[0-9a-f]{64}$' &&
			old.minLength === 64 &&
			old.maxLength === 64 &&
			next.pattern === '^[0-9a-f]{64}$(?![\\s\\S])'
		) {
			delete old.minLength;
			delete old.maxLength;
			old.pattern = next.pattern;
		}
		if (
			old.format === 'uri' &&
			!('pattern' in old) &&
			next.pattern === '^https:\\/\\/[^\\s/?#]+[^\\s]*$'
		)
			old.pattern = next.pattern;
		expect(Object.keys(next).sort()).toEqual(Object.keys(old).sort());
		for (const field of Object.keys(old)) expectTightening(old[field], next[field], field);
		return;
	}
	expect(after).toEqual(before);
}

describe('generated shapes preserve the released Zod API', () => {
	it('checks the complete frozen schema inventory and equality helper', () => {
		expect(Object.keys(typeEquality).sort()).toEqual(
			Object.keys(frozen)
				.filter((key) => frozen[key as keyof typeof frozen] instanceof z.ZodType)
				.sort()
		);
		expect(equalityControls).toEqual([false, false, false, false]);
	});
	for (const name of Object.keys(typeEquality) as SchemaKey[]) {
		it(
			name + ' keeps its schema kind and JSON contract with the approved vocabulary release',
			() => {
				expect(current[name].constructor.name).toBe(frozen[name].constructor.name);
				const options = { target: 'draft-2020-12', io: 'output' } as const;
				const baseline = z.toJSONSchema(frozen[name], options);
				const versionPath = titleReleasePaths[name];
				if (versionPath) {
					let version = baseline as Record<string, unknown>;
					for (const key of versionPath) version = version[key] as Record<string, unknown>;
					expect(version.enum).toEqual(['0.1.0', '1.0.0']);
					version.enum = [...titleReleaseVersions];
				}
				expectTightening(baseline, z.toJSONSchema(current[name], options));
			}
		);
	}
});

it('keeps the published mention property, required-key and parsed key order', () => {
	// Supplied ticket-20 baseline: zod-exports-baseline/site-next/mentions.schema.json,
	// /properties/mentions/items. The local copy keeps this check bun-only in consumers.
	const baseline = JSON.parse(
		readFileSync(join(__dirname, 'tests/frozen/mentions.schema.json'), 'utf8')
	).properties.mentions.items;
	const exported = z.toJSONSchema(current.IssueMentionSchema, {
		target: 'draft-2020-12',
		io: 'output',
	});
	const order = Object.keys(baseline.properties);
	expect(Object.keys(exported.properties!)).toEqual(order);
	expect(exported.required).toEqual(baseline.required);
	// Reverse the input keys so the check observes the parser's serialization order.
	const mention = {
		addresses: [{ image_uri: 'fictional.png', bbox: [0, 0, 1, 1], text: 'Fictional name' }],
		roles: ['named'],
		address_grain: 'words',
		content_item_id: 'fictional-item',
		wkd_id: null,
		function: null,
		title: null,
		printed_name: 'Fictional name',
		person_id: 'fictional-person',
		id: 'fictional-mention',
	};
	expect(Object.keys(current.IssueMentionSchema.parse(mention))).toEqual(order);
	expect(Object.keys(PublicMention.parse(mention))).toEqual(
		Object.keys(FrozenPublicMention.parse(mention))
	);
});

it('refuses weakened types, patterns, bounds, URI formats and required keys', () => {
	for (const [before, after] of [
		[{ type: 'integer' }, { type: 'number' }],
		[{ type: 'string', pattern: '\\S' }, { type: 'string' }],
		[
			{ type: 'integer', minimum: 1 },
			{ type: 'integer', minimum: 0 },
		],
		[
			{ type: 'integer', maximum: 10 },
			{ type: 'integer', maximum: 11 },
		],
		[{ type: 'string', format: 'uri' }, { type: 'string' }],
		[{ required: ['id'] }, { required: [] }],
		[{ type: 'object', additionalProperties: false }, { type: 'object' }],
	])
		expect(() => expectTightening(before, after)).toThrow();
});

// Operations used by pruzhany-svelte/src/lib/data/public.schema.ts, read 30 October 2026.
const PublicSource = current.SourceSchema.pick({
	id: true,
	kind: true,
	title: true,
	work_id: true,
	author: true,
	editor: true,
	published: true,
	repository: true,
	url_pattern: true,
	host: true,
}).extend({ holder_name: z.string().trim().min(1).optional() });
const PublicCitation = z.object(current.CitationSchema.shape).omit({ note: true }).strict();
const PublicFact = current.FactSchema.safeExtend({ citations: z.array(PublicCitation).min(1) });
const PublicMention = z
	.object(current.IssueMentionSchema.shape)
	.omit({ roles: true })
	.extend({ roles: z.array(current.IssueMentionSchema.shape.roles.element) })
	.strict();
const PublicPlace = current.SharedPlaceSchema.omit({ names: true }).strict();
const PublicOrganization = current.SharedOrganizationSchema.omit({ names: true }).strict();
const DownloadPage = current.PageSchema.extend({
	blocks: z.array(
		current.BlockSchema.extend({
			transcription: z.union([z.string(), z.number().int().nonnegative()]),
		})
	),
});
const DownloadPages = current.PagesDataSchema.extend({ pages: z.array(DownloadPage) });
const FrozenPublicSource = frozen.SourceSchema.pick({
	id: true,
	kind: true,
	title: true,
	work_id: true,
	author: true,
	editor: true,
	published: true,
	repository: true,
	url_pattern: true,
	host: true,
}).extend({ holder_name: z.string().trim().min(1).optional() });
const FrozenPublicCitation = z.object(frozen.CitationSchema.shape).omit({ note: true }).strict();
const FrozenPublicFact = frozen.FactSchema.safeExtend({
	citations: z.array(FrozenPublicCitation).min(1),
});
const FrozenPublicMention = z
	.object(frozen.IssueMentionSchema.shape)
	.omit({ roles: true })
	.extend({ roles: z.array(frozen.IssueMentionSchema.shape.roles.element) })
	.strict();
const FrozenPublicPlace = frozen.SharedPlaceSchema.omit({ names: true }).strict();
const FrozenPublicOrganization = frozen.SharedOrganizationSchema.omit({ names: true }).strict();
const FrozenDownloadPage = frozen.PageSchema.extend({
	blocks: z.array(
		frozen.BlockSchema.extend({
			transcription: z.union([z.string(), z.number().int().nonnegative()]),
		})
	),
});
const FrozenDownloadPages = frozen.PagesDataSchema.extend({ pages: z.array(FrozenDownloadPage) });
const consumerTypeEquality: {
	PublicSource: Equal<z.infer<typeof PublicSource>, z.infer<typeof FrozenPublicSource>>;
	PublicCitation: Equal<z.infer<typeof PublicCitation>, z.infer<typeof FrozenPublicCitation>>;
	PublicFact: Equal<z.infer<typeof PublicFact>, z.infer<typeof FrozenPublicFact>>;
	PublicMention: Equal<z.infer<typeof PublicMention>, z.infer<typeof FrozenPublicMention>>;
	PublicPlace: Equal<z.infer<typeof PublicPlace>, z.infer<typeof FrozenPublicPlace>>;
	PublicOrganization: Equal<
		z.infer<typeof PublicOrganization>,
		z.infer<typeof FrozenPublicOrganization>
	>;
	DownloadPage: Equal<z.infer<typeof DownloadPage>, z.infer<typeof FrozenDownloadPage>>;
	DownloadPages: Equal<z.infer<typeof DownloadPages>, z.infer<typeof FrozenDownloadPages>>;
} = {
	PublicSource: true,
	PublicCitation: true,
	PublicFact: true,
	PublicMention: true,
	PublicPlace: true,
	PublicOrganization: true,
	DownloadPage: true,
	DownloadPages: true,
};

it('keeps the site’s schema composition API and inferred projections', () => {
	expect(Object.values(consumerTypeEquality).every(Boolean)).toBe(true);
});

it('retains calendar and host refinements inside generated parents', () => {
	expect(
		current.HolderSchema.safeParse({
			id: 'fictional-holder',
			name: 'Fictional holder',
			kind: 'institution',
			host: 'www.example.test',
		}).success
	).toBe(false);
	expect(
		current.SourceSchema.safeParse({
			id: 'fictional-source',
			kind: 'book',
			title: 'Fictional title',
			host: 'www.example.test',
		}).success
	).toBe(false);
	expect(
		current.SourceSchema.safeParse({
			id: 'fictional-source',
			kind: 'book',
			title: 'Fictional title',
			host: 'example.test',
		}).success
	).toBe(true);
	expect(
		current.SourceSchema.safeParse({
			id: 'fictional-source',
			kind: 'book',
			title: 'Fictional title',
			dated: { start: '1900-02-30' },
		}).success
	).toBe(false);
	expect(current.MediaDecisionSchema.safeParse({ role: 'owner', on: '1900-02-30' }).success).toBe(
		false
	);
	// safeExtend must retain Fact's refinements in the public projection.
	expect(
		PublicFact.safeParse({
			id: 'fictional-fact',
			type: 'occupation',
			citations: [{ source_id: 'fictional-source', locator: 'fictional-part' }],
			evidence_confidence: 'confirmed',
			identity_confidence: 'confirmed',
			status: 'accepted',
			review: { state: 'pending' },
			attribution: { by: 'Fictional reviewer', on: '2000-01-01' },
		}).success
	).toBe(false);
});

it('keeps formerly strict printed addresses strict', () => {
	expect(
		current.PrintedAddressSchema.safeParse({
			image_uri: 'fictional.png',
			bbox: [0, 0, 1, 1],
			text: '',
			extra: true,
		}).success
	).toBe(false);
});

it('retains generated integer ranges and box bounds in public pages', () => {
	const block = { id: 'fictional-block', bbox: [0, 0, 2, 3], transcription: '', unit_id: null };
	const page = {
		id: 'fictional-page',
		issue_date: '2000-01-01',
		page_number: 1,
		image_uri: 'fictional.png',
		dimensions: [20, 30],
		blocks: [block],
	};
	const document = { edition_date: '2000-01-01', pages: [page] };
	expect(current.PagesDataSchema.safeParse(document).success).toBe(true);
	for (const changed of [
		{ ...page, page_number: 1.5 },
		{ ...page, dimensions: [20.5, 30] },
		{ ...page, blocks: [{ ...block, bbox: [-1, 0, 2, 3] }] },
		{ ...page, blocks: [{ ...block, bbox: [0, 0, 2.5, 3] }] },
	]) {
		expect(frozen.PageSchema.safeParse(changed).success).toBe(true);
		expect(current.PageSchema.safeParse(changed).success).toBe(false);
	}
});

it('enforces generated bounds, array cardinality, map values and closedness', () => {
	const block = { id: 'fictional-block', bbox: [0, 0, 2, 3], transcription: '' };
	expect(BlockShape.safeParse(block).success).toBe(true);
	for (const bbox of [
		[0, 0, 2],
		[0, 0, 2, 3, 4],
		[-1, 0, 2, 3],
		[0.5, 0, 2, 3],
	])
		expect(BlockShape.safeParse({ ...block, bbox }).success).toBe(false);
	expect(BlockShape.safeParse({ ...block, extra: true }).success).toBe(false);
	expect(TextBasisShape.safeParse({ source_text: '', addresses: [] }).success).toBe(false);
	expect(FactQualifiersShape.safeParse({ fictional: 'text' }).success).toBe(true);
	expect(FactQualifiersShape.safeParse({ fictional: null }).success).toBe(false);
	// Raw optional LinkML slots remain nullish; the hand layer requires this nullable key.
	expect(BlockShape.safeParse({ ...block, unit_id: null }).success).toBe(true);
	expect(current.BlockSchema.safeParse(block).success).toBe(false);
});

it('enforces generated inherited fields, exact regex sources and enum intersections', () => {
	const check = {
		reading_id: 'fictional-reading',
		reading_sha256: 'a'.repeat(64),
		english_sha256: 'b'.repeat(64),
		judgement_sha256: 'c'.repeat(64),
		judgement_id: 'fictional:title',
		attribution: { by: 'Fictional checker', on: '2000-01-01', kind: 'person' },
	};
	expect(TitleCheckShape.safeParse(check).success).toBe(true);
	expect(TitleCheckShape.safeParse({ ...check, attribution: undefined }).success).toBe(false);
	expect(
		TitleCheckShape.safeParse({ ...check, reading_sha256: check.reading_sha256 + '\n' }).success
	).toBe(false);
	expect(TitleCheckShape.safeParse({ ...check, judgement_id: 'fictional:text' }).success).toBe(
		false
	);
	expect(SourcedRelationShape.shape.type.safeParse('kinship').success).toBe(true);
	expect(SourcedRelationShape.shape.type.safeParse('birth').success).toBe(false);
});
