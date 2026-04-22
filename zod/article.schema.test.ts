import { describe, it, expect } from 'vitest';
import { ArticleSchema, ArticleDataSchema } from './article.schema';

describe('Article Schemas', () => {
	describe('ArticleSchema', () => {
		it('accepts valid article', () => {
			const article = {
				annotation_id: 5746,
				page_number: 1,
				page_oid: 'pruzst19381216-01.1.1',
				bbox: { x: 1596.44, y: 2802.89, width: 487.11, height: 135.72 },
				masked_regions: [],
				image_file: '5746.png',
				visual_reasoning: '',
				confidence: 0.9,
				cross_references: [],
				cluster_ids: [],
				preliminary_transcription: 'Test text',
				preliminary_english_translation: 'Test translation',
				category: 'Wedding',
				content_summary: 'Test summary',
			};
			expect(() => ArticleSchema.parse(article)).not.toThrow();
		});

		it('rejects article without required bbox', () => {
			const article = {
				annotation_id: 5746,
				page_number: 1,
				page_oid: 'pruzst19381216-01.1.1',
				// missing bbox
			};
			expect(() => ArticleSchema.parse(article)).toThrow();
		});
	});

	describe('ArticleDataSchema', () => {
		it('accepts valid article data wrapper', () => {
			const data = {
				edition_date: '1938-12-16',
				run_id: 'test-run',
				model: 'gemini-3-flash-preview',
				article_count: 0,
				articles: [],
			};
			expect(() => ArticleDataSchema.parse(data)).not.toThrow();
		});
	});
});
