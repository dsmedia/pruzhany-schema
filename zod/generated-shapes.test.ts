import { describe, expect, it } from 'vitest';
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
const typeEquality: {
	[K in SchemaKey]: Equal<Inferred<(typeof current)[K]>, Inferred<(typeof frozen)[K]>>;
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
		it(name + ' keeps its schema kind and JSON export bytes', () => {
			expect(current[name].constructor.name).toBe(frozen[name].constructor.name);
			const options = { target: 'draft-2020-12', io: 'output' } as const;
			expect(JSON.stringify(z.toJSONSchema(current[name], options), null, '\t') + '\n').toBe(
				JSON.stringify(z.toJSONSchema(frozen[name], options), null, '\t') + '\n'
			);
		});
	}
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

it('keeps the released stripping and strict object policies', () => {
	const crossReference = {
		target_id: 'fictional-item',
		confidence: 1,
		relationship: 'fictional link',
		evidence: 'Fictional evidence',
	};
	expect(current.CrossReferenceSchema.parse({ ...crossReference, extra: true })).toEqual(
		crossReference
	);
	expect(
		current.EditionSchema.parse({
			date: '2000-01-01',
			hebrewDate: 'Fictional date',
			hebrewMonth: 1,
			hebrewYear: 5760,
			extra: true,
		})
	).not.toHaveProperty('extra');
	expect(
		current.PrintedAddressSchema.safeParse({
			image_uri: 'fictional.png',
			bbox: [0, 0, 1, 1],
			text: '',
			extra: true,
		}).success
	).toBe(false);
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
