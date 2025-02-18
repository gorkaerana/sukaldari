# `sukaldari`

`sukaldari` is a recipe framework, and Python library designed for flexibility.

## Data model
Recipes are formed by structs `Recipe`, `Ingredient` and `Step`; which are described, respectively, in the below three tables.
- `Recipe` struct.

| Attribute name | Attribute type |
|---|---|
| name | string |
| ingredients | Array of `Ingredient` structs |
| steps | Array of `Step` structs |
- `Ingredient` struct.

| Attribute name | Attribute type |
|---|---|
| ingredient | string |
| amount | string or null |
| unit | string or null |
- `Step` struct.

| Attribute name | Attribute type |
|---|---|
| step | string |


Or in JSON Schema format:
```json
{
    "$ref": "#/$defs/Recipe",
    "$defs": {
        "Recipe": {
            "title": "Recipe",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "ingredients": {
                    "type": "array",
                    "items": {
                        "$ref": "#/$defs/Ingredient"
                    }
                },
                "steps": {
                    "type": "array",
                    "items": {
                        "$ref": "#/$defs/Step"
                    }
                }
            },
            "required": [
                "name",
                "ingredients",
                "steps"
            ]
        },
        "Ingredient": {
            "title": "Ingredient",
            "type": "object",
            "properties": {
                "ingredient": {
                    "type": "string"
                },
                "amount": {
                    "anyOf": [
                        {
                            "type": "string"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": null
                },
                "unit": {
                    "anyOf": [
                        {
                            "type": "string"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": null
                }
            },
            "required": [
                "ingredient"
            ]
        },
        "Step": {
            "title": "Step",
            "type": "object",
            "properties": {
                "step": {
                    "type": "string"
                }
            },
            "required": [
                "step"
            ]
        }
    }
}
```

## Use case
I've had my recipes scattered across many loose pieces of paper for years. As a Emacs and Org mode user, I figured the most convenient way to manage them would be a very simple `.org` file such as the below one. The follow-up question to such a set-up is, how does one share the recipes? And so the data model was born.

```org
* Chocolate sandwich
** Ingredients
- 2 slices of bread
- 8 squares of chocolate
** Steps
- Take one slice of bread, and place the squares of chocolate on top.
- Place the second slice of bread on top of the squares.
* Butter and cheese sandwich
** Ingredients
- 2 slices of bread
- Butter
- 2 slices of cheese
** Steps
- Take one slice of bread, butter it, and place a slice of cheese on top of it.
- Take the other slice of bread, butter it, and place the other slice of cheese on top of it.
- Join both halves.
```
