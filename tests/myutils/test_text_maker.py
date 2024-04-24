from __future__ import annotations


from myutils import text_maker


def test_make_now_yyyymmdd_hhmmss():
    text: str = text_maker.make_yyyymmdd_hhmmss()
    print(text)
    text: str = text_maker.make_yyyymmdd_hhmmss(True)
    print(text)
    return
