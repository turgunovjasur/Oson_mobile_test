import time
from pages.user_profile_page import UserProfilePage
from utils.android_driver import get_android_driver
from pages.login_page import LoginPage


def test_login_flow():
    driver = get_android_driver()

    login = LoginPage(driver)
    login.click_uzbek_language()
    login.click_action()

    login.click_choose_country()
    login.input_search_country(country_cod="+998")
    login.click_country()

    login.input_phone_number(number="936026869")
    login.click_offer_agreement()
    login.click_action()
    login.click_user_profile(timeout=60)

    user_profile = UserProfilePage(driver)
    user_profile.click_user_data()
    user_profile.input_user_name(user_name="Jasur")
    user_profile.input_nick_name(nick_name="tjasur")
    user_profile.click_phone_change()
    user_profile.click_numeric_keypad()
    user_profile.click_change_number(number="936026869")
    user_profile.click_numer_change()
    user_profile.click_error_massage()
    user_profile.click_back_page()

    user_profile.click_user_data()
    user_profile.click_remove_user()
    user_profile.click_continue()
    user_profile.click_back_page()

    time.sleep(2)
    driver.quit()