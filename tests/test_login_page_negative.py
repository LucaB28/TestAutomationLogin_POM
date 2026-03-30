import os
from dotenv import load_dotenv
load_dotenv()

import time
import pytest
from selenium import webdriver
from page_object.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [(os.environ.get("TEST_WRONG_USER", ""), os.environ.get("TEST_PASSWORD", ""), "Your username is invalid!"),
                              (os.environ.get("TEST_USERNAME", ""), os.environ.get("TEST_WRONG_PASS", ""), "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        time.sleep(2)
        assert login_page.get_error_message() == expected_error_message, "error message is not expected"

