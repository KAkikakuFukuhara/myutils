from __future__ import annotations


def show_kwargs(*args, **kwargs):
    text: str = "\n"
    text += f"┌ kwargs ─────\n"
    for key, value in kwargs.items():
        text += f"│ - {key}\n"
        text += f"│    - {value}\n"
    text += f"└─────────\n"
    print(text)