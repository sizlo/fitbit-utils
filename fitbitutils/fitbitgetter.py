from fitbitutils.fitbitapi import FitbitApi

import argparse

class FitbitGetter:

    def __init__(self):
        self._fitbit_api = FitbitApi()
        self.url = None
        self.response_field = None

    def get_all(self) -> list:
        response = self._fitbit_api.make_request("GET", self.url)
        if self.response_field:
            return response[self.response_field]
        else:
            return response

    def get_with_name(self, name: str) -> dict:
        all_food = self.get_all()
        food_with_name = filter(lambda food: food["name"] == name, all_food)
        return list(food_with_name)[0]

def main(getter: FitbitGetter):
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="name of item to get")
    args = parser.parse_args()

    if args.name:
        print(getter.get_with_name(args.name))
    else:
        print(getter.get_all())
