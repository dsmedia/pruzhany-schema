import { describe, expect, it } from 'vitest';
import { MediaSchema, PublicMediaSchema, publicMedia } from './media.schema';

const medium = {
	id: 'media-fictional',
	source_id: 'source-fictional',
	kind: 'image' as const,
	caption: { text: 'A fictional picture.' },
	alt: { text: 'A square.' },
	master: {
		key: 'private/' + 'a'.repeat(64),
		sha256: 'a'.repeat(64),
		mime: 'image/png',
		bytes: 128,
	},
};

describe('the media publication boundary', () => {
	it('keeps every master field private, with and without clearance', () => {
		for (const cleared of [undefined, { by: 'Fixture owner', on: '2026-10-24' }]) {
			const input = MediaSchema.parse({ ...medium, cleared });
			const output = publicMedia(input);
			expect(output).toEqual({
				id: input.id,
				source_id: input.source_id,
				kind: input.kind,
				caption: input.caption,
				alt: input.alt,
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
				url: 'https://pictures.pruzhanychronicles.org/media/fictional-w400.webp',
				width: 400,
				height: 200,
			},
		];
		expect(() => publicMedia(input)).toThrow('derived media needs clearance');
	});
});
