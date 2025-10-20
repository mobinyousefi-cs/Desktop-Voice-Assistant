#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_time.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Tells current local time.

Usage:
Registered skill; invoke via intent "time".

===================================================================
"""
from __future__ import annotations

from datetime import datetime

from .base import Skill


class TimeSkill(Skill):
    name = "time"

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "time"

    def handle(self, ctx, intent_name: str, slots: dict):
        now = datetime.now().strftime("%H:%M")
        msg = f"It's {now}."
        ctx.speak(msg)
        return msg