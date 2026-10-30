// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';

export const ExternalReferenceShape = z.strictObject({
	notes: z.string().nullish(),
	record_id: z.string().nullish(),
	source: z.string(),
	url: z.string().nullish(),
	verified: z.boolean().nullish(),
});
