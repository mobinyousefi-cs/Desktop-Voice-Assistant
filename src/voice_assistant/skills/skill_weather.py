#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_weather.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Fetches simple weather info using wttr.in JSON (no API key required).

Usage:
Say: "weather in Rome" or "what's the weather" (uses default city).

===================================================================
"""
from __future__ import annotations

import json
from typing import Optional
import requests

from .base import Skill
from ..config import Config


def _wttr(city: str) -> Optional[str]:
    url = f"https://wttr.in/{city}?format=j1"
    r = requests.get(url, timeout=6)
    if r.status_code != 200:
        return None
    data = r.json()
    cur = data["current_condition"][0]
    temp_c = cur["temp_C"]
    desc = cur["weatherDesc"][0]["value"]
    feels = cur.get("FeelsLikeC", temp_c)
    return f"Weather in {city}: {desc}, {temp_c}°C (feels {feels}°C)."


class WeatherSkill(Skill):
    name = "weather"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "weather"

    def handle(self, ctx, intent_name: str, slots: dict):
        city = slots.get("city") or self.cfg.default_city
        try:
            msg = _wttr(city)
        except Exception:
            msg = None
        if not msg:
            msg = f"Sorry, I couldn't fetch the weather for {city}."
        ctx.speak(msg)
        return msg