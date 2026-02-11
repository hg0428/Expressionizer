from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Literal, Optional

from .language_packs import StyleType, get_builtin_messages


LocaleTag = Literal["en"] | str


@dataclass
class ExplanationProfile:
    locale: LocaleTag = "en"
    style_type: StyleType = "default"
    missing_key_policy: Literal["fallback", "marker", "error"] = "fallback"
    message_overrides: dict[str, str] = field(default_factory=dict)
    exact_text_overrides: dict[str, str] = field(default_factory=dict)
    collect_diagnostics: bool = False


_PROFILE_PRESETS: dict[str, dict[str, Any]] = {
    # Baseline.
    "default": {},
    # Short, compact explanations for high-throughput data generation.
    "compact-research": {"style_type": "compact"},
    # Plain text headings/wrappers for logs and TSV-like exports.
    "plain-research": {"style_type": "plain"},
    # Structured wrapper profile for XML-oriented pipelines.
    "xml-research": {"style_type": "xml"},
    # Locale-focused presets.
    "spanish-default": {"locale": "es", "style_type": "default"},
    "korean-default": {"locale": "ko", "style_type": "default"},
    "hebrew-default": {"locale": "he", "style_type": "default"},
    "hebrew-niqqud-default": {"locale": "he-niqqud", "style_type": "default"},
}


def supported_profile_presets() -> list[str]:
    return sorted(_PROFILE_PRESETS.keys())


def build_explanation_profile(
    profile_preset: Optional[str] = None,
    *,
    locale: Optional[str] = None,
    style_type: Optional[StyleType] = None,
    missing_key_policy: Literal["fallback", "marker", "error"] = "fallback",
    message_overrides: Optional[dict[str, str]] = None,
    exact_text_overrides: Optional[dict[str, str]] = None,
    collect_diagnostics: bool = False,
) -> ExplanationProfile:
    merged: dict[str, Any] = {}
    if profile_preset:
        preset = _PROFILE_PRESETS.get(profile_preset)
        if preset is None:
            raise ValueError(
                f"Unknown profile preset '{profile_preset}'. Supported presets: {', '.join(supported_profile_presets())}"
            )
        merged.update(preset)
    if locale is not None:
        merged["locale"] = locale
    elif "locale" not in merged:
        merged["locale"] = "en"
    if style_type is not None:
        merged["style_type"] = style_type
    elif "style_type" not in merged:
        merged["style_type"] = "default"
    merged["missing_key_policy"] = missing_key_policy
    merged["message_overrides"] = message_overrides or {}
    merged["exact_text_overrides"] = exact_text_overrides or {}
    merged["collect_diagnostics"] = collect_diagnostics
    return ExplanationProfile(**merged)


def load_message_overrides(path: str) -> dict[str, str]:
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("messages file must be a JSON object of key -> string.")
    cleaned: dict[str, str] = {}
    for key, value in payload.items():
        if isinstance(value, str):
            cleaned[str(key)] = value
            continue
        raise ValueError(
            f"Invalid message override for key '{key}'. Expected string."
        )
    return cleaned


class Localizer:
    def __init__(
        self,
        locale: str = "en",
        style_type: StyleType = "default",
        missing_key_policy: Literal["fallback", "marker", "error"] = "fallback",
        message_overrides: Optional[dict[str, str]] = None,
        exact_text_overrides: Optional[dict[str, str]] = None,
    ):
        self.locale = (locale or "en").lower()
        self.style_type = style_type
        self.missing_key_policy = missing_key_policy
        self.message_overrides = message_overrides or {}
        self.exact_text_overrides = exact_text_overrides or {}
        self.builtin_messages = get_builtin_messages(self.locale, self.style_type)
        self.collect_diagnostics = False
        self._diagnostic_counts: dict[str, int] = {
            "override_hits": 0,
            "builtin_hits": 0,
            "default_hits": 0,
            "missing_hits": 0,
            "exact_text_override_hits": 0,
        }
        self._diagnostic_missing_keys: set[str] = set()
        self._diagnostic_used_keys: set[str] = set()

    _template_ref_pattern = re.compile(r"\{\{([a-zA-Z0-9_.-]+)\}\}")

    @classmethod
    def from_profile(cls, profile: Optional[ExplanationProfile]) -> "Localizer":
        if profile is None:
            return cls()
        localizer = cls(
            locale=profile.locale,
            style_type=profile.style_type,
            missing_key_policy=profile.missing_key_policy,
            message_overrides=profile.message_overrides,
            exact_text_overrides=profile.exact_text_overrides,
        )
        localizer.collect_diagnostics = bool(profile.collect_diagnostics)
        return localizer

    def template(
        self,
        key: str,
        default: Optional[str] = None,
        prefer_default: bool = False,
    ) -> str:
        value = self.message_overrides.get(key)
        if value is not None:
            self._record_diagnostic(key, "override_hits")
            return value
        if prefer_default and default is not None:
            self._record_diagnostic(key, "default_hits")
            return default
        builtin_value = self.builtin_messages.get(key)
        if builtin_value is not None:
            self._record_diagnostic(key, "builtin_hits")
            return builtin_value
        if self.missing_key_policy == "error":
            self._record_diagnostic(key, "missing_hits")
            raise KeyError(f"Missing localization key: {key}")
        if default is not None:
            self._record_diagnostic(key, "default_hits")
            return default
        if self.missing_key_policy == "fallback":
            self._record_diagnostic(key, "missing_hits")
            return ""
        self._record_diagnostic(key, "missing_hits")
        return f"[[{key}]]"

    def format(
        self,
        key: str,
        default: Optional[str] = None,
        payload: Optional[dict[str, Any]] = None,
    ) -> str:
        template = self._resolve_template_refs(self.template(key, default))
        if payload:
            try:
                return template.format(**payload)
            except Exception:
                return template
        return template

    def transform_text(self, text: str) -> str:
        if text in self.exact_text_overrides:
            if self.collect_diagnostics:
                self._diagnostic_counts["exact_text_override_hits"] += 1
            return self.exact_text_overrides[text]
        return text

    def diagnostics(self) -> dict[str, Any]:
        return {
            "counts": dict(self._diagnostic_counts),
            "missing_keys": sorted(self._diagnostic_missing_keys),
            "used_keys": sorted(self._diagnostic_used_keys),
        }

    def _record_diagnostic(self, key: str, bucket: str) -> None:
        if not self.collect_diagnostics:
            return
        self._diagnostic_counts[bucket] = self._diagnostic_counts.get(bucket, 0) + 1
        self._diagnostic_used_keys.add(key)
        if bucket == "missing_hits":
            self._diagnostic_missing_keys.add(key)

    def _resolve_template_refs(self, template: str, depth: int = 6) -> str:
        resolved = template
        for _ in range(depth):
            def _replace(match: re.Match[str]) -> str:
                ref_key = match.group(1)
                return self.template(ref_key)

            updated = self._template_ref_pattern.sub(_replace, resolved)
            if updated == resolved:
                break
            resolved = updated
        return resolved
