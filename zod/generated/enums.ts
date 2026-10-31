// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';

export const AddressGrainEnum = z.enum(['words', 'regions']);

export const AuthorshipKindEnum = z.enum(['person', 'model']);

export const CitationRemarkKindsEnum = z.enum(['private_source_remark']);

export const ClaimStatusEnum = z.enum(['proposed', 'accepted', 'disputed', 'rejected']);

export const CompatibilityEventTypesEnum = z.enum([
	'wedding',
	'birth',
	'death',
	'bar_mitzvah',
	'celebration',
	'community_event',
	'holocaust_event',
	'other',
]);

export const ConfidenceEnum = z.enum(['confirmed', 'probable', 'possible']);

export const ContentItemSubtypesEnum = z.enum([
	'wedding_greeting',
	'engagement_greeting',
	'birth_greeting',
	'bar_mitzvah_greeting',
	'new_year_greeting',
	'departure_greeting',
	'greeting',
	'thanks',
	'meeting_notice',
	'announcement',
	'appeal',
	'commercial_advertisement',
	'condolence',
	'memorial_notice',
	'death_announcement',
	'editorial',
	'opinion',
	'letter',
	'poem',
	'sketch',
	'humour',
]);

export const ContentUnitRolesEnum = z.enum([
	'primary_announcement',
	'congratulation',
	'condolence',
	'mention',
	'advertisement',
]);

export const EventPartsEnum = z.enum([
	'baby',
	'parent',
	'bride',
	'groom',
	'boy',
	'deceased',
	'remembered',
]);

export const EventTypesEnum = z.enum([
	'engagement',
	'wedding',
	'birth',
	'death',
	'bar_mitzvah',
	'celebration',
	'community_event',
	'holocaust_event',
	'other',
	'memorial',
]);

export const ExternalSourceTypesEnum = z.enum([
	'arolsen_archives',
	'familysearch',
	'findagrave',
	'geni',
	'jewishgen',
	'jri_poland',
	'wikipedia',
	'yad_vashem',
]);

export const FactTypesEnum = z.enum([
	'birth',
	'death',
	'residence',
	'occupation',
	'office',
	'membership',
	'education',
	'emigration',
	'survival',
	'parenthood',
	'ghetto_role',
	'partisan_service',
	'deportation',
	'burial',
	'commemoration',
	'event_participation',
	'other',
	'kinship',
]);

export const FateOutcomesEnum = z.enum([
	'unknown',
	'perished',
	'survived',
	'died_before',
	'not_applicable',
]);

export const GenderEnum = z.enum(['male', 'female', 'unknown']);

export const HolderKindEnum = z.enum(['institution', 'family', 'private']);

export const HolocaustFateTypesEnum = z.enum([
	'unknown',
	'perished',
	'likely_perished',
	'survived',
	'likely_survived',
	'died_before',
	'not_applicable',
]);

export const IdentifierTypesEnum = z.enum(['old_identifier']);

export const ImpressoTypesEnum = z.enum([
	'article',
	'ad',
	'image',
	'table',
	'death_notice',
	'weather',
	'page',
	'radio_bulletin',
	'radio_broadcast_episode',
	'chronicle',
	'chapter',
	'discussion',
	'entertainment',
]);

export const LifeEventTypesEnum = z.enum([
	'wedding',
	'birth',
	'death',
	'bar_mitzvah',
	'celebration',
	'community_event',
	'other',
]);

export const LocationTypesEnum = z.enum([
	'city',
	'town',
	'village',
	'shtetl',
	'street',
	'address',
	'landmark',
	'country',
	'region',
	'district',
	'ghetto',
	'camp',
	'massacre_site',
	'deportation_point',
	'forest',
]);

export const MediaDecisionRoleEnum = z.enum(['owner', 'project']);

export const MediaGrantedByEnum = z.enum(['owner', 'family', 'holder', 'institution']);

export const MediaIdentifiedByEnum = z.enum(['family', 'record', 'inscription']);

export const MediaKindEnum = z.enum(['image', 'audio', 'video', 'document']);

export const MediaWithdrawalReasonEnum = z.enum(['family', 'holder', 'error']);

export const MentionRolesEnum = z.enum([
	'subject',
	'deceased',
	'honoree',
	'signer',
	'mourner',
	'advertiser',
	'author',
	'office_holder',
	'donor',
	'named',
	'betrothed',
	'parent',
]);

export const NameKindsEnum = z.enum([
	'printed',
	'birth',
	'married',
	'later',
	'nickname',
	'alias',
	'religious',
	'spelling',
	'supplied',
]);

export const PrintedCalendarEnum = z.enum(['gregorian', 'hebrew']);

export const ReadingStatusValueEnum = z.enum(['machine', 'session_checked', 'person_corrected']);

export const RelationshipTypesEnum = z.enum([
	'child_in_law',
	'child_of',
	'colleague',
	'cousin',
	'family_member',
	'friend',
	'grandchild_of',
	'grandparent_of',
	'in_law',
	'nephew_niece_of',
	'parent_in_law',
	'parent_of',
	'sibling',
	'sibling_in_law',
	'spouse',
	'student_of',
	'teacher_of',
	'uncle_aunt_of',
	'great_grandparent_of',
	'great_grandchild_of',
]);

export const ReviewStatesEnum = z.enum(['pending', 'approved']);

export const SharedFactRepresentationEnum = z.enum(['structured', 'prose', 'image']);

export const SourceDerivationRelationEnum = z.enum(['copy', 'transcription']);

export const SourceKindsEnum = z.enum([
	'archive_database',
	'book',
	'memorial_book',
	'oral_history',
	'memoir',
	'photograph',
	'press',
	'family_document',
	'web_page',
	'the_paper',
]);

export const SourceMadeByEnum = z.enum([
	'family',
	'studio',
	'institution',
	'perpetrator',
	'unknown',
]);

export const SourceQuoteConditionEnum = z.enum(['unique_information']);

export const SourcedDatePrecisionEnum = z.enum(['year', 'month', 'day', 'range']);

export const SubjectsEnum = z.enum([
	'education',
	'culture',
	'health',
	'palestine',
	'jewish_world',
	'literature',
	'sport',
	'economy',
	'community_affairs',
	'zionism',
	'international_affairs',
]);

export const TitleTypesEnum = z.enum(['printed', 'supplied']);

export const MediaRightsEnum = z.enum([
	'http://rightsstatements.org/vocab/InC/1.0/',
	'http://rightsstatements.org/vocab/InC-OW-EU/1.0/',
	'http://rightsstatements.org/vocab/InC-EDU/1.0/',
	'http://rightsstatements.org/vocab/InC-NC/1.0/',
	'http://rightsstatements.org/vocab/InC-RUU/1.0/',
	'http://rightsstatements.org/vocab/NoC-CR/1.0/',
	'http://rightsstatements.org/vocab/NoC-NC/1.0/',
	'http://rightsstatements.org/vocab/NoC-OKLR/1.0/',
	'http://rightsstatements.org/vocab/NoC-US/1.0/',
	'http://rightsstatements.org/vocab/CNE/1.0/',
	'http://rightsstatements.org/vocab/UND/1.0/',
	'http://rightsstatements.org/vocab/NKC/1.0/',
	'https://creativecommons.org/licenses/by/4.0/',
	'https://creativecommons.org/licenses/by-sa/4.0/',
	'https://creativecommons.org/licenses/by-nd/4.0/',
	'https://creativecommons.org/licenses/by-nc/4.0/',
	'https://creativecommons.org/licenses/by-nc-sa/4.0/',
	'https://creativecommons.org/licenses/by-nc-nd/4.0/',
	'https://creativecommons.org/publicdomain/zero/1.0/',
	'https://creativecommons.org/publicdomain/mark/1.0/',
]);

export const MediaConsentBasisEnum = z.enum([
	'institution-terms',
	'holder-licence',
	'family-permission',
	'public-domain',
	'owner-family-papers',
]);

export const MediaConsentScopeUseEnum = z.enum(['site', 'site+download']);

export const SourcedRelationTypeEnum = z.enum(['kinship', 'other']);
