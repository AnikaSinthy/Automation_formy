import time
import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("https://formy-project.herokuapp.com")
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        self.driver.maximize_window()
        time.sleep(2)
        print("setup method")

    def tearDown(self):
        self.driver.close()
        print("teardown")
