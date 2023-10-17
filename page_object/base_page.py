from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator, text):
        self._find(locator).send_keys(text)

    def _click(self, locator):
        self._find(locator).click()

    @property
    def current_url(self):
        return self._driver.current_url

    def _is_displayed(self, locator):
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url):
        self._driver.get(url)

    def get_text(self,locator):
        return self._find(locator).text


