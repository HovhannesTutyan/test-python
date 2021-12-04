from Pages.BasePage import BasePage
import time
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.franckmuller.com/')
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
    def home_page_title(self):
        get_title = self.driver.title
        print(get_title)
        assert get_title == "Franck Muller Official Website - Haute Horlogerie Watches"