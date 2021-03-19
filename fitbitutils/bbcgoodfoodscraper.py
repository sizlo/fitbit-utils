from fitbitutils.nutritionscraper import NutritionScraper, main


class BbcGoodFoodScraper(NutritionScraper):

    @classmethod
    def accepts(cls, url: str) -> bool:
        return "bbcgoodfood.com" in url

    def get_name(self) -> str:
        return self.html_soup.find("h1", {"class": "post-header__title"}).text

    def get_calories(self) -> str:
        return self.get_value_with_title("kcal")

    def get_total_fat(self) -> str:
        return self.get_value_with_title("fat")

    def get_saturated_fat(self) -> str:
        return self.get_value_with_title("saturates")

    def get_total_carbohydrate(self) -> str:
        return self.get_value_with_title("carbs")

    def get_sugars(self) -> str:
        return self.get_value_with_title("sugars")

    def get_dietary_fiber(self) -> str:
        return self.get_value_with_title("fibre")

    def get_protein(self) -> str:
        return self.get_value_with_title("protein")

    def get_sodium(self) -> str:
        return self.get_value_with_title("salt")

    def get_value_with_title(self, text) -> str:
        title_element = self.html_soup.find("td", {"class": "key-value-blocks__key"}, string=text)
        value_element = title_element.find_next_sibling("td", {"class": "key-value-blocks__value"})
        return value_element.text

if __name__ == "__main__":
    main(BbcGoodFoodScraper())
