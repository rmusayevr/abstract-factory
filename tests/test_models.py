from src.pytemplate.domain.models import City, city_factory


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
