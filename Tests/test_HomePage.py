import time
from Pages.HomePage import HomePage
from .test_base import BaseTest

class Test_Home(BaseTest):
    def test_home(self):
        self.homePage = HomePage(self.driver)
    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        self.homePage.home_page_title()
