import allure
import random
import pytest
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Name {random.randint(1, 100)}")
        self.personal_page.change_middlename(f"Middlename {random.randint(1, 100)}")
        self.personal_page.change_lastname(f"Lastname {random.randint(1, 100)}")
        self.personal_page.click_save_changes_button()
        self.personal_page.checking_saving_changes()
        self.personal_page.make_screenshot("Success")
