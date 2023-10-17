from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __log_out_button_location = ("xpath",
                                 "/html//div[@id='loop-container']/div/article//a[@href='https://practicetestautomation.com/practice-test-login/']")
    __header_locator = ("xpath", "//*[@id='loop-container']/div/article/div[1]/h1")

    def __int__(self, driver: WebDriver):
        super().__int__(driver)

    @property
    def expected_url(self):
        return self._url

    @property
    def header(self):
        return super().get_text(self.__header_locator)

    def is_logout_button_displayed(self):
        return super()._is_displayed(self.__log_out_button_location)
