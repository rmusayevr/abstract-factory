from unittest.mock import patch

from src.pytemplate.entrypoints.cli.main import get_city_input


def test_get_city_input():
    with patch("builtins.input", side_effect=["Paris", "France", "2140526"]):
        result = get_city_input()
        expected = {"name": "Paris", "country": "France", "population": 2140526}
        assert result == expected
