import { withFieldOrder } from './shared.schema';
import {
	PublicMediaShape,
	MediaDecisionShape,
	MediaTextShape,
	MediaRegionShape,
	MediaDepictedShape,
	MediaPortraitShape,
	MediaWithdrawalShape,
	MediaConsentScopeShape,
	MediaConsentShape,
	MediaFamilyWordsShape,
	MediaFixityShape,
	MediaMasterShape,
	MediaDerivativeShape,
	MediaShape,
} from './generated/media';
import { z } from 'zod/v4';
import { siteDay, siteText, uniqueIds } from './site-common.schema';

import type { Source } from './sourced-entities.schema';
import { MEDIA_WIDTH_LIST } from './media-widths.table';
import { MEDIA_RIGHTS, COPYRIGHT_NOT_EVALUATED } from './media-rights.table';
export { MEDIA_RIGHTS, COPYRIGHT_NOT_EVALUATED } from './media-rights.table';

export const MEDIA_WIDTHS: readonly number[] = MEDIA_WIDTH_LIST;
// Local RepresentationType concepts, linked by rico:hasRepresentationType.
export const MediaKindSchema = PublicMediaShape.shape.kind;
export const MediaDecisionSchema = withFieldOrder(
	MediaDecisionShape.extend({ on: siteDay }),
	'role on'
);
export type MediaDecision = z.infer<typeof MediaDecisionSchema>;
export const MediaTextSchema = withFieldOrder(
	MediaTextShape.extend({ reviewed: MediaDecisionSchema.nullish() }),
	'text lang reviewed'
);
export type MediaText = z.infer<typeof MediaTextSchema>;
const pixels = z.number().int().positive().max(Number.MAX_SAFE_INTEGER);
export const MediaRegionSchema = withFieldOrder(
	MediaRegionShape.extend({ w: pixels, h: pixels }),
	'x y w h'
);
export type MediaRegion = z.infer<typeof MediaRegionSchema>;
export const MediaDepictedSchema = withFieldOrder(
	MediaDepictedShape.extend({ person_id: siteText.nullable(), region: MediaRegionSchema }),
	'person_id region identified_by'
);
export const MediaPortraitSchema = withFieldOrder(
	MediaPortraitShape.extend({ region: MediaRegionSchema, reviewed: MediaDecisionSchema }),
	'media_id region reviewed'
);
export type MediaPortrait = z.infer<typeof MediaPortraitSchema>;
export const MediaWithdrawalSchema = withFieldOrder(
	MediaWithdrawalShape.extend({ on: siteDay }),
	'on reason'
);
export const MediaConsentScopeSchema = withFieldOrder(
	MediaConsentScopeShape,
	'use person_ids unidentified'
).superRefine((v, ctx) => {
	for (const message of uniqueIds(v.person_ids, 'consent person'))
		ctx.addIssue({ code: 'custom', message });
});
export const MediaConsentSchema = withFieldOrder(
	MediaConsentShape.extend({ scope: MediaConsentScopeSchema, withdrawn_on: siteDay.nullish() }),
	'basis granted_by scope ref withdrawn_on'
);
// A public Citation subset: exact words and their recorded part. No private note or locator.
export const MediaFamilyWordsSchema = withFieldOrder(
	MediaFamilyWordsShape,
	'source_id page quote quote_language'
);
export const MediaFixitySchema = withFieldOrder(
	MediaFixityShape.extend({ on: siteDay }),
	'on sha256'
);
export const MediaMasterSchema = withFieldOrder(
	MediaMasterShape.extend({ bytes: pixels, checked: MediaFixitySchema.nullish() }),
	'bucket key sha256 mime bytes checked'
).superRefine((v, ctx) => {
	const fail = (message: string) => ctx.addIssue({ code: 'custom', message });
	if (v.bucket === 'pruzhany-page-pictures') fail('master needs its own private bucket');
	if (v.key.split('/').at(-1) !== v.sha256) fail('master key must be named by its sha256');
	if (v.checked && v.checked.sha256 !== v.sha256) fail('master check must match its sha256');
});
export type MediaMaster = z.infer<typeof MediaMasterSchema>;
export const MediaDerivativeSchema = withFieldOrder(
	MediaDerivativeShape.extend({ width: pixels, height: pixels }),
	'url width height process'
);
export type MediaDerivative = z.infer<typeof MediaDerivativeSchema>;
const publicFields = withFieldOrder(
	PublicMediaShape.extend({
		caption: MediaTextSchema,
		alt: MediaTextSchema.nullish(),
		inscription: MediaTextSchema.nullish(),
		transcript: MediaTextSchema.nullish(),
		family_words: MediaFamilyWordsSchema.nullish(),
		depicted: z.array(MediaDepictedSchema),
		width: pixels.nullish(),
		height: pixels.nullish(),
		duration: z.number().positive().nullish(),
		rights: z.enum(MEDIA_RIGHTS).default(COPYRIGHT_NOT_EVALUATED).optional(),
		cleared: MediaDecisionSchema.nullish(),
		withdrawn: MediaWithdrawalSchema.nullish(),
		derived: z.array(MediaDerivativeSchema).min(1).nullish(),
	}),
	'id source_id kind caption alt inscription transcript family_words depicted shows_unidentified width height duration credit conditions_of_access conditions_of_use rights cleared withdrawn link derived'
);
export function regionFits(
	region: MediaRegion,
	width?: number | null,
	height?: number | null
): boolean {
	return !!width && !!height && region.x + region.w <= width && region.y + region.h <= height;
}
function mediaRules(v: z.infer<typeof publicFields>, ctx: z.RefinementCtx) {
	const fail = (message: string) => ctx.addIssue({ code: 'custom', message });
	if (['image', 'document'].includes(v.kind) && !v.alt) fail('image or document needs alt');
	if (v.kind === 'document' && !v.transcript) fail('document needs transcript');
	if (!!v.width !== !!v.height) fail('media width and height must occur together');
	if (v.link && !['audio', 'video'].includes(v.kind))
		fail('holder link is only for audio or video');
	if (v.withdrawn && (v.derived || v.link)) fail('withdrawn media cannot be served or linked');
	if (v.depicted.some((p) => p.person_id === null) && !v.shows_unidentified)
		fail('unidentified depiction needs shows_unidentified');
	for (const p of v.depicted)
		if (!regionFits(p.region, v.width, v.height)) fail('depicted region must fit master pixels');
	for (const message of uniqueIds(
		v.depicted.flatMap((p) => (p.person_id ? [p.person_id] : [])),
		'depicted person'
	))
		fail(message);
	if (v.kind === 'image' && v.rights === 'http://rightsstatements.org/vocab/InC-OW-EU/1.0/')
		fail('EU orphan-work statement excludes photographs');
	if (v.alt) {
		if ([...v.alt.text].length > 150) fail('alt must be at most 150 characters');
		if (v.alt.text.trim().toLowerCase() === v.caption.text.trim().toLowerCase())
			fail('alt must not repeat caption');
		if (
			v.alt.lang.toLowerCase().startsWith('en') &&
			/(^image of\b|\b(?:holocaust victim|before the war|unaware|doomed|happy|little did they know)\b)/i.test(
				v.alt.text.trim()
			)
		)
			fail('alt must describe only what is visible');
	}
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
			const nominal = Number(d.url.match(/-w(\d+)\.webp$/)?.[1]);
			if (d.width > nominal || (v.width && d.width > v.width) || (v.height && d.height > v.height))
				fail('derived picture cannot exceed its width or master');
		}
	}
}
export const MediaSchema = withFieldOrder(
	MediaShape.extend({
		...publicFields.shape,
		master: MediaMasterSchema.nullish(),
		consent: MediaConsentSchema.nullish(),
	}),
	'id source_id kind caption alt inscription transcript family_words depicted shows_unidentified width height duration credit conditions_of_access conditions_of_use rights cleared withdrawn link derived master consent'
)
	.superRefine(mediaRules)
	.superRefine((v, ctx) => {
		if (v.consent?.withdrawn_on && !v.withdrawn)
			ctx.addIssue({ code: 'custom', message: 'withdrawn consent needs withdrawn media state' });
	});
export type Media = z.infer<typeof MediaSchema>;
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
	subjects: Set<string>,
	persons: {
		id: string;
		name: string;
		names: { value: string }[];
		portrait?: MediaPortrait | null;
	}[] = []
): string[] {
	const errors: string[] = [];
	const bySource = new Map(sources.map((s) => [s.id, s]));
	const people = new Set(persons.map((p) => p.id));
	for (const source of sources) {
		errors.push(...uniqueIds(source.subjects ?? [], 'source subject'));
		if (source.subjects?.some((id) => !subjects.has(id)))
			errors.push('source subject must resolve to a person, place or event');
	}
	for (const medium of media) {
		const source = bySource.get(medium.source_id);
		if (!source) errors.push('unknown media source');
		if (medium.depicted.some((p) => p.person_id && !people.has(p.person_id)))
			errors.push('depicted person must resolve to a person');
		if (
			medium.consent?.scope.person_ids.some(
				(id) => !medium.depicted.some((p) => p.person_id === id)
			)
		)
			errors.push('consent person must be depicted');
		if (medium.family_words && !bySource.has(medium.family_words.source_id))
			errors.push('unknown family words source');
		if (medium.link) {
			const host = source?.host;
			const name = medium.link.split('/')[2];
			if (!host || !(name === host || name.endsWith(`.${host}`)))
				errors.push('media link must be on its holder host');
		}
		for (const person of persons) {
			if (medium.depicted.some((p) => p.person_id === person.id)) continue;
			for (const name of [person.name, ...person.names.map((n) => n.value)]) {
				const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
				if (
					medium.alt &&
					new RegExp(`(^|[^\\p{L}\\p{N}])${escaped}($|[^\\p{L}\\p{N}])`, 'iu').test(medium.alt.text)
				)
					errors.push('alt names must come from depicted people');
			}
		}
	}
	for (const person of persons) {
		if (!person.portrait) continue;
		const portrait = person.portrait;
		const medium = media.find((m) => m.id === portrait.media_id);
		if (
			!medium ||
			medium.kind !== 'image' ||
			!medium.cleared ||
			medium.withdrawn ||
			!medium.caption.reviewed ||
			!medium.depicted.some((p) => p.person_id === person.id) ||
			!regionFits(portrait.region, medium.width, medium.height)
		)
			errors.push(
				'portrait needs a cleared reviewed image depicting this person and a region in master pixels'
			);
	}
	return errors;
}
