import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

APK_PATH = "C:\\Users\\jasur.turgunov\\Desktop\\ish\\Oson_mobile_test\\app\\test.apk"
PACKAGE_NAME = "com.oson"

def get_android_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "R9TR8089DDM",
        "platformVersion": "12",
        "automationName": "UiAutomator2",
        "appPackage": "com.oson",
        "appActivity": "com.oson.ui.user.registration.UserRegistrationActivity",
        "noReset": True
    }

    options = UiAutomator2Options()
    for key, value in capabilities.items():
        options.set_capability(key, value)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    install_application(driver, APK_PATH, PACKAGE_NAME)

    return driver

def install_application(driver, apk_path, package_name):
    if driver.is_app_installed(package_name):
        driver.remove_app(package_name)
    driver.install_app(apk_path)
    driver.activate_app(package_name)
    time.sleep(5)