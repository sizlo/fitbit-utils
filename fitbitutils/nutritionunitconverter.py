import re

DESIRED_UNITS = {
    "total_fat": "g",
    "saturated_fat": "g",
    "cholesterol": "mg",
    "sodium": "mg",
    "potassium": "mg",
    "total_carbohydrate": "g",
    "dietary_fiber": "g",
    "sugars": "g",
    "protein": "g",
    "vitamin_d": "iu",
    "calcium": "g",
    "iron": "mg",
}

CONVERSION_FACTORS = {
    "mg": {
        "mg": 1.0,
        "g": 1.0/1000.0,
    },
    "g": {
        "mg": 1000.0,
        "g": 1.0,
    },
    "iu": {
        "iu": 1.0,
    },
}

def convert_to_desired_units(nutrition_info: dict) -> dict:
    return {
        "calories": int(nutrition_info["calories"]),
        "total_fat": convert_to_desired_unit(nutrition_info, "total_fat"),
        "saturated_fat": convert_to_desired_unit(nutrition_info, "saturated_fat"),
        "cholesterol": convert_to_desired_unit(nutrition_info, "cholesterol"),
        "sodium": convert_to_desired_unit(nutrition_info, "sodium"),
        "potassium": convert_to_desired_unit(nutrition_info, "potassium"),
        "total_carbohydrate": convert_to_desired_unit(nutrition_info, "total_carbohydrate"),
        "dietary_fiber": convert_to_desired_unit(nutrition_info, "dietary_fiber"),
        "sugars": convert_to_desired_unit(nutrition_info, "sugars"),
        "protein": convert_to_desired_unit(nutrition_info, "protein"),
        "vitamin_d": convert_to_desired_unit(nutrition_info, "vitamin_d"),
        "calcium": convert_to_desired_unit(nutrition_info, "calcium"),
        "iron": convert_to_desired_unit(nutrition_info, "iron"),
    }


def convert_to_desired_unit(nutrition_info, field) -> float:
    if nutrition_info[field] is None:
        return None

    value_and_unit = nutrition_info[field].lower()
    value, from_unit = extract_value_and_unit(value_and_unit)
    to_unit = DESIRED_UNITS[field]
    conversion_factor = get_conversion_factor(from_unit, to_unit)
    return value * conversion_factor

def extract_value_and_unit(value_and_unit):
    matches = re.search(r"((\d*\.)?\d+)([a-z]+)", value_and_unit)
    if matches is None:
        raise RuntimeError(f"Could not extract value and unit from {value_and_unit}")

    value = float(matches.group(1))
    unit = matches.group(3)
    return value, unit

def get_conversion_factor(from_unit, to_unit):
    try:
        return CONVERSION_FACTORS[from_unit][to_unit]
    except KeyError:
        raise RuntimeError(f"Could not find conversion factor from {from_unit} to {to_unit}")
