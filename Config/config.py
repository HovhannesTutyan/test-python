from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestData:
    s = Service("C://Users//User//Desktop//chromedriver")
    CHROME_EXECUTABLE_PATH="C://Users//Admin//Desktop//chromedriver"
    BASE_URL = ("https://www.cincopa.com/")
    USER_NAME = "xxnkovyfdcvnkarvms@bvhrk.com"
    PASSWORD = "654127"
    LOGIN_PAGE_TITLE = "Login To Your Account | Cincopa"
    GALLERY_PREVIEW_TITLE = "New Gallery"
    GALLERY_PREVIEW_LOCATOR = (By.XPATH, "//*[@id=\"gallery_15520101\"]/td[1]/div[1]/div")
    GALLERIES_SEARCH_TEXT_BASE = "New Gallery"
    GALLERIES_SEARCH_TEXT_TEST = "New Gallery"
    CUSTOMIZE_GALLERY_TITLE = "Customize your skin"
    MANAGE_UPLOAD_FILES_TITLE = "Upload files | Files Uploader | Cincopa"
    EMBED_GALLERY_TITLE = "Embed your gallery"
    GALLERY_TAG_NAME = "TEST TAG NAME"
    GALLERY_TAG_NAME_TEST = "TEST TAG NAME!!!"

    EDIT_GALLERY_TITLE_TEXT1 = "TEST TITLE GALLERY 1"
    EDIT_GALLERY_TITLE_TEXT2 = "TEST TITLE GALLERY 2"

    ADD_GALLERY_FROM_ASSETS_NAME1 = "sample4.wma"
    ADD_GALLERY_FROM_ASSETS_NAME2 = "file_example_MOV_640_800kB (1).mov"

    ASSETS_NEW_ADDED_ASSET_TITLE = "New Added Asset"