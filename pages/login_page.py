from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # ------------------------------------------------------------------------------------------------------------------
    uzb_lang = (By.ID, "com.oson:id/uz_linear_layout")

    def click_uzbek_language(self):
        self.click(self.uzb_lang)
    # ------------------------------------------------------------------------------------------------------------------
    action_button = (By.ID, "com.oson:id/action_button")

    def click_action(self):
        self.click(self.action_button)
    # ------------------------------------------------------------------------------------------------------------------
    choose_country = (By.ID, "com.oson:id/choose_country_edit_text")

    def click_choose_country(self):
        self.click(self.choose_country)
    # ------------------------------------------------------------------------------------------------------------------
    search_country_input = (By.ID, "com.oson:id/search_edit_text")

    def input_search_country(self, country_cod):
        self.input_text(self.search_country_input, country_cod)
    # ------------------------------------------------------------------------------------------------------------------
    country_button = (By.ID, "com.oson:id/text_view")

    def click_country(self):
        self.click(self.country_button)
    # ------------------------------------------------------------------------------------------------------------------
    phone_number_input = (By.ID, "com.oson:id/phone_number_edit_text")

    def input_phone_number(self, number):
        self.click(self.phone_number_input)
        self.input_text(self.phone_number_input, number)
    # ------------------------------------------------------------------------------------------------------------------
    offer_button = (By.ID, "com.oson:id/check_image_view")

    def click_offer_agreement(self):
        self.click(self.offer_button)
    # ------------------------------------------------------------------------------------------------------------------
    number_button_1 = (By.ID, "com.oson:id/widget_numerickeypadlayout_button_1")
    number_button_4 = (By.ID, "com.oson:id/widget_numerickeypadlayout_button_4")
    number_button_2 = (By.ID, "com.oson:id/widget_numerickeypadlayout_button_2")
    number_button_5 = (By.ID, "com.oson:id/widget_numerickeypadlayout_button_5")

    def enter_pin_code(self):
        self.click(self.number_button_1)
        self.click(self.number_button_4)
        self.click(self.number_button_2)
        self.click(self.number_button_5)
    # ------------------------------------------------------------------------------------------------------------------
    permission_deny_button = (By.ID, "com.android.permissioncontroller:id/permission_deny_button")

    def deny_permission(self):
        self.click(self.permission_deny_button)
    # ------------------------------------------------------------------------------------------------------------------
    user_profile = (By.ID, "com.oson:id/profile_fragment")

    def click_user_profile(self, timeout):
        self.click(self.user_profile, timeout)
    # ------------------------------------------------------------------------------------------------------------------