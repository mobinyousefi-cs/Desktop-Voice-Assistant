#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: config.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Configuration loader for API keys, feature flags, and defaults.

Usage:
python -c "from voice_assistant.config import Config; print(Config().as_dict())"

Notes:
- Loads from environment variables and optional .env file (python-dotenv).
- Keeps potentially dangerous actions opt-in via flags.

===================================================================
"""
from __future__ import annotations

from dataclasses import dataclass, field
import os
from pathlib import Path
from typing import Dict

try:
    from dotenv import load_dotenv

    load_dotenv()  # best-effort
except Exception:
    pass


@dataclass
class Config:
    app_name: str = "Mobin Desktop Voice Assistant"
    locale: str = os.getenv("VA_LOCALE", "en-US")
    wolfram_app_id: str | None = os.getenv("WOLFRAM_APP_ID")
    default_city: str = os.getenv("VA_DEFAULT_CITY", "Rome")

    # Safety & feature flags
    allow_system_power: bool = os.getenv("VA_ALLOW_SYSTEM_POWER", "0") == "1"
    allow_email: bool = os.getenv("VA_ALLOW_EMAIL", "0") == "1"

    # Email settings (used only if allow_email is True)
    smtp_host: str | None = os.getenv("VA_SMTP_HOST")
    smtp_port: int = int(os.getenv("VA_SMTP_PORT", "587"))
    smtp_user: str | None = os.getenv("VA_SMTP_USER")
    smtp_password: str | None = os.getenv("VA_SMTP_PASSWORD")
    smtp_use_tls: bool = os.getenv("VA_SMTP_TLS", "1") == "1"
    email_sender: str | None = os.getenv("VA_EMAIL_SENDER")

    # STT engine
    recognizer_timeout: int = int(os.getenv("VA_RECOGNIZER_TIMEOUT", "6"))

    # TTS voice preferences (pyttsx3 property names)
    tts_rate: int = int(os.getenv("VA_TTS_RATE", "180"))
    tts_volume: float = float(os.getenv("VA_TTS_VOLUME", "1.0"))
    tts_voice_contains: str | None = os.getenv("VA_TTS_VOICE", None)

    extra: Dict[str, str] = field(default_factory=dict)

    def as_dict(self) -> Dict[str, str]:
        return {
            "app_name": self.app_name,
            "locale": self.locale,
            "wolfram_app_id": bool(self.wolfram_app_id),
            "default_city": self.default_city,
            "allow_system_power": self.allow_system_power,
            "allow_email": self.allow_email,
            "smtp_host": bool(self.smtp_host),
            "smtp_user": bool(self.smtp_user),
            "email_sender": bool(self.email_sender),
            "recognizer_timeout": self.recognizer_timeout,
            "tts_rate": self.tts_rate,
            "tts_volume": self.tts_volume,
            "tts_voice_contains": self.tts_voice_contains,
        }

    @staticmethod
    def project_root() -> Path:
        return Path(__file__).resolve().parents[2]