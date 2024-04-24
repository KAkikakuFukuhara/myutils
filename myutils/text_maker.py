""" text作成に関するプログラムをまとめたファイル
"""
from __future__ import annotations
import datetime

def make_yyyymmdd_hhmmss(use_ms:bool=False) -> str:
    dt: datetime.datetime = datetime.datetime.now()
    # convert to yyyymmdd_hhmmss
    text: str = "{:4}{:02}{:02}_{:02}{:02}{:02}".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    if use_ms:
        text += f"_{dt.microsecond:06}"

    return text
