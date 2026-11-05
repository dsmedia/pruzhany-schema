// The catalog keys' exact optional addition to the picture-source baseline (5 November 2026).
// Independent shape declarations keep the frozen migration sources unchanged.
import { z } from 'zod/v4';
import * as frozen from './picture-source-baseline';
export * from './picture-source-baseline';

const key = z.string().regex(/^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])/);
const { newspapers } = frozen.EditionsCatalogSchema.shape;
const withoutNewspapers = frozen.EditionsCatalogSchema.omit({ newspapers: true });
// The definition places availableKeys before newspapers.
export const EditionsCatalogSchema = withoutNewspapers.extend({
	availableKeys: z.array(key).nullish(),
	newspapers,
});
