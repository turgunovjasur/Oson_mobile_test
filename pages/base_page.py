from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 30

    def wait_for_presence(self, locator, timeout=None):
        """Element DOMda mavjud bo'lishini kutadi"""
        timeout = timeout or self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout):
        """Element bosiladigan holatga kelishini kutadi"""
        timeout = timeout or self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            element = self.wait_for_clickable(locator, timeout)
            element.click()
        except Exception as e:
            print(f"[XATO] Elementni bosishda xatolik: {e}")
            raise

    def input_text(self, locator, text, timeout=None):
        timeout = timeout or self.default_timeout

        try:
            element = self.wait_for_presence(locator, timeout)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"[XATO] Matn yuborishda xatolik: {e}")
            raise

    def is_displayed(self, locator, timeout=None):
        timeout = timeout or self.default_timeout

        try:
            element = self.wait_for_presence(locator, timeout)
            return element.is_displayed()
        except Exception:
            return False