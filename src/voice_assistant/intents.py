#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: intents.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Lightweight intent parser based on keyword patterns.

Usage:
from voice_assistant.intents import parse_intent; intent, args = parse_intent("what's the time in Rome?")

===================================================================
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Optional, Tuple


@dataclass
class Intent:
    name: str
    slots: Dict[str, str]


_PATTERNS = [
    ("time", re.compile(r"\b(time|what's the time|time in)\b", re.I)),
    ("weather", re.compile(r"\b(weather|temperature|forecast)\b", re.I)),
    ("wikipedia", re.compile(r"\b(wikipedia|who is|what is|tell me about)\b", re.I)),
    ("web_search", re.compile(r"\b(search|google|open)\b", re.I)),
    ("joke", re.compile(r"\b(joke|make me laugh)\b", re.I)),
    ("system", re.compile(r"\b(shutdown|sleep|lock)\b", re.I)),
    ("email", re.compile(r"\b(send email|email)\b", re.I)),
    ("file", re.compile(r"\b(open file|list files|move file)\b", re.I)),
]


def _extract_city(text: str) -> Optional[str]:
    m = re.search(r"in ([A-Z][a-zA-Z\s-]+)$", text.strip())
    return m.group(1) if m else None


def parse_intent(text: str) -> Optional[Intent]:
    if not text:
        return None
    for name, pat in _PATTERNS:
        if pat.search(text):
            if name == "weather":
                city = _extract_city(text)
                return Intent("weather", {"city": city} if city else {})
            if name == "wikipedia":
                q = re.sub(r"^(wikipedia|who is|what is|tell me about)\s+", "", text, flags=re.I)
                return Intent("wikipedia", {"query": q} if q else {})
            if name == "web_search":
                q = re.sub(r"^(search|google|open)\s+", "", text, flags=re.I)
                return Intent("web_search", {"query": q} if q else {})
            return Intent(name, {})
    return None