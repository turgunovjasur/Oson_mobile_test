import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserProfilePage(BasePage):
    # ------------------------------------------------------------------------------------------------------------------
    user_data_button = (By.XPATH, '(//android.widget.ImageView[@resource-id="com.oson:id/image_view"])[2]')

    def click_user_data(self):
        self.click(self.user_data_button)
    # ------------------------------------------------------------------------------------------------------------------
    user_name_input = (By.ID, "com.oson:id/user_name_text_view")

    def input_user_name(self, user_name):
        self.input_text(self.user_name_input, user_name)
    # ------------------------------------------------------------------------------------------------------------------
    nick_name_input = (By.ID, "com.oson:id/nick_name_text_view")

    def input_nick_name(self, nick_name):
        self.input_text(self.nick_name_input, nick_name)
    # ------------------------------------------------------------------------------------------------------------------
    phone_change_button = (By.ID, "com.oson:id/phone_change_text_view")

    def click_phone_change(self):
        self.click(self.phone_change_button)
    # ------------------------------------------------------------------------------------------------------------------
    def click_numeric_keypad(self):
        for digit in ["1", "1", "1", "1"]:
            locator = (By.ID, f"com.oson:id/widget_numerickeypadlayout_button_{digit}")
            time.sleep(0.2)
            self.click(locator)
    # ------------------------------------------------------------------------------------------------------------------
    change_number_button = (By.ID, "com.oson:id/change_number_button")
    phone_number_edit_button = (By.ID, "com.oson:id/phone_number_edit_text")

    def click_change_number(self, number):
        self.click(self.change_number_button)
        self.input_text(self.phone_number_edit_button, number)
    # ------------------------------------------------------------------------------------------------------------------
    error_massage = (By.ID, "com.oson:id/ok_text_view")

    def click_error_massage(self):
        self.click(self.error_massage)
    # ------------------------------------------------------------------------------------------------------------------
    change_button = (By.ID, "com.oson:id/action_button")

    def click_numer_change(self):
        self.click(self.change_button)
    # ------------------------------------------------------------------------------------------------------------------
    back_button = (By.ID, "com.oson:id/back_image_view")

    def click_back_page(self):
        self.click(self.back_button)
    # ------------------------------------------------------------------------------------------------------------------
    remove_user_button = (By.ID, "com.oson:id/remove_user_text_view")

    def click_remove_user(self):
        self.click(self.remove_user_button)
    # ------------------------------------------------------------------------------------------------------------------
    continue_button = (By.ID, "com.oson:id/continue_button")

    def click_continue(self):
        self.click(self.continue_button)
    # ------------------------------------------------------------------------------------------------------------------