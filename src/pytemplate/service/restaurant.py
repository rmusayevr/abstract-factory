from abc import ABC, abstractmethod
from typing import Any

from pytemplate.domain.models import City, city_factory, Dish, dish_factory, Restaurant, restaurant_factory


class RestaurantService(ABC):

    @abstractmethod
    def allocate_city(self, data: dict[str, Any]) -> City:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def make_dish(self, data: dict[str, Any]) -> Dish:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def create(self, data: dict[str, Any]) -> Restaurant:
        raise NotImplementedError("This method should be overridden by subclasses")


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
