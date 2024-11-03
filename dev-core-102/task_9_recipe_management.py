recipe_ingredients = {
    "Pasta": ["Tomato", "Pasta", "Cheese"],
    "Salad": ["Lettuce", "Tomato", "Cucumber"]
}

ingredient_prices = {
    "Tomatoes": 500,
    "Cheese": 2000,
    "Spaghetti": 1500,
    "Cucumbers": 300,
    "Lettuce": 700
}

def print_list(list):
    print('Avilable recipes:')
    for recipe, ingredients in list.items():
        print(f"- {recipe}: {', ' .join(ingredients)}")

def print_ingredient_prices(ingredient_prices):
    print("Ingredient Prices:")
    for ingredient, price in ingredient_prices.items():
        print(f"- {ingredient}: {price} tenge")

def get_ingredient_price(ingredient, ingredient_prices):
    if ingredient in ingredient_prices:
        print(f"{ingredient} already exists with price: {ingredient_prices[ingredient]} units.")
        return ingredient_prices[ingredient]
    else:
        price = float(input(f"Enter the price for {ingredient}: "))
        ingredient_prices[ingredient] = price
        return price

def add_new_recipe(recipes, ingredient_prices):
    recipe_name = input("Enter the name of the new recipe: ")
    new_ingredients = []
    
    while True:
        ingredient = input("Enter an ingredient for the recipe (or type 'stop' to finish): ")
        if ingredient.lower() == 'stop':
            break
        
        price = get_ingredient_price(ingredient, ingredient_prices)
        new_ingredients.append(ingredient)
    
    recipes[recipe_name] = new_ingredients
    print(f"New recipe '{recipe_name}' added successfully!")

def calculate_food_cost(recipes, ingredient_prices):
    # Ask for the recipe name
    recipe_name = input("Enter the name of the recipe to calculate the cost: ")
    
    # Check if the recipe exists
    if recipe_name not in recipes:
        print(f"Recipe '{recipe_name}' not found.")
        return
    
    ingredients = recipes[recipe_name]
    
    total_cost = 0
    print(f"Ingredients for {recipe_name} and their costs:")
    
    # Print ingredients and calculate total cost
    for ingredient in ingredients:
        cost = ingredient_prices.get(ingredient, 0)
        total_cost += cost
        print(f"- {ingredient}: {cost} units")
    
    print(f"\nTotal cost before discount: {total_cost} units")
    
    # Apply discount if total cost exceeds 30,000
    if total_cost > 30000:
        discount = total_cost * 0.10
        final_price = total_cost - discount
        print(f"Discount applied: {discount} units")
        print(f"Final price after discount: {final_price} units")
    else:
        print(f"Final price: {total_cost} units")

print_list(recipe_ingredients)
print_ingredient_prices(ingredient_prices)
choice = int(input('Please select your choice: 1. add new recipe; 2. add new ingredient'))
if choice == 1:
    add_new_recipe(recipe_ingredients, ingredient_prices)
elif choice == 2:
    calculate_food_cost(recipe_ingredients, ingredient_prices)
else: 
    print('Try again')

