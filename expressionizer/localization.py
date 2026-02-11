from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Literal, Optional


LocaleTag = Literal["en"] | str


@dataclass
class ExplanationProfile:
    locale: LocaleTag = "en"
    missing_key_policy: Literal["fallback", "marker", "error"] = "fallback"
    message_overrides: dict[str, str] = field(default_factory=dict)
    exact_text_overrides: dict[str, str] = field(default_factory=dict)


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
        missing_key_policy: Literal["fallback", "marker", "error"] = "fallback",
        message_overrides: Optional[dict[str, str]] = None,
        exact_text_overrides: Optional[dict[str, str]] = None,
    ):
        self.locale = (locale or "en").lower()
        self.missing_key_policy = missing_key_policy
        self.message_overrides = message_overrides or {}
        self.exact_text_overrides = exact_text_overrides or {}

    _template_ref_pattern = re.compile(r"\{\{([a-zA-Z0-9_.-]+)\}\}")

    @classmethod
    def from_profile(cls, profile: Optional[ExplanationProfile]) -> "Localizer":
        if profile is None:
            return cls()
        return cls(
            locale=profile.locale,
            missing_key_policy=profile.missing_key_policy,
            message_overrides=profile.message_overrides,
            exact_text_overrides=profile.exact_text_overrides,
        )

    def template(self, key: str, default: Optional[str] = None) -> str:
        value = self.message_overrides.get(key)
        if value is not None:
            return value
        if self.missing_key_policy == "error":
            raise KeyError(f"Missing localization key: {key}")
        if default is not None:
            return default
        if self.missing_key_policy == "fallback":
            return ""
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
            return self.exact_text_overrides[text]
        return text

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
