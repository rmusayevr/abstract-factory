from unittest.mock import patch

from src.pytemplate.entrypoints.cli.main import get_city_input, get_dish_input, main


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


@patch("builtins.input", side_effect=["Italian", "Rome", "Italy", "2873000", "Spaghetti Carbonara", "15.5", "yes"])
def test_main_success(mock_input):
    expected_output = "Italian restaurant is created successfully!"
    assert main() == expected_output


@patch(
    "builtins.input",
    side_effect=["Chinese", "Pekin", "China", "9045000", "Kung Pao Chicken", "25.5", "no", "Sweet and Sour Pork", "12.99", "yes"],
)
def test_main_success(mock_input):
    expected_output = "Chinese restaurant is created successfully!"
    assert main() == expected_output


@patch("builtins.input", side_effect=["French", "Pekin", "China", "9045000", "Kung Pao Chicken", "25.5", "yes"])
def test_main_invalid_cuisine(mock_input):
    expected_output = "Failed to create French restaurant."
    assert main() == expected_output
