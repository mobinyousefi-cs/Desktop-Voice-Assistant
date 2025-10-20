#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: skill_email.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Send a short email via SMTP when enabled.

Usage:
Programmatic invocation by intent "email".

===================================================================
"""
from __future__ import annotations

import smtplib
from email.message import EmailMessage

from .base import Skill
from ..config import Config


class EmailSkill(Skill):
    name = "email"

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def can_handle(self, intent_name: str) -> bool:
        return intent_name == "email"

    def handle(self, ctx, intent_name: str, slots: dict):
        if not self.cfg.allow_email:
            msg = "Email sending is disabled."
            ctx.speak(msg)
            return msg
        to = slots.get("to") or self.cfg.email_sender
        subject = slots.get("subject") or "Hello from your Assistant"
        body = slots.get("body") or "This is a test email."
        if not to:
            msg = "No recipient configured. Set VA_EMAIL_SENDER or provide 'to' slot."
            ctx.speak(msg)
            return msg
        try:
            m = EmailMessage()
            m["From"] = self.cfg.email_sender
            m["To"] = to
            m["Subject"] = subject
            m.set_content(body)

            if self.cfg.smtp_use_tls:
                server = smtplib.SMTP(self.cfg.smtp_host, self.cfg.smtp_port)
                server.starttls()
            else:
                server = smtplib.SMTP_SSL(self.cfg.smtp_host, self.cfg.smtp_port)
            server.login(self.cfg.smtp_user, self.cfg.smtp_password)
            server.send_message(m)
            server.quit()
            msg = f"Email sent to {to}."
        except Exception as e:
            msg = f"Failed to send email: {e}"
        ctx.speak(msg)
        return msg