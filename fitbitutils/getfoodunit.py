from fitbitutils.fitbitgetter import FitbitGetter, main

class FoodUnitGetter(FitbitGetter):

    def __init__(self):
        super().__init__()
        self.url = "/foods/units.json"

if __name__ == "__main__":
    main(FoodUnitGetter())