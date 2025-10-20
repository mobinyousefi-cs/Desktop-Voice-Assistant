#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: stt.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Speech-to-text using SpeechRecognition; falls back to keyboard input when needed.

Usage:
from voice_assistant.stt import recognize_once; text = recognize_once()

===================================================================
"""
from __future__ import annotations

import speech_recognition as sr


def recognize_once(timeout: int = 6, phrase_time_limit: int = 6, language: str = "en-US") -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        return r.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""