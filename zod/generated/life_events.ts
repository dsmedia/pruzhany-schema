// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import { ContentUnitRolesEnum } from './enums';

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;

export const ContentItemRefShape = z.strictObject({
	content_item_id: z.string().regex(pattern1),
	role: ContentUnitRolesEnum,
});

export const IssueLifeEventShape = z.strictObject({
	id: z.string().regex(pattern1),
	content_items: z.array(ContentItemRefShape).min(1),
});

export const IssueLifeEventsDataShape = z.strictObject({
	issue_date: z.string().regex(pattern2),
	life_events: z.array(IssueLifeEventShape),
});
