from fitbitutils.fitbitgetter import FitbitGetter, main

class FoodGetter(FitbitGetter):
    
    def __init__(self):
        super().__init__()
        self.url = f"/user/{self._fitbit_api.authenticator.user_id}/foods.json"
        self.response_field = "foods"

if __name__ == "__main__":
    main(FoodGetter())
