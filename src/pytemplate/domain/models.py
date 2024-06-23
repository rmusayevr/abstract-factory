from dataclasses import dataclass
from typing import List
from uuid import UUID, uuid4


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


@dataclass
class Restaurant:
    uuid: UUID
    city: City
    dishes: List[Dish]


def restaurant_factory(city: City, dishes: List[Dish]) -> Restaurant:
    return Restaurant(uuid=uuid4(), dishes=dishes, city=city)
