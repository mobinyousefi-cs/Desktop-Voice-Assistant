#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_wikipedia.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Answers general knowledge questions via Wikipedia; falls back to WolframAlpha when configured.

Usage:
"wikipedia Alan Turing" or "who is Ada Lovelace".

===================================================================
"""
from __future__ import annotations

import wikipedia
from typing import Optional

from .base import Skill
from ..config import Config

try:
    import wolframalpha  # type: ignore
except Exception:  # pragma: no cover
    wolframalpha = None


class WikipediaSkill(Skill):
    name = "wikipedia"

    def __init__(self, cfg: Config):
        self.cfg = cfg
        wikipedia.set_lang("en")
        self._wolfram_client = None
        if self.cfg.wolfram_app_id and wolframalpha:
            try:
                self._wolfram_client = wolframalpha.Client(self.cfg.wolfram_app_id)
            except Exception:
                self._wolfram_client = None

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "wikipedia"

    def handle(self, ctx, intent_name: str, slots: dict):
        q = slots.get("query") or "Python (programming language)"
        try:
            summary = wikipedia.summary(q, sentences=2, auto_suggest=True, redirect=True)
            msg = summary
        except Exception:
            msg = None
        if not msg and self._wolfram_client:
            try:
                res = self._wolfram_client.query(q)
                msg = next(res.results).text  # type: ignore
            except Exception:
                msg = None
        if not msg:
            msg = f"Sorry, I couldn't find an answer for '{q}'."
        ctx.speak(msg)
        return msg