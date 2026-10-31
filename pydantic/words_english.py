"""Exact source bindings; mandatory quote coverage follows the one LinkML switch."""
import re
from .generated.words_policy import ENGLISH_FIELDS, REQUIRE_NON_ENGLISH_QUOTE_ENGLISH


def validate_english(model, value, require_quote_english=None):
    if require_quote_english is None:
        require_quote_english = REQUIRE_NON_ENGLISH_QUOTE_ENGLISH
    for english_field, original_field in ENGLISH_FIELDS[model].items():
        english = getattr(value, english_field)
        if english is not None and english.based_on.source_text != getattr(value, original_field):
            raise ValueError(f'{english_field} must translate exactly {original_field}')
    if (require_quote_english and model in {'Citation', 'SiteCitation'}
            and value.quote and re.search(r'\S', value.quote)
            and not (value.quote_language and re.match(r'^[eE][nN](-|$)', value.quote_language))
            and value.quote_english is None):
        raise ValueError('a quote not explicitly marked as English needs quote_english')
    return value
