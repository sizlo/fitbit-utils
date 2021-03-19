from abc import abstractmethod

from bs4 import BeautifulSoup

import requests
import argparse

class ScrapeResult:
    def __init__(self, name: str, nutrition_info: dict):
        self.name = name
        self.nutrition_info = nutrition_info

    def __str__(self):
        result = f"Name: {self.name}\n"
        for key, value in self.nutrition_info.items():
            if value is not None:
                result += f"{key}: {value}\n"
        return result

class NutritionScraper:

    @classmethod
    @abstractmethod
    def accepts(cls, url: str) -> bool:
        pass

    def scrape(self, url) -> ScrapeResult:
        html = requests.get(url).text
        self.html_soup = BeautifulSoup(html, "html.parser")

        name = self.get_name()

        nutrition_info = {
            "calories": self.get_calories(),
            "total_fat": self.get_total_fat(),
            "saturated_fat": self.get_saturated_fat(),
            "cholesterol": self.get_cholesterol(),
            "sodium": self.get_sodium(),
            "potassium": self.get_potassium(),
            "total_carbohydrate": self.get_total_carbohydrate(),
            "dietary_fiber": self.get_dietary_fiber(),
            "sugars": self.get_sugars(),
            "protein": self.get_protein(),
            "vitamin_d": self.get_vitamin_d(),
            "calcium": self.get_calcium(),
            "iron": self.get_iron(),
        }

        return ScrapeResult(name, nutrition_info)

    def get_name(self) -> str:
        pass

    def get_calories(self) -> str:
        pass

    def get_total_fat(self) -> str:
        pass

    def get_saturated_fat(self) -> str:
        pass

    def get_cholesterol(self) -> str:
        pass

    def get_sodium(self) -> str:
        pass

    def get_potassium(self) -> str:
        pass

    def get_total_carbohydrate(self) -> str:
        pass

    def get_dietary_fiber(self) -> str:
        pass

    def get_sugars(self) -> str:
        pass

    def get_protein(self) -> str:
        pass

    def get_vitamin_d(self) -> str:
        pass

    def get_calcium(self) -> str:
        pass

    def get_iron(self) -> str:
        pass

def main(scraper: NutritionScraper):
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to scrape")
    args = parser.parse_args()

    scrape_result = scraper.scrape(args.url)
    print(scrape_result)
