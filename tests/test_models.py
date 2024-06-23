from src.pytemplate.domain.models import City, city_factory, Dish, dish_factory


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
