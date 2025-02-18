from __future__ import annotations
from pathlib import Path

import msgspec


class Ingredient(msgspec.Struct):
    ingredient: str
    amount: str | None = None
    unit: str | None = None  # TODO: maybe `Literal`?


class Step(msgspec.Struct):
    step: str


class Recipe(msgspec.Struct):
    name: str
    ingredients: list[Ingredient]
    steps: list[Step]

    # TODO: `format: Literal`
    # TODO: the `list[Recipe]` return type annotation is an anti-pattern
    @classmethod
    def load(self, file_path: str | Path, format: str | None = None) -> list[Recipe]:
        file_path = Path(file_path)
        if format is None:
            format = file_path.suffix.lstrip(".")
        loader = __import__(
            f"sukaldari.loaders.{format}", globals(), locals(), ["load"], 0
        ).load
        return msgspec.convert(loader(file_path), type=list[Recipe])

    # TODO: `format: Literal`
    def dump(self, file_path: str | Path, format: str | None = None):
        file_path = Path(file_path)
        if format is None:
            format = file_path.suffix.lstrip(".")
        dumper = __import__(
            f"sukaldari.dumpers.{format}", globals(), locals(), ["dump"], 0
        ).dump
        dumper(self, file_path)
