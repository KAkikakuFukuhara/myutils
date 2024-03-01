from __future__ import annotations
from typing import Any

from myutils import args_viewer


def test_show_kwargs():
    kwargs: dict[str, Any] = {}
    kwargs["img_dir"] = "/home/tmpusr"
    kwargs["count"] = 10

    args_viewer.show_kwargs(**kwargs)

