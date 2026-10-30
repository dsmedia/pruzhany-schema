// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import { AddressGrainEnum, MentionRolesEnum } from './enums';
import { PrintedAddressShape } from './site_common';

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;

export const IssueMentionShape = z.strictObject({
	address_grain: AddressGrainEnum,
	addresses: z.array(PrintedAddressShape).min(1),
	content_item_id: z.string().regex(pattern1),
	function: z.string().nullish(),
	id: z.string().regex(pattern1),
	person_id: z.string().regex(pattern1),
	printed_name: z.string().regex(pattern1).nullish(),
	roles: z.array(MentionRolesEnum).min(1),
	title: z.string().nullish(),
	wkd_id: z.string().nullish(),
});

export const IssueMentionsDataShape = z.strictObject({
	issue_date: z.string().regex(pattern2),
	mentions: z.array(IssueMentionShape),
});
