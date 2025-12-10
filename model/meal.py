from database import db

class Meal(db.Model):
    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=False)
    description = db.Column(db.String(255), nullable=False, unique=False)
    datetime = db.Column(db.DateTime(), nullable=False, unique=False)
    is_on_diet = db.Column(db.Boolean, nullable=False, unique=False)
    user_id = db.Column(db.Integer, nullable=False, primary_key=False)
    

    def to_dict(self):
        return {
            "meal_id": self.meal_id,
            "name": self.name,
            "description": self.description,
            "datetime": self.datetime,
            "is_on_diet": self.is_on_diet,
            "user_id": self.user_id
        }

