from src.pytemplate.domain.models import City, Dish, Restaurant
from src.pytemplate.service.restaurant import ChineseRestaurantService, ItalianRestaurantService


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
