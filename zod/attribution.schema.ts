// Attribution is shared by evidence and English; keep the runtime module acyclic.
import { AttributionShape } from './generated/site_common';

export function validDate(v: string): boolean {
	const full = v + ({ 4: '-01-01', 7: '-01', 10: '' }[v.length] ?? 'invalid');
	const d = new Date(`${full}T00:00:00Z`);
	return (
		Number(v.slice(0, 4)) > 0 && !Number.isNaN(d.valueOf()) && d.toISOString().slice(0, 10) === full
	);
}
export const AttributionSchema = AttributionShape.extend({
	on: AttributionShape.shape.on.refine(validDate, 'invalid ISO day'),
});
