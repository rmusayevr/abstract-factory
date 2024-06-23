from typing import Any, Dict


def get_city_input() -> Dict[str, Any]:
    name = input("Enter city name: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    return {"name": name, "country": country, "population": population}
