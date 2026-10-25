/**
 * Emit the JSON Schema of every Zod model that has a Pydantic twin, for
 * check_lockstep.py to set beside the twin's model_json_schema().
 *
 *   bun tests/contract/dump_zod_schemas.ts
 *
 * Moved here from pruzhany-press/tests/contract/ on 2026-10-22, when that
 * repository was retired: its imports now resolve zod from this repository's
 * own locked node_modules, so the snapshot it needed there is not needed here.
 * A model whose export is absent is emitted as {"__missing__": true}, so the
 * Python side reports it as drift rather than crashing.
 */
import { z } from 'zod/v4';
import * as shared from '../../zod/shared.schema';
import * as sourced from '../../zod/sourced-entities.schema';
import * as site from '../../zod/index';

const targets: Record<string, unknown> = {
	MediaRegion: site.MediaRegionSchema,
	MediaDepicted: site.MediaDepictedSchema,
	MediaPortrait: site.MediaPortraitSchema,
	MediaWithdrawal: site.MediaWithdrawalSchema,
	MediaConsentScope: site.MediaConsentScopeSchema,
	MediaConsent: site.MediaConsentSchema,
	MediaFamilyWords: site.MediaFamilyWordsSchema,
	MediaFixity: site.MediaFixitySchema,

	MediaDecision: site.MediaDecisionSchema,
	MediaText: site.MediaTextSchema,
	MediaMaster: site.MediaMasterSchema,
	MediaDerivative: site.MediaDerivativeSchema,
	Media: site.MediaSchema,
	PublicMedia: site.PublicMediaSchema,
	Block: site.BlockSchema,
	Page: site.PageSchema,
	PagesData: site.PagesDataSchema,
	CrossReference: site.CrossReferenceSchema,
	ExternalReference: shared.ExternalReferenceSchema,
	SourcedDate: sourced.SourcedDateSchema,
	Review: sourced.ReviewSchema,
	Attribution: sourced.AttributionSchema,
	Source: sourced.SourceSchema,
	Citation: sourced.CitationSchema,
	Fact: sourced.FactSchema,
	Name: sourced.NameSchema,
	Fate: sourced.FateSchema,
	Mention: sourced.MentionSchema,
};

const out: Record<string, unknown> = {};
targets.Holder = site.HolderSchema;
targets.SourceDerivation = site.SourceDerivationSchema;
targets.EnglishCheck = site.EnglishCheckSchema;
targets.TitleCheck = site.TitleCheckSchema;
targets.TranslationCheck = site.TranslationCheckSchema;
targets.PrintedAddress = site.PrintedAddressSchema;
targets.TextBasis = site.TextBasisSchema;
targets.Authorship = site.AuthorshipSchema;
targets.PrintedTitle = site.PrintedTitleSchema;
targets.SuppliedTitle = site.SuppliedTitleSchema;
targets.Translation = site.TranslationSchema;
targets.ContentItemBlockRef = site.ContentItemBlockRefSchema;
targets.ContentItem = site.ContentItemSchema;
targets.PrintedSection = site.PrintedSectionSchema;
targets.ContentItemsData = site.ContentItemsDataSchema;
targets.SharedFact = site.SharedFactSchema;
targets.SourcedRelation = site.SourcedRelationSchema;
targets.SharedPerson = site.SharedPersonSchema;
targets.SharedFamily = site.SharedFamilySchema;
targets.PlaceIdentifier = site.PlaceIdentifierSchema;
targets.SharedPlace = site.SharedPlaceSchema;
targets.SharedOrganization = site.SharedOrganizationSchema;
targets.SharedEvent = site.SharedEventSchema;
targets.SharedName = site.SharedNameSchema;
targets.SiteCitation = site.SiteCitationSchema;
targets.LifeEventDate = site.LifeEventDateSchema;
targets.LifeEventMainPerson = site.LifeEventMainPersonSchema;
targets.SharedRecord = site.SharedRecordSchema;
targets.IssueMention = site.IssueMentionSchema;
targets.IssueMentionsData = site.IssueMentionsDataSchema;
targets.ContentItemRef = site.ContentItemRefSchema;
targets.IssueLifeEvent = site.IssueLifeEventSchema;
targets.IssueLifeEventsData = site.IssueLifeEventsDataSchema;
targets.SiteIssue = site.SiteIssueSchema;
targets.SiteArchive = site.SiteArchiveSchema;
for (const [name, schema] of Object.entries(targets)) {
	out[name] = schema === undefined ? { __missing__: true } : z.toJSONSchema(schema as never);
}

process.stdout.write(JSON.stringify(out));
