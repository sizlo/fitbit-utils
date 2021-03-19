from fitbitutils.bbcgoodfoodscraper import BbcGoodFoodScraper
from fitbitutils.nutritionscraper import NutritionScraper, ScrapeResult
from fitbitutils.nutritionunitconverter import convert_to_desired_units
from fitbitutils.createfood import FoodCreator

import argparse
import sys

class Scraper:
    def __init__(self, url):
        self.url = url
        self.food_creator = FoodCreator()

    def scrape(self):
        scrape_result = self.do_scrape()
        name = scrape_result.name
        nutrition_info = convert_to_desired_units(scrape_result.nutrition_info)
        self.food_creator.create_food(
            name=name,
            calories=nutrition_info["calories"],
            total_fat=nutrition_info["total_fat"],
            saturated_fat=nutrition_info["saturated_fat"],
            cholesterol=nutrition_info["cholesterol"],
            sodium=nutrition_info["sodium"],
            potassium=nutrition_info["potassium"],
            total_carbohydrate=nutrition_info["total_carbohydrate"],
            dietary_fiber=nutrition_info["dietary_fiber"],
            sugars=nutrition_info["sugars"],
            protein=nutrition_info["protein"],
            vitamin_d=nutrition_info["vitamin_d"],
            calcium=nutrition_info["calcium"],
            iron=nutrition_info["iron"],
        )

    def do_scrape(self) -> ScrapeResult:
        nutrition_scraper = self.get_nutrition_scraper()
        if nutrition_scraper is None:
            print(f"No scrapers available for {self.url}")
            sys.exit(1)

        return nutrition_scraper.scrape(self.url)

    def get_nutrition_scraper(self) -> NutritionScraper:
        possible_scrapers = [
            BbcGoodFoodScraper()
        ]

        for scraper in possible_scrapers:
            if scraper.__class__.accepts(self.url):
                return scraper

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to scrape")
    args = parser.parse_args()

    Scraper(args.url).scrape()
