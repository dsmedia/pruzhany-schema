import { z } from 'zod/v4';
import { ENGLISH_FIELDS, REQUIRE_NON_ENGLISH_QUOTE_ENGLISH } from './generated/words_policy';

// A present rendering always translates these exact words. The later rollout only
// switches mandatory quote coverage; it never permits a stale or orphan rendering.
export function englishIssues(
	model: keyof typeof ENGLISH_FIELDS,
	value: object,
	requireQuoteEnglish: boolean = REQUIRE_NON_ENGLISH_QUOTE_ENGLISH
): { message: string; path: string[] }[] {
	const issues: { message: string; path: string[] }[] = [];
	const fields = value as Record<string, unknown>;
	for (const [englishField, originalField] of Object.entries(ENGLISH_FIELDS[model])) {
		const english = fields[englishField] as { based_on: { source_text: string } } | null;
		if (english && english.based_on.source_text !== fields[originalField])
			issues.push({
				path: [englishField, 'based_on', 'source_text'],
				message: `${englishField} must translate exactly ${originalField}`,
			});
	}
	if (
		requireQuoteEnglish &&
		(model === 'Citation' || model === 'SiteCitation') &&
		typeof fields.quote === 'string' &&
		/\S/.test(fields.quote) &&
		!(typeof fields.quote_language === 'string' && /^[eE][nN](-|$)/.test(fields.quote_language)) &&
		!fields.quote_english
	)
		issues.push({
			path: ['quote_english'],
			message: 'a quote not explicitly marked as English needs quote_english',
		});
	return issues;
}

export function addEnglishIssues(
	model: keyof typeof ENGLISH_FIELDS,
	value: object,
	ctx: z.RefinementCtx,
	requireQuoteEnglish: boolean = REQUIRE_NON_ENGLISH_QUOTE_ENGLISH
): void {
	for (const issue of englishIssues(model, value, requireQuoteEnglish))
		ctx.addIssue({ code: 'custom', ...issue });
}
