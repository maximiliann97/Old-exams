import os

# Part A
filename1 = 'exam 2021-08/recipes/chicken_salad.txt'
filename2 = 'exam 2021-08/calorie_data.txt'

def read_recipe(filename):
    recipe = dict()
    with open(filename, mode='r') as file:
        for line in file:
            if not (line.startswith('#')):
                ingredient, quantity = line.split('=')
                recipe[ingredient.strip().lower()] = float(quantity)
    return recipe

# Part B

def read_calorie_data(filename):
    calorie_dict = dict()
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) == 0: continue #Skip empty lines
            ingredient, calories = line.split(':')
            value = calories.rstrip('kJcal')
            unit = calories[len(value):].strip()
            scale = 1000 if 'k' in unit else 1
            if 'J' in unit:
                scale /= 4.184
            calorie_dict[ingredient.strip().lower()] = float(value) * scale

    return calorie_dict

# Part C
def count_calories(recipe, calorie_dict):
    c = 0
    for ingredient, quantity in recipe.items():
        c += calorie_dict[ingredient] * quantity
    return c

calorie_dict = read_calorie_data(filename2)
# Part D
for name in os.listdir('exam 2021-08/recipes/'):
    recipe = read_recipe(f'exam 2021-08/recipes/{name}')
    calories = count_calories(recipe, calorie_dict)
    print (f'{name} has {calories:.0f} calories')





