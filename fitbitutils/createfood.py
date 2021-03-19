import argparse

from fitbitutils.fitbitapi import FitbitApi
from fitbitutils.getfoodunit import FoodUnitGetter

class FoodCreator:

    def __init__(self):
        self._fitbit_api = FitbitApi()

    def create_food(self,
                    name: str,
                    calories: int,
                    total_fat: int = None,
                    saturated_fat: int = None,
                    cholesterol: int = None,
                    sodium: int = None,
                    potassium: int = None,
                    total_carbohydrate: int = None,
                    dietary_fiber: int = None,
                    sugars: int = None,
                    protein: int = None,
                    vitamin_d: int = None,
                    calcium: int = None,
                    iron: int = None,
                    ):
        params = {
            "name": name,
            "defaultFoodMeasurementUnitId": self._get_serving_food_unit_id(),
            "defaultServingSize": 1,
            "calories": calories,
            "totalFat": total_fat,
            "saturatedFat": saturated_fat,
            "cholesterol": cholesterol,
            "sodium": sodium,
            "potassium": potassium,
            "totalCarbohydrate": total_carbohydrate,
            "dietaryFiber": dietary_fiber,
            "sugars": sugars,
            "protein": protein,
            "vitaminD": vitamin_d,
            "calcium": calcium,
            "iron": iron,
        }

        valid_params = {key: value for key, value in params.items() if value is not None}

        url = f"/user/{self._fitbit_api.authenticator.user_id}/foods.json"

        response = self._fitbit_api.make_request("POST", url, params=valid_params)
        print(f"Food with name [{name}] created with id [{response['food']['foodId']}]")

    def _get_serving_food_unit_id(self) -> int:
        serving = FoodUnitGetter().get_with_name("serving")
        return serving["id"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="name of food to create")
    parser.add_argument("--calories", type=int, required=True, help="number of calories in 1 serving")
    parser.add_argument("--total-fat", type=int, help="amount of totalFat in 1 serving in g")
    parser.add_argument("--saturated-fat", type=int, help="amount of saturated fat in 1 serving in g")
    parser.add_argument("--cholesterol", type=int, help="amount of cholesterol in 1 serving in mg")
    parser.add_argument("--sodium", type=int, help="amount of sodium in 1 serving in mg")
    parser.add_argument("--potassium", type=int, help="amount of potassium in 1 serving in mg")
    parser.add_argument("--total-carbohydrate", type=int, help="amount of total carbohydrate in 1 serving in g")
    parser.add_argument("--dietary-fiber", type=int, help="amount of dietary fiber in 1 serving in g")
    parser.add_argument("--sugars", type=int, help="amount of sugars in 1 serving in g")
    parser.add_argument("--protein", type=int, help="amount of protein in 1 serving in g")
    parser.add_argument("--vitamin-d", type=int, help="amount of vitamin D in 1 serving in IU")
    parser.add_argument("--calcium", type=int, help="amount of calcium in 1 serving in g")
    parser.add_argument("--iron", type=int, help="amount of iron in 1 serving in mg")
    args = parser.parse_args()

    food_creator = FoodCreator()
    food_creator.create_food(
        name=args.name,
        calories=args.calories,
        total_fat=args.total_fat,
        saturated_fat=args.saturated_fat,
        cholesterol=args.cholesterol,
        sodium=args.sodium,
        potassium=args.potassium,
        total_carbohydrate=args.total_carbohydrate,
        dietary_fiber=args.dietary_fiber,
        sugars=args.sugars,
        protein=args.protein,
        vitamin_d=args.vitamin_d,
        calcium=args.calcium,
        iron=args.iron,
    )
