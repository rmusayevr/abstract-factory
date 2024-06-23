from uuid import UUID, uuid4

from src.pytemplate.domain.models import City, city_factory, Dish, dish_factory, Restaurant


def test_city_creation():
    city = City(name="Paris", country="France", population=2148327)
    assert city.name == "Paris"
    assert city.country == "France"
    assert city.population == 2148327


def test_city_factory():
    city = city_factory(name="Tokyo", country="Japan", population=13929286)
    assert isinstance(city, City)
    assert city.name == "Tokyo"
    assert city.country == "Japan"
    assert city.population == 13929286


def test_dish_creation():
    dish = Dish(name="Pasta", price=12.99)
    assert dish.name == "Pasta"
    assert dish.price == 12.99


def test_dish_factory():
    dish = dish_factory(name="Pasta", price=12.99)
    assert isinstance(dish, Dish)
    assert dish.name == "Pasta"
    assert dish.price == 12.99


def test_restaurant_creation():
    city = city_factory(name="New York", country="USA", population=8398748)
    dish1 = dish_factory(name="Pasta", price=12.99)
    dish2 = dish_factory(name="Salad", price=8.99)
    dishes = [dish1, dish2]
    uuid = uuid4()
    restaurant = Restaurant(uuid=uuid, dishes=dishes, city=city)
    assert restaurant.uuid == uuid
    assert restaurant.city == city
    assert restaurant.dishes == dishes
    assert isinstance(restaurant.uuid, UUID)
    assert isinstance(restaurant.city, City)
    assert isinstance(restaurant.dishes, list)
    assert all(isinstance(dish, Dish) for dish in restaurant.dishes)
