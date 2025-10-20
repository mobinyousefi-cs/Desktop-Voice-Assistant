#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: app.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Application entry-point: wires config, TTS/STT, intents, skills, and optional GUI.

Usage:
python -m voice_assistant.app --gui
voice-assistant --cli

===================================================================
"""
from __future__ import annotations

import argparse
from typing import List, Optional

from .config import Config
from .tts import TTS
from .stt import recognize_once
from .intents import parse_intent
from .gui import run_gui

from .skills.skill_time import TimeSkill
from .skills.skill_weather import WeatherSkill
from .skills.skill_wikipedia import WikipediaSkill
from .skills.skill_web import WebSkill
from .skills.skill_jokes import JokeSkill
from .skills.skill_system import SystemSkill
from .skills.skill_email import EmailSkill
from .skills.skill_files import FilesSkill


class AppContext:
    def __init__(self, cfg: Config, tts: TTS):
        self.cfg = cfg
        self.tts = tts

    def speak(self, text: str) -> None:
        self.tts.say(text)


def _register_skills(cfg: Config) -> List:
    return [
        TimeSkill(),
        WeatherSkill(cfg),
        WikipediaSkill(cfg),
        WebSkill(),
        JokeSkill(),
        SystemSkill(cfg),
        EmailSkill(cfg),
        FilesSkill(),
    ]


def _dispatch(ctx: AppContext, text: str, skills: List) -> str:
    intent = parse_intent(text)
    if not intent:
        msg = "Sorry, I didn't understand."
        ctx.speak(msg)
        return msg
    for sk in skills:
        if sk.can_handle(intent.name):
            return sk.handle(ctx, intent.name, intent.slots) or ""
    msg = "I couldn't find a skill to handle that."
    ctx.speak(msg)
    return msg


def run_cli(cfg: Config):
    tts = TTS(rate=cfg.tts_rate, volume=cfg.tts_volume, voice_contains=cfg.tts_voice_contains)
    ctx = AppContext(cfg, tts)
    skills = _register_skills(cfg)
    print("Type text or /listen to use microphone. Ctrl+C to exit.")
    while True:
        try:
            q = input("> ").strip()
            if q == "/listen":
                heard = recognize_once(timeout=cfg.recognizer_timeout, language=cfg.locale)
                print(f"Heard: {heard}")
                if not heard:
                    continue
                ans = _dispatch(ctx, heard, skills)
                print(ans)
            else:
                ans = _dispatch(ctx, q, skills)
                print(ans)
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break


def run_gui_mode(cfg: Config):
    tts = TTS(rate=cfg.tts_rate, volume=cfg.tts_volume, voice_contains=cfg.tts_voice_contains)
    ctx = AppContext(cfg, tts)
    skills = _register_skills(cfg)

    def on_listen() -> str:
        heard = recognize_once(timeout=cfg.recognizer_timeout, language=cfg.locale)
        if heard:
            _dispatch(ctx, heard, skills)
        return heard

    def on_text(q: str) -> str:
        return _dispatch(ctx, q, skills)

    run_gui(cfg.app_name, on_listen, on_text)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="voice-assistant", description="Desktop Voice Assistant")
    parser.add_argument("--cli", action="store_true", help="run in CLI mode")
    parser.add_argument("--gui", action="store_true", help="run in GUI mode")
    args = parser.parse_args(argv)

    cfg = Config()

    if args.gui or not args.cli:
        run_gui_mode(cfg)
    else:
        run_cli(cfg)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())