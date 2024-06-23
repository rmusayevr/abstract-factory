from typing import Dict


def get_city_input() -> Dict:
    name = input("Enter city name: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    return {"name": name, "country": country, "population": population}
