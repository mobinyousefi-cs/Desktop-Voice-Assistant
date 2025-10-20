#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_jokes.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Tells a random programming joke.

Usage:
Say: "tell me a joke".

===================================================================
"""
from __future__ import annotations

import pyjokes

from .base import Skill


class JokeSkill(Skill):
    name = "joke"

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "joke"

    def handle(self, ctx, intent_name: str, slots: dict):
        joke = pyjokes.get_joke(category="neutral")
        ctx.speak(joke)
        return joke