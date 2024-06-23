from src.pytemplate.domain.models import City


def test_city_creation():
    city = City(name="Paris", country="France", population=2148327)
    assert city.name == "Paris"
    assert city.country == "France"
    assert city.population == 2148327
