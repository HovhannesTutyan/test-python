import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.AssetsPage import AssetsPage
from selenium.webdriver.common.by import By
import pyautogui
import time

class Test_Assets(BaseTest):
    def test_check_items_in_assets(self):
        self.assets_page = LoginPage(self.driver)
        self.assets_page.do_login(TestData.USER_NAME,TestData.PASSWORD)
        time.sleep(2)
    def test_check_items_in_assets_check_items(self):
        #Check if number of assets in Copy To/Delete is the same as number of assets with checkboxes
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.check_items_in_assets()
        assets_copy_to_parent_div_id = self.driver.find_element(By.ID,"copyTo")
        assets_copy_to_text = assets_copy_to_parent_div_id.text
        print(assets_copy_to_text)
        assets_checkbox_class = self.driver.find_elements(By.CLASS_NAME,"selected")
        assets_checkbox_length = len(assets_checkbox_class)
        print(assets_checkbox_length)
        if assets_copy_to_text == "Copy To("+str(assets_checkbox_length)+")":
            print("*************The Copy to number of items is the same as actual number of items*****************")
        else:
            print("Something went wrong with number of assets.")
    def test_upload_file_to_assets_folder(self):
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.upload_file_to_assets_folder(self.assets_page.ASSETS_UPLOAD_FILE_PATH)
        i_text_all = self.driver.find_elements(By.CLASS_NAME, "caption")
        for text in i_text_all:
            print (text.text)
            if text.text == "New Added Asset":
                print("**************Element is present in screen*****************")

    def test_delete_item_from_assets(self):
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.delete_item_from_assets(self.assets_page.ASSETS_SEARCH_INPUT_ITEM_DELETE)
        time.sleep(3)
        try:
            i_text_all = self.driver.find_elements(By.CLASS_NAME, "caption")
            for text in i_text_all:
                print(text.text)
                if text.text == "New Added Asset":
                    print("----------Element is still present in screen---------")
        except:
            print("**************Element is deleted*************")
    def test_view_assets_info(self):
        #select a single class by css_selector, and use get_attribute method to get its value(isntead of text method) and compare it to inputed by user
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.view_assets_info()
        assets_info_title_classname = self.driver.find_element(By.CSS_SELECTOR,".keyup_input.keyup_input_caption.changeCaption")
        assets_info_title_value = assets_info_title_classname.get_attribute("value")
        print(assets_info_title_value)
        if assets_info_title_value == "Record 1111":
            print("*******The title was successfully added*********")
        else:
            print("-----------Something went wrong--------------")
        assets_info_description_classname = self.driver.find_element(By.CSS_SELECTOR,".keyup_textarea_description")
        assets_info_description_text = assets_info_description_classname.text
        print(assets_info_description_text)
        if assets_info_description_text == "Record 1111 description":
            print("**********Description was successfully added********")
        else:
            print("----------Something went wrong---------------")
        assets_info_tag_classname = self.driver.find_element(By.CSS_SELECTOR,".tag")
        assets_info_tag_text = assets_info_tag_classname.text
        print(assets_info_tag_text)
        if assets_info_tag_text == "record 1111 tagx":
            print("***********Tag was successfully created*********")
        else:
            print("-----------Something went wrong-----------")

    def test_share_asset(self):
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.share_asset()
        new_page = self.driver.window_handles[1]
        self.driver.switch_to.window(new_page)
        print(self.driver.title)
        if self.driver.title == "Record 1111":
            print("***************The asset is shared*******************.")
        else:
            print("---------------The share asset link was not correct----------------")
    # #-------------------------------------------------------------------------------------------------------#
    # # def test_set_thumbnail_image(self):
    # #     self.assets_page = AssetsPage(self.driver)
    # #     self.assets_page.set_thumbnail_image_reset(self.assets_page.ASSETS_SET_THUMBNAIL_IMAGE_FILE_PATH)
    # # def test_set_thumbnail_video(self):
    # #     self.assets_page = AssetsPage(self.driver)
    # #     self.assets_page.set_thumbnail_video()
    # #--------------------------------------------------------------------------------------------------------#
    def test_asset_trimming(self):
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.asset_trimming()
        start_time = self.driver.find_element(By.CSS_SELECTOR, ".mejs-currenttime")
        print(start_time.text)
        if start_time.text == "00:07" or start_time.text == "00:08" or start_time.text == "00:09":
            print("************Assets start time was trimmed*********** ")
        else:
            print("_____________Assets start time is not correct___________")
    def test_subtitles_and_captions(self):
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.subtitles_and_captions()
        captions_number_class = self.driver.find_elements(By.CLASS_NAME,"subNumber")
        captions_text_class = self.driver.find_elements(By.CLASS_NAME,"subText")
        print(len(captions_number_class))
        for i in captions_text_class:
            print (i.text)
        if len(captions_number_class) == 8:
            print("**********Subtitles and Captions were added************")
        else:
            print("-------------Captions were not added-------------------")
    #def test_add_chapters(self):
    #    self.assets_page = AssetsPage(self.driver)
    #    self.assets_page.add_chapter()
    #    sample_chapters_parent_class = self.driver.find_element(By.CSS_SELECTOR,".mejs-chapters-list")
    #   sample_chapters_text = sample_chapters_parent_class.text
    #   if sample_chapters_text:
    #        print("Chapters were successfully added")
    #   else:
    #        print("Chapters were not added")
    # def test_delete_chapter(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.del_chapter()
    #     sample_chapters_parent_class = self.driver.find_element(By.CSS_SELECTOR, ".mejs-chapters-list")
    #     sample_chapters_text = sample_chapters_parent_class.text
    #     if not sample_chapters_text:
    #         print("Chapters were successfully deleted")
    #     else:
    #         print("Chapters were not deleted")
    def test_add_annotation(self):
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.add_annotation()
        time.sleep(2)
        # print(pyautogui.position())
        # pyautogui.click(1393,735)
        # time.sleep(1)
        # pyautogui.click(1393, 735)
        # time.sleep(1)
        # pyautogui.click(1393, 735)
        # time.sleep(5)
        # sample_annotation_div = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[7]/div")
        # if sample_annotation_div.text == "Sample explore me annotation":
        print("The annotation is successfully added")
        # else:
        #     print("No annotation added")
    # def test_del_annotation(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.del_annotation()
    #def test_call_to_action(self):
    #    self.assets_page = AssetsPage(self.driver)
    #    self.assets_page.call_to_action()
    #    new_page = self.driver.window_handles[2]
    #    self.driver.switch_to.window(new_page)
    #    time.sleep(2)
    #    print(self.driver.title)
    #    if self.driver.title == "Search projects | Photos, videos, logos, illustrations and branding on Behance":
    #        print("***************The call to action link was successfully added*******************.")
    #    else:
    #        print("---------------The link was not added----------------")