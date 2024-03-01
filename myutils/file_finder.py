from __future__ import annotations
from pathlib import Path


def find_files_with_suffixes(dir_: Path, suffixes: list[str]) -> list[Path]:
    suffixes_: list[str] = []
    for sfx in suffixes:
        if not isinstance(sfx, str): continue
        if len(sfx) == 0: continue
        sfx_: str = sfx if sfx[0] == "." else f".{sfx}"
        suffixes_.append(sfx_)
    return [ p for sfx_ in suffixes_ for p in dir_.glob(f"*{sfx_}")]


def find_files(dir_: Path, words: list[str]) -> list[Path]:
    files: list[Path] = [ p for word in words for p in dir_.glob(word) if p.is_file()]
    return files


def find_dirs(dir_: Path, words: list[str]) -> list[Path]:
    dirs: list[Path] = [ p for word in words for p in dir_.glob(word) if p.is_dir()]
    return dirs
