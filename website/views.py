from flask import Blueprint, render_template
import requests

views = Blueprint('views', __name__)

@views.route('/')
def home():
	data = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php').json()
	name = data['drinks'][0]['strDrink']
	image = data['drinks'][0]['strDrinkThumb']
	ingredients = []
	measures = []
	instructions = data['drinks'][0]['strInstructions']
	for i in range(1, 16):
		ingredients.append(data['drinks'][0][f'strIngredient{i}'])
		measures.append(data['drinks'][0][f'strMeasure{i}'])
	return render_template("home.html", name=name, image=image, ingredients=ingredients, measures=measures, instructions=instructions)
