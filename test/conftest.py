import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

import pytest


@pytest.fixture()
def init_driver(request):
    option = ChromeOptions()
    option.add_argument("--headless")
    driver = webdriver.Chrome(options=option)
    driver.get("https://formy-project.herokuapp.com")
    # driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    driver.maximize_window()
    time.sleep(2)
    print("setup method")
    request.cls.driver = driver

    yield
    driver.close()
    print("teardown")
