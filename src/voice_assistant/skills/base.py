#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: base.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Skill base class and registry utilities.

Usage:
Subclass Skill and implement can_handle/handle.

===================================================================
"""
from __future__ import annotations

from typing import Optional, Protocol


class Context(Protocol):
    def speak(self, text: str) -> None: ...


class Skill:
    name: str = "base"

    def can_handle(self, intent_name: str) -> bool:
        return False

    def handle(self, ctx: Context, intent_name: str, slots: dict) -> Optional[str]:
        raise NotImplementedError