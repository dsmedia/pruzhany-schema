import { z } from 'zod/v4';
import { siteDay, siteText, uniqueIds } from './site-common.schema';
import type { Source } from './sourced-entities.schema';

// Local presentation kinds, not RiC-O ContentType values (media design §1).
export const MediaKindSchema = z.enum(['image', 'audio', 'video', 'document']);
export const MediaDecisionSchema = z.strictObject({ by: siteText, on: siteDay });
export type MediaDecision = z.infer<typeof MediaDecisionSchema>;
export const MediaTextSchema = z.strictObject({
	text: siteText,
	reviewed: MediaDecisionSchema.nullish(),
});
export type MediaText = z.infer<typeof MediaTextSchema>;

const digest = z.string().regex(/^[0-9a-f]{64}$(?![\s\S])/);
export const MediaMasterSchema = z
	.strictObject({
		key: z.string().regex(/^(?:[a-z0-9_-]+\/)*[0-9a-f]{64}$(?![\s\S])/),
		sha256: digest,
		mime: z.string().regex(/^(?:image|audio|video|application)\/[a-z0-9][a-z0-9.+-]*$(?![\s\S])/),
		bytes: z.number().int().positive().max(Number.MAX_SAFE_INTEGER),
	})
	.superRefine((v, ctx) => {
		if (v.key.split('/').at(-1) !== v.sha256)
			ctx.addIssue({ code: 'custom', message: 'master key must be named by its sha256' });
	});
export type MediaMaster = z.infer<typeof MediaMasterSchema>;

const pixels = z.number().int().positive().max(Number.MAX_SAFE_INTEGER);
export const MediaDerivativeSchema = z.strictObject({
	url: z
		.string()
		.regex(
			/^https:\/\/pictures\.pruzhanychronicles\.org\/(?:[a-z0-9_-]+\/)*[a-z0-9-]+-w(?:100|400|800|1200)\.webp$(?![\s\S])/
		),
	width: pixels,
	height: pixels,
});
export type MediaDerivative = z.infer<typeof MediaDerivativeSchema>;

const publicFields = z.strictObject({
	id: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$(?![\s\S])/),
	source_id: siteText,
	kind: MediaKindSchema,
	caption: MediaTextSchema,
	alt: MediaTextSchema.nullish(),
	width: pixels.nullish(),
	height: pixels.nullish(),
	// Seconds; no duration mapping is claimed in the pinned profile.
	duration: z.number().positive().nullish(),
	conditions_of_use: siteText.nullish(),
	rights: z
		.string()
		.regex(/^https?:\/\/(?:rightsstatements\.org|creativecommons\.org)\/[^\s\\]+$(?![\s\S])/)
		.nullish(),
	cleared: MediaDecisionSchema.nullish(),
	// A holder's page, never a served media file. Host checked through source_id.
	link: z
		.string()
		.regex(/^https:\/\/[a-z0-9]+(?:[.-][a-z0-9]+)*(?:\/[^\s\\]*)?$(?![\s\S])/)
		.nullish(),
	derived: z.array(MediaDerivativeSchema).min(1).nullish(),
});

function mediaRules(v: z.infer<typeof publicFields>, ctx: z.RefinementCtx) {
	const fail = (message: string) => ctx.addIssue({ code: 'custom', message });
	if (v.kind === 'image' && !v.alt) fail('image needs alt');
	if (!!v.width !== !!v.height) fail('media width and height must occur together');
	if (v.link && !['audio', 'video'].includes(v.kind))
		fail('holder link is only for audio or video');
	if (v.derived) {
		if (!v.cleared) fail('derived media needs clearance');
		if (!(v.width && v.height) && !v.duration) fail('derived media needs dimensions or duration');
		if (['image', 'document'].includes(v.kind) && !(v.width && v.height))
			fail('derived picture needs master dimensions');
		for (const message of uniqueIds(
			v.derived.map((d) => d.url),
			'derived address'
		))
			fail(message);
		for (const d of v.derived) {
			const nominal = Number(d.url.match(/-w(\d+)\.webp$(?![\s\S])/)?.[1]);
			if (d.width > nominal || (v.width && d.width > v.width) || (v.height && d.height > v.height))
				fail('derived picture cannot exceed its width or master');
		}
	}
}

export const MediaSchema = publicFields
	.extend({ master: MediaMasterSchema.nullish() })
	.superRefine(mediaRules);
export type Media = z.infer<typeof MediaSchema>;
// Strict: even master:null is refused at the public boundary.
export const PublicMediaSchema = publicFields.superRefine(mediaRules);
export type PublicMedia = z.infer<typeof PublicMediaSchema>;

export function publicMedia(value: Media): PublicMedia {
	const checked = MediaSchema.parse(value);
	return PublicMediaSchema.parse(
		Object.fromEntries(
			Object.keys(publicFields.shape)
				.filter((k) => k in checked)
				.map((k) => [k, checked[k as keyof Media]])
		)
	);
}

export function mediaReferenceErrors(
	media: Media[],
	sources: Source[],
	subjects: Set<string>
): string[] {
	const errors: string[] = [];
	const bySource = new Map(sources.map((s) => [s.id, s]));
	for (const source of sources) {
		errors.push(...uniqueIds(source.subjects ?? [], 'source subject'));
		if (source.subjects?.some((id) => !subjects.has(id)))
			errors.push('source subject must resolve to a person, place or event');
	}
	for (const medium of media) {
		const source = bySource.get(medium.source_id);
		if (!source) errors.push('unknown media source');
		if (medium.link) {
			// Ticket 01 replaces this source-host lookup with source.holder_id -> holder.host.
			const host = source?.host;
			// The link grammar already excludes credentials, ports and escaped hosts.
			const name = medium.link.split('/')[2];
			if (!host || !(name === host || name.endsWith(`.${host}`)))
				errors.push('media link must be on its holder host');
		}
	}
	return errors;
}
