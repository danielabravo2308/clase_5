import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def five():
    print("Aqui comienza el fixture 5")
    number=5
    yield number 
    number = 0
    print("Aqui termina el fixture 5")

@pytest.fixture
def two():
    return 5


@pytest.fixture
def array():
    print("Aqui comienza el fixture array")
    arr = [1,2,3,4]
    yield arr
    arra = []
    print("Aqui termina el fixture array")


@pytest.fixture
def multi_2():
    print("Aqui comienza el fixture multi 2")
    number=2
    yield number 
    number = 0
    print("Aqui termina el fixture multi 2")



    