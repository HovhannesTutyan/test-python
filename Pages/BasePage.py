from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,driver):
        self.driver=driver

    # def _find(self,by_locator):
    #     return self.driver.find_element(by_locator)

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_clear(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self,by_locator):
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self,by_locator):
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title

    # def do_get_text(self,by_locator):
    #     element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
    #     return element.get_attribute("value")

    def do_hover(self,by_locator):
        actions = ActionChains(self.driver)
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        actions.move_to_element(element).perform()