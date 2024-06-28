from dataclasses import dataclass
from uuid import UUID, uuid4
from abc import ABC, abstractmethod
from typing import Any


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
    dishes: list[Dish]


def restaurant_factory(city: City, dishes: list[Dish]) -> Restaurant:
    return Restaurant(uuid=uuid4(), dishes=dishes, city=city)


class RestaurantService(ABC):

    @abstractmethod
    def allocate_city(self, data: dict[str, Any]) -> City:
        raise NotImplementedError(
            "This method should be overridden by subclasses")

    @abstractmethod
    def make_dish(self, data: dict[str, Any]) -> Dish:
        raise NotImplementedError(
            "This method should be overridden by subclasses")

    @abstractmethod
    def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
        raise NotImplementedError(
            "This method should be overridden by subclasses")

    @abstractmethod
    def create(self, data: dict[str, Any]) -> Restaurant:
        raise NotImplementedError(
            "This method should be overridden by subclasses")


class ItalianRestaurantService(RestaurantService):
    def allocate_city(self, data: dict[str, Any]) -> City:
        return city_factory(name=data["name"], country=data["country"], population=data["population"])

    def make_dish(self, data: dict[str, Any]) -> Dish:
        return dish_factory(name=data["name"], price=data["price"])

    def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
        return restaurant_factory(city=city, dishes=dishes)

    def create(self, data: dict[str, Any]) -> Restaurant:
        city_data = data["city"]
        dish_data_list = data["dishes"]
        city = self.allocate_city(city_data)
        dishes = [self.make_dish(dish_data) for dish_data in dish_data_list]
        return self.make_restaurant(city=city, dishes=dishes)


class ChineseRestaurantService(RestaurantService):
    def allocate_city(self, data: dict[str, Any]) -> City:
        return city_factory(name=data["name"], country=data["country"], population=data["population"])

    def make_dish(self, data: dict[str, Any]) -> Dish:
        return dish_factory(name=data["name"], price=data["price"])

    def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
        return restaurant_factory(city=city, dishes=dishes)

    def create(self, data: dict[str, Any]) -> Restaurant:
        city_data = data["city"]
        dish_data_list = data["dishes"]
        city = self.allocate_city(city_data)
        dishes = [self.make_dish(dish_data) for dish_data in dish_data_list]
        return self.make_restaurant(city=city, dishes=dishes)


def restaurant(data: dict[str, Any], registry: dict[str, type[RestaurantService]]) -> Restaurant:
    cuisine = data["cuisine"]
    service_class = registry.get(cuisine)
    if service_class is None:
        raise ValueError(f"No service found for cuisine: {cuisine}")
    service_instance = service_class()
    return service_instance.create(data)


restaurant_registry = {
    "Italian": ItalianRestaurantService,
    "Chinese": ChineseRestaurantService,
}

cuisine = input("Enter the cuisine of the restaurant: (Italian, Chinese) ")
city_data = {"name": "Paris", "country": "France", "population": 2140526}
dishes_data = [{"name": "Spaghetti Carbonara", "price": 15.5}, {"name": "Margherita Pizza", "price": 12.0}]

restaurant_data = {"cuisine": cuisine,
                   "city": city_data, "dishes": dishes_data}

try:
    restaurant(restaurant_data, restaurant_registry)
    print(f"{cuisine} restaurant is created successfully!")
except ValueError:
    print(f"Failed to create {cuisine} restaurant.")
