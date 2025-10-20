#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: tts.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Thin wrapper around pyttsx3 for text-to-speech.

Usage:
from voice_assistant.tts import TTS; TTS().say("Hello")

===================================================================
"""
from __future__ import annotations

import pyttsx3
from typing import Optional


class TTS:
    def __init__(self, rate: int = 180, volume: float = 1.0, voice_contains: Optional[str] = None):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)
        if voice_contains:
            for v in self.engine.getProperty("voices"):
                name = getattr(v, "name", "").lower()
                if voice_contains.lower() in name:
                    self.engine.setProperty("voice", v.id)
                    break

    def say(self, text: str, wait: bool = True) -> None:
        self.engine.say(text)
        if wait:
            self.engine.runAndWait()

    def stop(self) -> None:
        self.engine.stop()