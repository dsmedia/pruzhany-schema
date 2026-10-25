import { describe, expect, it } from 'vitest';
import { MediaSchema, PublicMediaSchema, publicMedia } from './media.schema';

const medium = {
	id: 'media-fictional',
	source_id: 'source-fictional',
	kind: 'image' as const,
	caption: { text: 'A fictional picture.', lang: 'en' },
	alt: { text: 'A square.', lang: 'en' },
	depicted: [],
	shows_unidentified: false,
	credit: 'Courtesy of the fixture family',
	master: {
		bucket: 'fixture-private-masters',
		key: 'private/' + 'a'.repeat(64),
		sha256: 'a'.repeat(64),
		mime: 'image/png',
		bytes: 128,
	},
};

describe('the media publication boundary', () => {
	it('keeps every master field private, with and without clearance', () => {
		for (const cleared of [undefined, { role: 'owner', on: '2026-10-24' }]) {
			const input = MediaSchema.parse({ ...medium, cleared });
			const output = publicMedia(input);
			expect(output).toEqual({
				id: input.id,
				source_id: input.source_id,
				kind: input.kind,
				caption: input.caption,
				alt: input.alt,
				depicted: [],
				shows_unidentified: false,
				credit: input.credit,
				rights: input.rights,
				cleared,
			});
			expect(JSON.stringify(output)).not.toMatch(/master|private\/|sha256|image\/png|"bytes"/);
			expect(PublicMediaSchema.safeParse(input).success).toBe(false);
			expect(input.master).toEqual(medium.master);
		}
	});
	it('revalidates before projection and refuses an uncleared served address', () => {
		const input = MediaSchema.parse(medium);
		input.width = 400;
		input.height = 200;
		input.derived = [
			{
				url: 'https://pictures.pruzhanychronicles.org/media/bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb-w400.webp',
				width: 400,
				height: 200,
				process: 'resize',
			},
		];
		expect(() => publicMedia(input)).toThrow('derived media needs clearance');
	});
});

describe('private consent and public dates', () => {
	it('never projects the grant, its reference, bucket name or fixity log', () => {
		const input = MediaSchema.parse({
			...medium,
			consent: {
				basis: 'family-permission',
				granted_by: 'family',
				ref: 'PRIVATE EMAIL',
				scope: { use: 'site', person_ids: [], unidentified: false },
			},
			master: { ...medium.master, checked: { on: '2026-10-24', sha256: 'a'.repeat(64) } },
			cleared: { role: 'owner', on: '2026-10-24' },
		});
		const publicValue = publicMedia(input);
		expect(JSON.stringify(publicValue)).not.toMatch(/PRIVATE|bucket|master|checked|sha256|consent/);
		expect(publicValue.cleared).toEqual({ role: 'owner', on: '2026-10-24' });
		expect(publicValue.rights).toBe('http://rightsstatements.org/vocab/CNE/1.0/');
	});
});
