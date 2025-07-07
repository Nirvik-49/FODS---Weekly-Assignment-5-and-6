class Recipe:
    def __init__(self, recipe_id, name, ingredients, description):

        """Initialize a Recipe with all necessary attributes"""
        self.id = recipe_id
        self.name = name
        self.ingredients = ingredients
        self.description = description
    
    def display(self):
        
        """Display the recipe details in a formatted way"""
        print(f"\nRecipe ID: {self.id}")
        print(f"Name: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"Description: {self.description}")

class RecipeBook:
    def __init__(self):
        """Initialize an empty recipe book"""
        self.recipes = []
    
    def add_recipe(self, recipe):

        """Add a recipe to the recipe book"""
        self.recipes.append(recipe)
        print(f"\nRecipe '{recipe.name}' added successfully!")
    
    def display_all(self):

        """Display all recipes in the book"""
        if not self.recipes:
            print("\nThe recipe book is empty!")
            return
        
        print("\n===== RECIPE BOOK =====")
        for recipe in self.recipes:
            recipe.display()
            print("-" * 30)
    
    def find_by_id(self, recipe_id):

        """Find and display a recipe by its ID"""
        for recipe in self.recipes:
            if recipe.id == recipe_id:
                print("\nFound recipe:")
                recipe.display()
                return recipe
        print(f"\nNo recipe found with ID: {recipe_id}")
        return None

def get_recipe_input():

    """Helper function to get recipe details from user"""
    recipe_id = input("Enter recipe ID: ")
    name = input("Enter recipe name: ")
    
    print("Enter ingredients (press enter after each, blank to finish):")
    ingredients = []
    while True:
        ingredient = input("- ")
        if not ingredient.strip():
            break
        ingredients.append(ingredient)
    
    description = input("Enter recipe description: ")
    return Recipe(recipe_id, name, ingredients, description)

def menu():
    print("\nRECIPE BOOK MENU")
    print("1. Add a new recipe")
    print("2. View all recipes")
    print("3. Find recipe by ID")
    print("4. Exit")

if __name__ == "__main__":
    recipe_book = RecipeBook()
    
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            recipe = get_recipe_input()
            recipe_book.add_recipe(recipe)
        elif choice == "2":
            recipe_book.display_all()
        elif choice == "3":
            recipe_id = input("Enter recipe ID to search: ")
            recipe_book.find_by_id(recipe_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
