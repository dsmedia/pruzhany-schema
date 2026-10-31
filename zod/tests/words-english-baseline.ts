// Exact ticket-02 additions to the frozen migration baseline. Production shapes
// are never imported here; existing fields, constraints and defaults stay checked.
import { z } from 'zod/v4';
import * as frozen from './identifiers-baseline';
export * from './identifiers-baseline';
const english = frozen.TranslationSchema.extend({
	based_on: frozen.TextBasisSchema.extend({
		addresses: z.array(frozen.PrintedAddressSchema).min(1).nullish(),
	}),
}).nullish();
export const SourceSchema = frozen.SourceSchema.extend({
	title_english: english,
});
export const CitationSchema = frozen.CitationSchema.safeExtend({
	quote_english: english,
});
export const FactSchema = frozen.FactSchema.safeExtend({
	citations: z.array(CitationSchema).min(1),
});
export const NameSchema = frozen.NameSchema.safeExtend({
	citations: z.array(CitationSchema).nullish(),
});
export const SiteCitationSchema = CitationSchema.safeExtend({
	addresses: frozen.SiteCitationSchema.shape.addresses,
});
export const SharedNameSchema = NameSchema.safeExtend({
	citations: z.array(SiteCitationSchema).nullish(),
});
export const SharedFactSchema = FactSchema.safeExtend({
	...frozen.SharedFactSchema.shape,
	citations: z.array(SiteCitationSchema).min(1),
});
export const SourcedRelationSchema = FactSchema.safeExtend({
	...frozen.SourcedRelationSchema.shape,
	citations: z.array(SiteCitationSchema).min(1),
});
export const SharedPersonSchema = frozen.SharedPersonSchema.extend({
	names: z.array(SharedNameSchema),
});
export const SharedFamilySchema = frozen.SharedFamilySchema.extend({ names: z.array(NameSchema) });
export const SharedPlaceSchema = frozen.SharedPlaceSchema.extend({ names: z.array(NameSchema) });
export const SharedOrganizationSchema = frozen.SharedOrganizationSchema.extend({
	names: z.array(NameSchema),
});
export const MediaFamilyWordsSchema = frozen.MediaFamilyWordsSchema.extend({
	quote_english: english,
});
export const PublicMediaSchema = frozen.PublicMediaSchema.safeExtend({
	family_words: MediaFamilyWordsSchema.nullish(),
});
export const MediaSchema = PublicMediaSchema.safeExtend({
	...frozen.MediaSchema.shape,
	family_words: MediaFamilyWordsSchema.nullish(),
});
export const SharedRecordSchema = frozen.SharedRecordSchema.safeExtend({
	persons: z.array(SharedPersonSchema),
	families: z.array(SharedFamilySchema),
	places: z.array(SharedPlaceSchema),
	organizations: z.array(SharedOrganizationSchema),
	sources: z.array(SourceSchema),
	facts: z.array(SharedFactSchema),
	relations: z.array(SourcedRelationSchema),
	media: z.array(MediaSchema).nullish(),
});
export const SiteArchiveSchema = frozen.SiteArchiveSchema.safeExtend({
	shared_record: SharedRecordSchema,
});
