// Frozen from main e3e80c1 for ticket 20: shapes only; never import production shapes here.
import { z } from 'zod/v4';
import { PagesDataSchema } from './page.schema';
import { MentionSchema } from './sourced-entities.schema';
import { MentionRolesSchema, ContentUnitRolesSchema } from './sourced-entities.vocabulary';
import { ContentItemsDataSchema } from './content-item.schema';
import { SharedRecordSchema } from './shared-record.schema';
import { PrintedAddressSchema, siteText, siteDay } from './site-common.schema';

// Mention: located words or whole regions, with a derived content item reference.
export const IssueMentionSchema = MentionSchema.omit({ unit_id: true, role: true }).extend({
	content_item_id: siteText,
	address_grain: z.enum(['words', 'regions']),
	printed_name: MentionSchema.shape.printed_name.nullable(),
	roles: z.array(MentionRolesSchema).min(1),
	addresses: z.array(PrintedAddressSchema).min(1),
});
export type IssueMention = z.infer<typeof IssueMentionSchema>;
export const IssueMentionsDataSchema = z.strictObject({
	issue_date: siteDay,
	mentions: z.array(IssueMentionSchema),
});
export type IssueMentionsData = z.infer<typeof IssueMentionsDataSchema>;

export const ContentItemRefSchema = z.strictObject({
	content_item_id: siteText,
	role: ContentUnitRolesSchema, // Role of the content item, not the person's role.
});
export type ContentItemRef = z.infer<typeof ContentItemRefSchema>;
export const IssueLifeEventSchema = z.strictObject({
	id: siteText,
	content_items: z.array(ContentItemRefSchema).min(1),
});
export type IssueLifeEvent = z.infer<typeof IssueLifeEventSchema>;
export const IssueLifeEventsDataSchema = z.strictObject({
	issue_date: siteDay,
	life_events: z.array(IssueLifeEventSchema),
});
export type IssueLifeEventsData = z.infer<typeof IssueLifeEventsDataSchema>;

// In-memory check of the four documents. Pages keep their existing file shape.
export const SiteIssueSchema = z.strictObject({
	pages: PagesDataSchema,
	content_items: ContentItemsDataSchema,
	mentions: IssueMentionsDataSchema,
	life_events: IssueLifeEventsDataSchema,
});
export type SiteIssue = z.infer<typeof SiteIssueSchema>;

export const SiteArchiveSchema = z.strictObject({
	shared_record: SharedRecordSchema,
	issues: z.array(SiteIssueSchema),
});
export type SiteArchive = z.infer<typeof SiteArchiveSchema>;
