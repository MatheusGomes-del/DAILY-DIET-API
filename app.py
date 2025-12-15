from flask import Flask, jsonify, request
from database import db
import os
from dotenv import load_dotenv
from model.meal import Meal
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_DB')

db.init_app(app)

@app.route('/meal/register', methods=['POST'])
def register_meal():
    data = request.get_json()
    dt = datetime.strptime(data["datetime"], "%d-%m-%Y %H:%M:%S")

    print(data)
    meal = Meal( name=data["name"],
                 description=data["description"],
                 datetime=dt,
                 is_on_diet=data["is_on_diet"],
                 user_id=data["user_id"])
    
    if meal:
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição adicionada com sucesso"})
    
    return jsonify({"message": "Refeição invalida"}), 400


@app.route('/meal/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):

    data = request.get_json()

    meal = Meal.query.get(meal_id)
    print(meal)

    if meal:
        meal.name = data["name"]
        meal.description = data["description"]
        meal.datetime = data["datetime"]
        meal.is_on_diet = data["is_on_diet"]

        return jsonify({"message": "Refeição atualizada com sucesso"})
    
    return jsonify({"message": "Id de Refeição invalido"}), 404

@app.route('/meal/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):

    meal = Meal.query.get(meal_id)
    print(meal)

    if meal:
       db.Query.delete(meal)
       db.session.commit()
       return jsonify({"message": "Refeição deletada com sucesso"})
    
    return jsonify({"message": "Id de Refeição invalido"}), 404


@app.route('/meal/meals/<int:user_id>', methods=['GET'])
def get_all_meals(user_id):

    meals = Meal.query.filter_by(user_id=user_id).all()

    if not meals:
        return jsonify({"message": "Nenhuma refeição encontrada para esse usuário"}), 404

    return jsonify({"meals": [meal.to_dict() for meal in meals]})


@app.route('/meal/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):

    meal = Meal.query.filter_by(meal_id=meal_id).all()

    if not meal:
        return jsonify({"message": "Nenhuma refeição encontrada!"}), 404

    return jsonify({"meals": f"{[meal.to_dict() for meal in meal]}"})


if __name__ == '__main__':
    app.run(debug=True)
