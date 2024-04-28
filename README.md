# open the Django shell and run

python manage.py shell

# import the FoodRecipe model

from recipes.models import FoodRecipe

# create a new recipe by instantiating the FoodRecipe model and saving it
recipe = FoodRecipe(name="Spaghetti Carbonara", ingredients="Spaghetti, bacon, eggs, Parmesan cheese, black pepper", instructions="1. Cook spaghetti according to package instructions. 2. In a separate pan, fry bacon until crispy. 3. Whisk eggs and Parmesan cheese in a bowl. 4. Once spaghetti is cooked, drain and add to the pan with bacon. 5. Quickly add egg mixture to the hot spaghetti and stir well. 6. Season with black pepper and serve immediately.")
recipe.save()

# migrate

python manage.py makemigrations 
python manage.py migrate
