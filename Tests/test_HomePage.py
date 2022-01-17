import time

import allure

from Pages.HomePage import HomePage
from .test_base import BaseTest

class Test_Home(BaseTest):
    @allure.description("Validate OrangeHRM with valid credentials")
    @allure.severity(severity_level="CRITICAL")
    def test_home(self):
        self.homePage = HomePage(self.driver)

    @allure.description("Validate OrangeHRM with invalid credentials")
    @allure.severity(severity_level="NORMAL")
    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        self.homePage.home_page_title()
