"""Deprecated — Diamonds uses Google Translate only (fixed Swedish UI strings)."""

from __future__ import annotations


def t(key: str) -> str:
    return key


def hint_for_section(_section: str) -> str:
    return ""


def render_lang_toggle() -> str:
    return "sv"
