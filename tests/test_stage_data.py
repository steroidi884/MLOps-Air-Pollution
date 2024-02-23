#from air_quality import Person

import pytest

@pytest.fixture()
def person():
    return {"name": "test", "age":2}

def test_init(person):
    assert person["name"] == "test"
    assert person["age"] == 2

def test_forename(person):
    assert person["name"] == "lol"