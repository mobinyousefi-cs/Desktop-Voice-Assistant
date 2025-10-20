#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================
Project: Desktop Voice Assistant
File: gui.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi)
Created: 2025-10-20
Updated: 2025-10-20
License: MIT License (see LICENSE file for details)
===================================================================

Description:
Tkinter GUI with push-to-talk, transcript pane, and manual input.

Usage:
from voice_assistant.gui import run_gui; run_gui(app_context)

===================================================================
"""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Callable


class AssistantGUI:
    def __init__(self, title: str, on_listen: Callable[[], str], on_text: Callable[[str], str]):
        self.on_listen = on_listen
        self.on_text = on_text

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("840x560")

        self.text = tk.Text(self.root, wrap="word")
        self.text.configure(state=tk.NORMAL)
        self.text.insert(tk.END, "👋 Ready. Click ‘🎙️ Listen’ or type a command.\n")
        self.text.configure(state=tk.DISABLED)
        self.text.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        frame = ttk.Frame(self.root)
        frame.pack(fill=tk.X, padx=8, pady=4)

        self.entry = ttk.Entry(frame)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        btn_send = ttk.Button(frame, text="Send", command=self._send_text)
        btn_send.pack(side=tk.LEFT, padx=4)

        btn_listen = ttk.Button(frame, text="🎙️ Listen", command=self._listen)
        btn_listen.pack(side=tk.LEFT)

        self.root.bind("<Return>", lambda e: self._send_text())

    def log(self, who: str, message: str):
        self.text.configure(state=tk.NORMAL)
        self.text.insert(tk.END, f"{who}: {message}\n")
        self.text.see(tk.END)
        self.text.configure(state=tk.DISABLED)

    def _send_text(self):
        q = self.entry.get().strip()
        if not q:
            return
        self.entry.delete(0, tk.END)
        self.log("You", q)
        ans = self.on_text(q)
        self.log("Assistant", ans)

    def _listen(self):
        self.log("You", "(Listening…)")
        ans = self.on_listen()
        if ans:
            self.log("Heard", ans)
        else:
            self.log("Heard", "<no speech detected>")

    def run(self):
        self.root.mainloop()


def run_gui(title: str, on_listen: Callable[[], str], on_text: Callable[[str], str]):
    app = AssistantGUI(title, on_listen, on_text)
    app.run()