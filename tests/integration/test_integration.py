from sukaldari import Recipe


recipes = Recipe.load("./main.org", format="org")
recipes[0].dump("main.typst", "typst")
# If format is not provided, it is fetched from the file extension
recipes = Recipe.load("./main.org")
recipes[0].dump("main.typst")
