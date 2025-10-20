#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: test_intents.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Minimal tests for intent parsing.

Usage:
pytest -q

===================================================================
"""
from voice_assistant.intents import parse_intent


def test_weather_in_city():
    it = parse_intent("weather in Rome")
    assert it and it.name == "weather" and it.slots.get("city") == "Rome"


def test_wikipedia_query():
    it = parse_intent("wikipedia Alan Turing")
    assert it and it.name == "wikipedia" and "Alan" in it.slots.get("query", "")


def test_no_intent():
    assert parse_intent("unrecognized command") is None