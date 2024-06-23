from src.pytemplate.domain.models import City, Dish, Restaurant
from src.pytemplate.service.restaurant import ItalianRestaurantService


def test_allocate_city():
    service = ItalianRestaurantService()
    city_data = {"name": "Rome", "country": "Italy", "population": 2873000}
    city = service.allocate_city(city_data)
    assert isinstance(city, City)
    assert city.name == "Rome"
    assert city.country == "Italy"
    assert city.population == 2873000


def test_make_dish():
    service = ItalianRestaurantService()
    dish_data = {"name": "Spaghetti Carbonara", "price": 15.5}
    dish = service.make_dish(dish_data)
    assert isinstance(dish, Dish)
    assert dish.name == "Spaghetti Carbonara"
    assert dish.price == 15.5


def test_make_restaurant():
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


def test_create():
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
