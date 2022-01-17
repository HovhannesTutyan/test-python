import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
class LoginPage(BasePage):
    EMAIL=(By.ID,"email")
    PASSWORD=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,"submitBtn")
    GO_TO_LOGIN=("Login")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT,"Login").click()
    def get_login_page_title(self,title):
        return self.get_title(title)
    def do_login(self,email,password):
        self.do_send_keys(self.EMAIL,email)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)