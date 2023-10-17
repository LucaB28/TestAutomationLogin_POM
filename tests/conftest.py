# Constructor
import pytest
from selenium import webdriver

# parametrizacion para utilizar dos navegadores
"""
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    global driver
    browser = request.param
    print("creando driver")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
       driver = webdriver.Firefox()
    yield driver
    print("cerrando driver")
    driver.quit()
"""


# Funcion para utilizar un solo browser
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    yield driver
    driver.implicitly_wait(6)
    driver.quit()
