import time
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
    def test_get_title(self):
        self.driver.get('https://www.franckmuller.com/')
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        get_title = self.driver.title
        print(get_title)
        assert get_title == "Franck Muller Official Website - Haute Horlogerie Watc"

    def  tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()