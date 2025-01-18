import pytest
from selenium import webdriver

import urls


@pytest.fixture(scope = "function")
def get_driver_function(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.get(urls.main_page)
    yield
    driver.quit()

@pytest.fixture(scope = "class")
def get_driver_class(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.get(urls.main_page)
    yield
    driver.quit()