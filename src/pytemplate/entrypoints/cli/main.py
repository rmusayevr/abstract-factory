from typing import Dict, List


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
