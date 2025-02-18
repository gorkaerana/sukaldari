from pathlib import Path


def to_typst(recipe):
    yield f"= {recipe.name}"
    yield "== Ingredients"
    for ingredient in recipe.ingredients:
        yield f"- {ingredient.ingredient}"
    yield "== Steps"
    for step in recipe.steps:
        yield f"- {step.step}"


def dump(recipe, file_path: str | Path):
    Path(file_path).write_text("\n".join(to_typst(recipe)))
