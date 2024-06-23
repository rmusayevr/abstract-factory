from unittest.mock import patch

from src.pytemplate.entrypoints.cli.main import get_city_input, get_dish_input


def test_get_city_input():
    with patch("builtins.input", side_effect=["Paris", "France", "2140526"]):
        result = get_city_input()
        expected = {"name": "Paris", "country": "France", "population": 2140526}
        assert result == expected


def test_get_dish_input():
    with patch("builtins.input", side_effect=["Spaghetti Carbonara", "15.5", "no", "Margherita Pizza", "12.0", "yes"]):
        result = get_dish_input()
        expected = [{"name": "Spaghetti Carbonara", "price": 15.5}, {"name": "Margherita Pizza", "price": 12.0}]
        assert result == expected
