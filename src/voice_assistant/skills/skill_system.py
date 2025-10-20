#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_system.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Safe system actions (announce only by default). Real power actions require opt-in flag.

Usage:
Say: "shutdown" or "sleep" (will refuse unless enabled).

===================================================================
"""
from __future__ import annotations

import platform
import subprocess

from .base import Skill
from ..config import Config


class SystemSkill(Skill):
    name = "system"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "system"

    def handle(self, ctx, intent_name: str, slots: dict):
        if not self.cfg.allow_system_power:
            msg = "System power actions are disabled for safety."
            ctx.speak(msg)
            return msg
        os_name = platform.system().lower()
        # Example: implement sleep on Windows/macOS/Linux guardedly
        try:
            if os_name == "windows":
                subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0", "1", "0"], check=False)
                msg = "Attempted to put the system to sleep."
            elif os_name == "darwin":
                subprocess.run(["pmset", "sleepnow"], check=False)
                msg = "Attempted to put the system to sleep."
            else:
                subprocess.run(["systemctl", "suspend"], check=False)
                msg = "Attempted to put the system to sleep."
        except Exception:
            msg = "Failed to execute the system action."
        ctx.speak(msg)
        return msg