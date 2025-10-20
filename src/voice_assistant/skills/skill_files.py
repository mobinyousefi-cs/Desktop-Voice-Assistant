#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_files.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Lightweight file operations (list/open) in a safe manner.

Usage:
Intent: "file"; operations could be extended.

===================================================================
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from .base import Skill


class FilesSkill(Skill):
    name = "file"

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "file"

    def handle(self, ctx, intent_name: str, slots: dict):
        # Demo: list current directory and open it
        cwd = Path.cwd()
        entries = ", ".join(sorted(p.name for p in cwd.iterdir())[:10])
        msg = f"Here are some files in {cwd}: {entries}"
        try:
            if sys.platform.startswith("win"):
                os.startfile(str(cwd))  # type: ignore
            elif sys.platform == "darwin":
                subprocess.run(["open", str(cwd)], check=False)
            else:
                subprocess.run(["xdg-open", str(cwd)], check=False)
        except Exception:
            pass
        ctx.speak(msg)
        return msg