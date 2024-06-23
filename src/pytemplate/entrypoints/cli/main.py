from typing import Dict, List

from src.pytemplate.service.restaurant import ChineseRestaurantService, ItalianRestaurantService
from src.pytemplate.use_case.restaurant import restaurant


def get_city_input() -> Dict:
    name = input("Enter city name: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    return {"name": name, "country": country, "population": population}


def get_dish_input() -> List[Dict]:
    dishes = []
    while True:
        dish_name = input("Enter dish name: ")
        dish_price = float(input("Enter dish price: "))
        dishes.append({"name": dish_name, "price": dish_price})

        decide = input("Do you want to stop? (yes/no): ").strip().lower()
        if decide == "yes":
            break
    return dishes


def main() -> str:
    restaurant_registry = {
        "Italian": ItalianRestaurantService,
        "Chinese": ChineseRestaurantService,
    }

    cuisine = input("Enter the cuisine of the restaurant: (Italian, Chinese) ")
    city_data = get_city_input()
    dishes_data = get_dish_input()

    restaurant_data = {"cuisine": cuisine, "city": city_data, "dishes": dishes_data}

    try:
        restaurant(restaurant_data, restaurant_registry)
        return f"{cuisine} restaurant is created successfully!"
    except ValueError:
        return f"Failed to create {cuisine} restaurant."
