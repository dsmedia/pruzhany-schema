"""Pydantic models for bbox review Gemini structured output.

These models define the response schema for Gemini's analysis of
bounding box annotations on newspaper pages.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class BboxCoords(BaseModel):
    """Bounding box coordinates in absolute pixels."""

    x: int = Field(description="Left edge x-coordinate in absolute pixels")
    y: int = Field(description="Top edge y-coordinate in absolute pixels")
    width: int = Field(description="Width in absolute pixels")
    height: int = Field(description="Height in absolute pixels")


class SubBlock(BaseModel):
    """A sub-region within a split bounding box."""

    sub_id: str = Field(
        description="Sub-block letter suffix assigned top-to-bottom: a, b, c, etc."
    )
    bbox: BboxCoords = Field(description="Bounding box coordinates for this sub-region")
    content_description: str = Field(
        description=(
            "Brief English description of the editorial content in this sub-region, "
            "e.g. 'Bereze kehillah budget report' or 'Start of White-Blue Ball notice'"
        )
    )


class BboxRecommendation(BaseModel):
    """Review recommendation for a single input bounding box."""

    annotation_id: int = Field(description="The annotation_id of the bounding box being reviewed")
    action: Literal["keep", "split"] = Field(
        description=(
            "keep: bbox aligns with exactly one unit (editorial or structural). "
            "split: bbox contains multiple units and should be divided."
        )
    )
    reason: str = Field(
        description="Explanation of why this action is recommended, referencing the content identified"
    )
    sub_blocks: list[SubBlock] = Field(
        description=(
            "For 'split': sub-block regions that tile the original bbox (same x/width, "
            "adjusted y/height for horizontal splits). For 'keep': empty list []."
        )
    )


class MergeGroup(BaseModel):
    """A set of sub-blocks from different bboxes that belong to the same article."""

    block_ids: list[str] = Field(
        description=(
            "Block identifiers to merge, formatted as 'annotation_id' + 'sub_id'. "
            "Example: ['13690b', '13691a'] for sub-block b of annotation 13690 "
            "and sub-block a of annotation 13691."
        )
    )
    reason: str = Field(
        description=(
            "Why these blocks belong to the same article, e.g. "
            "'Article continues from bottom of right column to top of left column'"
        )
    )


class PageReview(BaseModel):
    """Complete Gemini review of bounding boxes on one newspaper page."""

    page_number: int = Field(description="The newspaper page number (1-4)")
    recommendations: list[BboxRecommendation] = Field(
        description="One recommendation per input bounding box"
    )
    merges: list[MergeGroup] = Field(
        description=(
            "Groups of sub-blocks from different bboxes that should be merged into "
            "single content units (cross-column articles). Empty list if none detected."
        )
    )
    summary: str = Field(
        description="2-3 sentence summary: how many bboxes need changes, what issues were found"
    )


# ---------------------------------------------------------------------------
# Verification schemas (ADK VerifierAgent output)
# ---------------------------------------------------------------------------


class VerificationIssue(BaseModel):
    """An issue found by the VerifierAgent."""

    type: Literal["merge_rejected", "merge_uncertain", "split_imprecise", "tiling_invalid"] = Field(
        description="Category of the issue found during verification"
    )
    target: str = Field(
        description="Annotation ID or merge block_ids identifying the problematic element"
    )
    reason: str = Field(
        description="Human-readable explanation of why this is an issue"
    )


class VerificationResult(BaseModel):
    """VerifierAgent structured output."""

    approved: bool = Field(description="True if all decisions passed verification")
    merges_verified: int = Field(description="Number of merge groups visually verified")
    splits_verified: int = Field(description="Number of split boundaries visually verified")
    issues: list[VerificationIssue] = Field(
        description="List of issues found; empty if approved"
    )


# ---------------------------------------------------------------------------
# Gemini response types (0-1000 normalized coordinates)
# ---------------------------------------------------------------------------
# These mirror the absolute-pixel types above but use Gemini's native
# box_2d format. Passed as response_schema to Gemini, then converted to
# the absolute-pixel types for downstream processing.


class GeminiBbox(BaseModel):
    """Gemini native bounding box in 0-1000 normalized coords."""

    ymin: int = Field(description="Top edge, 0-1000 normalized")
    xmin: int = Field(description="Left edge, 0-1000 normalized")
    ymax: int = Field(description="Bottom edge, 0-1000 normalized")
    xmax: int = Field(description="Right edge, 0-1000 normalized")


class GeminiSubBlock(BaseModel):
    """A sub-region within a split bounding box (Gemini response format)."""

    sub_id: str = Field(
        description="Sub-block letter suffix assigned top-to-bottom: a, b, c, etc."
    )
    bbox: GeminiBbox = Field(description="Bounding box in 0-1000 normalized coords")
    content_description: str = Field(
        description=(
            "Brief English description of the editorial content in this sub-region, "
            "e.g. 'Bereze kehillah budget report' or 'Start of White-Blue Ball notice'"
        )
    )


class GeminiBboxRecommendation(BaseModel):
    """Review recommendation for a single input bounding box (Gemini response format)."""

    annotation_id: int = Field(description="The annotation_id of the bounding box being reviewed")
    action: Literal["keep", "split"] = Field(
        description=(
            "keep: bbox aligns with exactly one unit (editorial or structural). "
            "split: bbox contains multiple units and should be divided."
        )
    )
    reason: str = Field(
        description="Explanation of why this action is recommended, referencing the content identified"
    )
    sub_blocks: list[GeminiSubBlock] = Field(
        description=(
            "For 'split': sub-block regions that tile the original bbox (same xmin/xmax, "
            "adjusted ymin/ymax for horizontal splits). For 'keep': empty list []."
        )
    )


class GeminiPageReview(BaseModel):
    """Gemini response format for page review (0-1000 normalized coords).

    This is the response_schema passed to Gemini. After parsing, convert to
    PageReview (absolute pixels) via bbox_review._convert_to_absolute().
    """

    page_number: int = Field(description="The newspaper page number (1-4)")
    recommendations: list[GeminiBboxRecommendation] = Field(
        description="One recommendation per input bounding box"
    )
    merges: list[MergeGroup] = Field(
        description=(
            "Groups of sub-blocks from different bboxes that should be merged into "
            "single content units (cross-column articles). Empty list if none detected."
        )
    )
    summary: str = Field(
        description="2-3 sentence summary: how many bboxes need changes, what issues were found"
    )


# ---------------------------------------------------------------------------
# Second-pass verification schemas (0-1000 coords relative to each crop)
# ---------------------------------------------------------------------------
# After the first pass identifies splits/keeps/drops, a second pass crops
# tightly around each decision boundary for pixel-precise verification.


class GeminiBoundaryCheck(BaseModel):
    """Verification of one split boundary position in a cropped region."""

    crop_label: str = Field(
        description="Label identifying this crop from the prompt, e.g. 'split-13690-0'"
    )
    boundary_y: int = Field(
        description=(
            "0-1000 y-coordinate in this crop where the actual content boundary is. "
            "The proposed boundary is near the vertical center (~500). "
            "Report where you see the real boundary between editorial units."
        )
    )
    reason: str = Field(
        description="What you see at this boundary: headline, whitespace, horizontal rule, etc."
    )


class GeminiKeepCheck(BaseModel):
    """Verification that a keep bbox is truly a single editorial unit."""

    crop_label: str = Field(
        description="Label identifying this crop from the prompt, e.g. 'keep-13692'"
    )
    is_single_unit: bool = Field(
        description="True if this bbox contains exactly one editorial unit, False if it should be split"
    )
    split_y: int = Field(
        description=(
            "If is_single_unit is False: 0-1000 y-coordinate in this crop where the "
            "hidden article boundary is. If is_single_unit is True: set to 0."
        )
    )
    reason: str = Field(
        description="Brief description: single article confirmed, or hidden boundary details"
    )


class GeminiSecondPassReview(BaseModel):
    """Focused second-pass verification of first-pass decisions."""

    boundary_checks: list[GeminiBoundaryCheck] = Field(
        description="One check per split boundary crop, in order presented"
    )
    keep_checks: list[GeminiKeepCheck] = Field(
        description="One check per keep bbox crop, in order presented"
    )
    summary: str = Field(
        description="Brief summary: how many boundaries confirmed vs adjusted, any keeps needing splits"
    )


# ---------------------------------------------------------------------------
# Third-pass: cross-column continuation detection
# ---------------------------------------------------------------------------
# After splits and keeps are finalized, check adjacent columns for articles
# that flow from the bottom of one column to the top of the next (RTL).


class GeminiJunctionCheck(BaseModel):
    """Check for cross-column article continuation at one column junction."""

    junction_label: str = Field(
        description="Label identifying this junction from the prompt, e.g. 'junction-13690-13691a'"
    )
    has_continuation: bool = Field(
        description=(
            "True if the text at the bottom of the right column continues "
            "at the top of the left column (same article spanning columns)"
        )
    )
    right_split_y: int = Field(
        description=(
            "If has_continuation: 0-1000 y-coordinate in the RIGHT crop where the "
            "cross-column article BEGINS (content above is a different article). "
            "If the cross-column article fills the entire right crop, use 0. "
            "If no continuation: 0."
        )
    )
    left_end_y: int = Field(
        description=(
            "If has_continuation: 0-1000 y-coordinate in the LEFT crop where the "
            "cross-column article ENDS (content below is a different article). "
            "If the entire left crop is the continuation, use 1000. "
            "If no continuation: 0."
        )
    )
    reason: str = Field(
        description=(
            "Evidence: matching/mismatching content topics, presence or absence "
            "of headlines, mid-sentence continuation, etc."
        )
    )


class GeminiCrossColumnReview(BaseModel):
    """Cross-column continuation detection results."""

    junction_checks: list[GeminiJunctionCheck] = Field(
        description="One check per column junction, in order presented"
    )
    summary: str = Field(
        description="Brief summary: junctions checked, continuations found, content descriptions"
    )
