from dataclasses import dataclass


@dataclass
class City:
    name: str
    country: str
    population: int


def city_factory(name: str, country: str, population: int) -> City:
    return City(name=name, country=country, population=population)


@dataclass
class Dish:
    name: str
    price: float


def dish_factory(name: str, price: float) -> Dish:
    return Dish(name=name, price=price)
