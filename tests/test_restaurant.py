import pytest

from src.pytemplate.domain.models import Restaurant
from src.pytemplate.service.restaurant import ChineseRestaurantService, ItalianRestaurantService
from src.pytemplate.use_case.restaurant import restaurant


def test_restaurant_italian():
    data = {
        "cuisine": "Italian",
        "city": {"name": "Rome", "country": "Italy", "population": 2873000},
        "dishes": [{"name": "Spaghetti Carbonara", "price": 15.5}, {"name": "Margherita Pizza", "price": 12.0}],
    }
    registry = {"Italian": ItalianRestaurantService, "Chinese": ChineseRestaurantService}
    rest = restaurant(data, registry)
    assert isinstance(rest, Restaurant)
    assert rest.city.name == "Rome"
    assert rest.city.country == "Italy"
    assert rest.city.population == 2873000
    assert len(rest.dishes) == 2
    assert rest.dishes[0].name == "Spaghetti Carbonara"
    assert rest.dishes[1].name == "Margherita Pizza"


def test_restaurant_chinese():
    data = {
        "cuisine": "Chinese",
        "city": {"name": "Beijing", "country": "China", "population": 21540000},
        "dishes": [{"name": "Kung Pao Chicken", "price": 12.5}, {"name": "Sweet and Sour Pork", "price": 10.0}],
    }
    registry = {"Italian": ItalianRestaurantService, "Chinese": ChineseRestaurantService}
    rest = restaurant(data, registry)
    assert isinstance(rest, Restaurant)
    assert rest.city.name == "Beijing"
    assert rest.city.country == "China"
    assert rest.city.population == 21540000
    assert len(rest.dishes) == 2
    assert rest.dishes[0].name == "Kung Pao Chicken"
    assert rest.dishes[1].name == "Sweet and Sour Pork"


def test_restaurant_invalid_cuisine():
    data = {
        "cuisine": "French",
        "city": {"name": "Paris", "country": "France", "population": 2148000},
        "dishes": [{"name": "Croissant", "price": 3.0}, {"name": "Baguette", "price": 2.0}],
    }
    registry = {"Italian": ItalianRestaurantService, "Chinese": ChineseRestaurantService}
    with pytest.raises(ValueError, match="No service found for cuisine: French"):
        restaurant(data, registry)
