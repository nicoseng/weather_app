from flask import request
from flask import Flask
from flask import render_template
from data_extractor import DataExtractor

# Pour créer notre app, on crée une instance de la classe Flask
app = Flask(__name__)

# C'est le chemin URL
@app.route("/")
# Méthode invoquée quand on se rend sur la route "/" définie juste au dessus 
def index():
    return render_template('index.html')

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        city_name = request.form["city_name"]
        print(city_name)
        if city_name:
            data_extractor = DataExtractor()
            city_data = data_extractor.get_ow_data(city_name)
            return render_template('index.html', city_data=city_data)
        # Si le formulaire est vide
        elif request.form["city_name"] == "":
            empty_message = "Vous n'avez pas entré un nom de lieu"
            return render_template('index.html', empty_message=empty_message)
        else:
            unknown_message = "Nom inconnu"
            return render_template('index.html', unknown_message=unknown_message)