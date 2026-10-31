// Ticket 03 additions to the immutable pre-generation baseline. All old fields and
// refinements still come from the frozen contracts; new fields have exact expectations.
import { z } from 'zod/v4';
import * as frozen from './frozen';
export * from './frozen';

export const PlaceIdentifierSchema = frozen.PlaceIdentifierSchema.extend({
	type: z.enum(['old_identifier']).nullish(),
});
const identifiers = z.array(PlaceIdentifierSchema).min(1).nullish();
export const HolderSchema = frozen.HolderSchema.extend({ identifiers });
export const SharedPlaceSchema = frozen.SharedPlaceSchema.extend({ identifiers });
export const SharedPersonSchema = frozen.SharedPersonSchema.extend({ identifiers });
export const SharedOrganizationSchema = frozen.SharedOrganizationSchema.extend({ identifiers });
export const SharedRecordSchema = frozen.SharedRecordSchema.safeExtend({
	persons: z.array(SharedPersonSchema),
	organizations: z.array(SharedOrganizationSchema),
	places: z.array(SharedPlaceSchema),
	holders: z.array(HolderSchema).optional(),
});
export const SiteArchiveSchema = frozen.SiteArchiveSchema.safeExtend({
	shared_record: SharedRecordSchema,
});
