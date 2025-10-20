#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_web.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Basic web search/open using default browser.

Usage:
"open github" or "search quantum metaheuristics".

===================================================================
"""
from __future__ import annotations

import urllib.parse
import webbrowser

from .base import Skill


class WebSkill(Skill):
    name = "web_search"

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "web_search"

    def handle(self, ctx, intent_name: str, slots: dict):
        q = slots.get("query") or "google"
        url = f"https://www.google.com/search?q={urllib.parse.quote_plus(q)}"
        webbrowser.open(url)
        msg = f"Searching the web for: {q}"
        ctx.speak(msg)
        return msg