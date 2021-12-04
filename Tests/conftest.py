import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.select import Select
from Config.config import TestData
@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    # if request.param=="chrome":
    # web_driver=webdriver.Chrome(service=TestData.s)
    # request.cls.driver=web_driver
    # yield
    web_driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    request.cls.driver = web_driver
    yield