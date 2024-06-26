from typing import Any

import pytest

from pytemplate.domain.models import City, Dish, Restaurant
from src.pytemplate.service.restaurant import ChineseRestaurantService, ItalianRestaurantService, RestaurantService


def test_italian_allocate_city():
    service = ItalianRestaurantService()
    city_data = {"name": "Rome", "country": "Italy", "population": 2873000}
    city = service.allocate_city(city_data)
    assert isinstance(city, City)
    assert city.name == "Rome"
    assert city.country == "Italy"
    assert city.population == 2873000


def test_italian_make_dish():
    service = ItalianRestaurantService()
    dish_data = {"name": "Spaghetti Carbonara", "price": 15.5}
    dish = service.make_dish(dish_data)
    assert isinstance(dish, Dish)
    assert dish.name == "Spaghetti Carbonara"
    assert dish.price == 15.5


def test_italian_make_restaurant():
    service = ItalianRestaurantService()
    city_data = {"name": "Rome", "country": "Italy", "population": 2873000}
    city = service.allocate_city(city_data)
    dish_data_1 = {"name": "Spaghetti Carbonara", "price": 15.5}
    dish_data_2 = {"name": "Margherita Pizza", "price": 12.0}
    dishes = [service.make_dish(dish_data_1), service.make_dish(dish_data_2)]
    restaurant = service.make_restaurant(city=city, dishes=dishes)
    assert isinstance(restaurant, Restaurant)
    assert restaurant.city == city
    assert len(restaurant.dishes) == 2
    assert restaurant.dishes[0].name == "Spaghetti Carbonara"
    assert restaurant.dishes[1].name == "Margherita Pizza"


def test_italian_create():
    service = ItalianRestaurantService()
    data = {
        "city": {"name": "Rome", "country": "Italy", "population": 2873000},
        "dishes": [{"name": "Spaghetti Carbonara", "price": 15.5}, {"name": "Margherita Pizza", "price": 12.0}],
    }
    restaurant = service.create(data)
    assert isinstance(restaurant, Restaurant)
    assert restaurant.city.name == "Rome"
    assert restaurant.city.country == "Italy"
    assert restaurant.city.population == 2873000
    assert len(restaurant.dishes) == 2
    assert restaurant.dishes[0].name == "Spaghetti Carbonara"
    assert restaurant.dishes[1].name == "Margherita Pizza"


def test_chinese_allocate_city():
    service = ChineseRestaurantService()
    city_data = {"name": "Beijing", "country": "China", "population": 21540000}
    city = service.allocate_city(city_data)
    assert isinstance(city, City)
    assert city.name == "Beijing"
    assert city.country == "China"
    assert city.population == 21540000


def test_chinese_make_dish():
    service = ChineseRestaurantService()
    dish_data = {"name": "Kung Pao Chicken", "price": 12.5}
    dish = service.make_dish(dish_data)
    assert isinstance(dish, Dish)
    assert dish.name == "Kung Pao Chicken"
    assert dish.price == 12.5


def test_chinese_make_restaurant():
    service = ChineseRestaurantService()
    city_data = {"name": "Beijing", "country": "China", "population": 21540000}
    city = service.allocate_city(city_data)
    dish_data_1 = {"name": "Kung Pao Chicken", "price": 12.5}
    dish_data_2 = {"name": "Sweet and Sour Pork", "price": 10.0}
    dishes = [service.make_dish(dish_data_1), service.make_dish(dish_data_2)]
    restaurant = service.make_restaurant(city=city, dishes=dishes)
    assert isinstance(restaurant, Restaurant)
    assert restaurant.city == city
    assert len(restaurant.dishes) == 2
    assert restaurant.dishes[0].name == "Kung Pao Chicken"
    assert restaurant.dishes[1].name == "Sweet and Sour Pork"


def test_chinese_create():
    service = ChineseRestaurantService()
    data = {
        "city": {"name": "Beijing", "country": "China", "population": 21540000},
        "dishes": [{"name": "Kung Pao Chicken", "price": 12.5}, {"name": "Sweet and Sour Pork", "price": 10.0}],
    }
    restaurant = service.create(data)
    assert isinstance(restaurant, Restaurant)
    assert restaurant.city.name == "Beijing"
    assert restaurant.city.country == "China"
    assert restaurant.city.population == 21540000
    assert len(restaurant.dishes) == 2
    assert restaurant.dishes[0].name == "Kung Pao Chicken"
    assert restaurant.dishes[1].name == "Sweet and Sour Pork"


def test_allocate_city_not_implemented():

    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            return super().allocate_city(data)

        def make_dish(self, data: dict[str, Any]) -> Dish:
            pass

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            pass

        def create(self, data: dict[str, Any]) -> Restaurant:
            pass

    service = ConcreteRestaurantService()

    with pytest.raises(NotImplementedError):
        service.allocate_city({"city_name": "TestCity"})


def test_make_dish_not_implemented():
    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            pass

        def make_dish(self, data: dict[str, Any]) -> Dish:
            return super().make_dish(data)

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            pass

        def create(self, data: dict[str, Any]) -> Restaurant:
            pass

    service = ConcreteRestaurantService()

    with pytest.raises(NotImplementedError):
        service.make_dish({"dish_name": "TestDish"})


def test_make_restaurant_not_implemented():

    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            pass

        def make_dish(self, data: dict[str, Any]) -> Dish:
            pass

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            return super().make_restaurant(city, dishes)

        def create(self, data: dict[str, Any]) -> Restaurant:
            pass

    service = ConcreteRestaurantService()
    city = City(name="Beijing", country="China", population=21540000)
    dishes = [Dish(name="Kung Pao Chicken", price=12.5), Dish(name="Sweet and Sour Pork", price=10.0)]
    with pytest.raises(NotImplementedError):
        service.make_restaurant(city, dishes)


def test_create_not_implemented():

    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            pass

        def make_dish(self, data: dict[str, Any]) -> Dish:
            pass

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            pass

        def create(self, data: dict[str, Any]) -> Restaurant:
            return super().create(data)

    service = ConcreteRestaurantService()
    with pytest.raises(NotImplementedError):
        service.create({"city_name": "TestCity", "num_dishes": 3})
