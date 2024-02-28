import allure
import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = (By.XPATH, "//input[@name='middleName']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@name='lastName']")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")
    SPINNER = (By.XPATH, "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_first_name):
        with allure.step(f"Change name on '{new_first_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + "A")
            first_name_field.send_keys(Keys.BACK_SPACE)
            # first_name_field.clear()
            # assert first_name_field.get_attribute("value") == "", "There is old first name"
            first_name_field.send_keys(new_first_name)
            self.new_name = new_first_name

    def change_middlename(self, new_middle_name):
        with allure.step(f"Change name on '{new_middle_name}'"):
            middle_name_field = self.wait.until(EC.element_to_be_clickable(self.MIDDLE_NAME_FIELD))
            middle_name_field.send_keys(Keys.CONTROL + "A")
            middle_name_field.send_keys(Keys.BACK_SPACE)
            # middle_name_field.clear()
            # assert middle_name_field.get_attribute("value") == "", "There is old middle name"
            middle_name_field.send_keys(new_middle_name)
            self.new_middlename = new_middle_name

    def change_lastname(self, new_last_name):
        with allure.step(f"Change name on '{new_last_name}'"):
            last_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD))
            last_name_field.send_keys(Keys.CONTROL + "A")
            last_name_field.send_keys(Keys.BACK_SPACE)
            # last_name_field.clear()
            # assert last_name_field.get_attribute("value") == "", "There is old last name"
            last_name_field.send_keys(new_last_name)
            self.new_lastname = new_last_name

    @allure.step("Click save button")
    def click_save_changes_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved successfully")
    def checking_saving_changes(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.new_name))
        self.wait.until(EC.text_to_be_present_in_element_value(self.MIDDLE_NAME_FIELD, self.new_middlename))
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_FIELD, self.new_lastname))
