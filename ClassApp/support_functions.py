def get_recipe_options(user_ingredients, all_recipes, exempt_ingredients):
    recipe_list = list()
    suggested_list = list()
    for one_recipe in all_recipes:                              # one_recipe is each recipe
        ingredient_score = 0                                    # initialize ingredient score
        registered_ingredients = []                             # initialize list of registered ingredients
        for one_ingredient in one_recipe.ingredients:           # iterate through all ingredients in the recipe

            for user_ingredient in user_ingredients:
                parts = user_ingredient.split()                 # separate user ingredients into words
                real_ingredient = parts[len(parts) - 1]         # ingredient name is last part of user ingredient
                if real_ingredient in one_ingredient:           # if the user ingredient is a recipe ingredient
                    ingredient_score += 1                       # increment the ingredient score
                    registered_ingredients.append(real_ingredient)  # add the ingredient to registered ingredients list

        if ingredient_score == len(one_recipe.ingredients):     # if the ingredient score is the number of ingredients
            recipe_list.append(one_recipe)                      # add the recipe to the list of approved recipes

        elif ingredient_score < len(one_recipe.ingredients):

            # find which exempt ingredients are in the recipe
            # add the number of exempt ingredients to the recipe score
            if ingredient_score == len(one_recipe.ingredients):
                recipe_list.append(one_recipe)

    return (recipe_list, suggested_list)




"""from ClassApp.models import Currency

def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "https://thefactfile.org/countries-currencies-symbols/"
    response = requests.get(url)
    if not response.status_code == 200:
        return currency_list
    soup = BeautifulSoup(response.content)
    data_lines = soup.find_all('tr')
    for line in data_lines:
        try:
            detail = line.find_all('td')
            currency = detail[2].get_text().strip()
            iso = detail[3].get_text().strip()
            if (currency,iso) in currency_list:
                continue
            currency_list.append((currency,iso))
        except:
            continue
    return currency_list

def add_currencies(currency_list):
    for currency in currency_list:
        currency_name = currency[0]
        currency_symbol = currency[1]
        try:
            c = Currency.objects.get(iso=currency_symbol)
        except:
            c = Currency(long_name=currency_name, iso=currency_symbol)
            c.name = currency_name
            print(c) #c.save()  #To test out the code, replace this by print(c)
    return
