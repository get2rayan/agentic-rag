import json

# Cook times for all 55 recipes (in minutes)
cook_times = {
    1: 65,   # Classic Margherita Pizza
    2: 60,   # Chicken Tikka Masala
    3: 25,   # Beef and Broccoli Stir-Fry
    4: 30,   # Vegetarian Buddha Bowl
    5: 20,   # Chocolate Chip Cookies
    6: 30,   # Pad Thai
    7: 15,   # Japanese Miso Soup
    8: 60,   # Tacos al Pastor
    9: 90,   # Greek Moussaka
    10: 60,  # Moroccan Chicken Tagine
    11: 45,  # Spanish Paella
    12: 30,  # French Onion Soup
    13: 35,  # Korean Bibimbap
    14: 45,  # Vietnamese Pho
    15: 45,  # Butter Chicken
    16: 15,  # Caesar Salad
    17: 30,  # Fish and Chips
    18: 25,  # Shakshuka
    19: 55,  # Lamb Gyros
    20: 10,  # Caprese Salad
    21: 30,  # Thai Green Curry
    22: 35,  # Enchiladas Rojas
    23: 20,  # Tom Yum Soup
    24: 20,  # Banana Pancakes
    25: 40,  # Sushi Rolls (Maki)
    26: 180, # Beef Bourguignon
    27: 10,  # Hummus
    28: 25,  # Chicken Fajitas
    29: 30,  # Ramen
    30: 45,  # Falafel Wrap
    31: 45,  # Chicken Adobo
    32: 20,  # Bruschetta
    33: 40,  # Chicken Katsu Curry
    34: 25,  # Pasta Carbonara
    35: 30,  # Chicken Shawarma
    36: 10,  # Guacamole
    37: 60,  # Shepherd's Pie
    38: 30,  # Tomato Basil Soup
    39: 30,  # Chicken Satay
    40: 60,  # Ratatouille
    41: 30,  # Ceviche
    42: 35,  # Palak Paneer
    43: 60,  # Lobster Bisque
    44: 15,  # Chicken Quesadillas
    45: 360, # Tiramisu (includes chilling time)
    46: 45,  # Jambalaya
    47: 60,  # Baklava
    48: 20,  # Coconut Shrimp
    49: 25,  # Vegetable Stir-Fry with Tofu
    50: 120, # New York Cheesecake (includes chilling)
    51: 90,  # Biryani
    52: 150, # Gazpacho (includes chilling)
    53: 20,  # Teriyaki Salmon
    54: 30,  # Chickpea Curry (Chana Masala)
    55: 50,  # Apple Crisp
}

with open('/Users/rayan/learning/git/agentic-rag/recipes_dataset.json', 'r') as f:
    data = json.load(f)

for recipe in data:
    recipe_id = recipe['id']
    if recipe_id in cook_times:
        # Find the index of "nutrition" key and insert cooktime before it
        # We'll rebuild the dict with cooktime inserted before nutrition
        new_recipe = {}
        for key, value in recipe.items():
            if key == 'nutrition':
                new_recipe['cooktime_minutes'] = cook_times[recipe_id]
            new_recipe[key] = value
        # Replace the recipe in the list
        idx = data.index(recipe)
        data[idx] = new_recipe

with open('/Users/rayan/learning/git/agentic-rag/recipes_dataset.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Cook times added to all recipes!")
