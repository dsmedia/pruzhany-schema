// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';

const pattern1 = /\S/;

export const PictureSourceShape = z.strictObject({
	holder: z.string().regex(pattern1),
	route: z.string().regex(pattern1).nullish(),
	shelf_mark: z.string().regex(pattern1).nullish(),
	url: z.url().nullish(),
});
