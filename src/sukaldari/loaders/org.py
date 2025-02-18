from pathlib import Path
from typing import Any, Callable

ORG_LIST_BULLET_CHAR = "-+1234567890.)"


class BufferableOpen:
    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)
        self.buffer: list = []

    def __enter__(self):
        self.fp = self.file_path.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fp.close()

    def __next__(self):
        if self.buffer:
            return self.buffer.pop(0)
        else:
            return next(self.fp)

    def takeuntil(self, predicate: Callable[[Any], bool]):
        """An alternative to `itertools.takewhile` that returns the one matching element"""
        gathered = []
        next_element = next(self)
        collect = True
        while not predicate(next_element):
            gathered.append(next_element)
            try:
                next_element = next(self)
            except StopIteration:
                collect = False
                break
        if collect:
            self.buffer.append(next_element)
        return gathered


# TODO: How to type this to avoid circular dependencies?
def load(file_path: str | Path) -> list[dict]:
    recipes: list[dict] = []
    with BufferableOpen(file_path) as fp:
        while True:
            try:
                line = next(fp)
            except StopIteration:
                break
            if line.startswith("* "):
                next(fp)  # Skip ingredients header
                ingredients = fp.takeuntil(lambda line: line.startswith("** "))
                next(fp)  # Skip steps header
                steps = fp.takeuntil(lambda line: line.startswith("* "))
                recipe = {
                    "name": line.strip("*").strip(),
                    "ingredients": [
                        {"ingredient": s.strip(ORG_LIST_BULLET_CHAR).strip()}
                        for s in ingredients
                    ],
                    "steps": [
                        {"step": s.strip(ORG_LIST_BULLET_CHAR).strip()} for s in steps
                    ],
                }
                recipes.append(recipe)
    return recipes
