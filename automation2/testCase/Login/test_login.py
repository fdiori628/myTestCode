import inspect

import pytest
from Common.web_config_until import WebConfig
from Components.Component.Login import Login
from Components.Component.Project import Project
from time import sleep
from Common.logger_until import Logger


class TestLogin:
    config = WebConfig('Login')
    url = config.testdata["env"][217]
    user_valid = config.testdata["user"]["valid"]
    user_invalid = config.testdata["user"]["invalid"]
    logger = Logger()

    @pytest.fixture(scope="class", autouse=True)
    def values_test_start(self, driver):
        self.logger.logger("===================Login testing is started==============================================")
        yield
        self.logger.logger("===================Login testing is completed============================================")
        driver.quit()

    @pytest.fixture(scope="function")
    def visit_esb(self, driver):
        try:
            self.logger.logger(f"visit {self.url}")
            driver.get(self.url)
        except TimeoutError:
            self.logger.logger("visit esb timeout, will retry")
            self.logger.logger(f"retrying visit {self.url}")
            driver.get(self.url)

    @pytest.fixture(scope="function")
    def visit_clientportal(self, driver):
        url = self.config.testdata["env"]["client_portal"]
        try:
            self.logger.logger(f"visit {url}")
            driver.get(url)
        except TimeoutError:
            self.logger.logger("visit client-portal timeout, will retry")
            self.logger.logger(f"retrying visit {self.url}")
            driver.get(self.url)

    @pytest.mark.high
    @pytest.mark.parametrize('user_valid', user_valid)
    def testlogin_esb_success(self, user_valid, visit_esb, driver):
        login = Login(driver)
        expect_username = user_valid["user_name"]
        self.logger.logger(f"input username")
        login.username_input(user_valid["username"])
        self.logger.logger(f"input password")
        login.password_input(user_valid["password"])
        if not login.privacy_checkbox()[1]:
            self.logger.logger(f"click on privacy checkbox")
            login.privacy_check_click()
        sleep(1)
        self.logger.logger(f"click on submit")
        login.submit()
        self.logger.logger(f"checking username_span....")
        username = Project(driver).username_span().text
        self.logger.logger(f"target username: {expect_username}, actually username: {username}")
        assert username == expect_username
        self.logger.logger(f"testcase //{inspect.stack()[0][3]}// is completed and passed")

    @pytest.mark.critical
    @pytest.mark.parametrize('user_invalid', user_invalid)
    def testlogin_esb_fail(self, user_invalid, visit_esb, driver):
        login = Login(driver)
        msg = user_invalid["message"]
        self.logger.logger(f"input username")
        login.username_input(user_invalid["username"])
        self.logger.logger(f"input password")
        login.password_input(user_invalid["password"])
        if not login.privacy_checkbox()[1]:
            self.logger.logger(f"click on privacy checkbox")
            login.privacy_check_click()
        sleep(1)
        self.logger.logger(f"click on submit")
        login.submit()
        self.logger.logger(f"getting error message")
        err_msg = login.error_message()
        current_url = driver.current_url
        assert err_msg == msg, "login" in current_url
        self.logger.logger(f"testcase //{inspect.stack()[0][3]}// is completed and passed")

    @pytest.mark.critical
    @pytest.mark.parametrize('user_valid', user_valid)
    def testlogin_clientportal_success(self, user_valid, visit_clientportal, driver):
        login = Login(driver)
        expect_username = user_valid["user_name"]
        self.logger.logger(f"input username")
        login.username_input(user_valid["username"])
        self.logger.logger(f"input password")
        login.password_input(user_valid["password"])
        if not login.privacy_checkbox()[1]:
            self.logger.logger(f"click on privacy checkbox")
            login.privacy_check_click()
        sleep(1)
        self.logger.logger(f"click on submit")
        login.submit()
        self.logger.logger(f"checking username_span....")
        username = Project(driver).username_span().text
        assert username == expect_username
        self.logger.logger(f"testcase //{inspect.stack()[0][3]}// is completed and passed")

    @pytest.mark.critical
    @pytest.mark.parametrize('user_invalid', user_invalid)
    def testlogin_clientportal_fail(self, user_invalid, visit_clientportal, driver):
        login = Login(driver)
        msg = user_invalid["message"]
        self.logger.logger(f"input username")
        login.username_input(user_invalid["username"])
        self.logger.logger(f"input password")
        login.password_input(user_invalid["password"])
        if not login.privacy_checkbox()[1]:
            self.logger.logger(f"click on privacy checkbox")
            login.privacy_check_click()
        sleep(1)
        self.logger.logger(f"click on submit")
        login.submit()
        self.logger.logger(f"getting error message")
        err_msg = login.error_message()
        current_url = driver.current_url
        assert err_msg == msg, "login" in current_url
        self.logger.logger(f"testcase //{inspect.stack()[0][3]}// is completed and passed")

    # @pytest.mark.critical
    # @pytest.mark.parametrize('user_valid', user_valid)
    # def testlogin_clientportal_forgotpwd(self, user_valid, visit_clientportal, driver):
    #     login = Login(driver)
    #     expect_username = user_valid["user_name"]
    #     self.logger.logger(f"input username")
    #     login.username_input(user_valid["username"])
    #     self.logger.logger(f"input password")
    #     login.password_input(user_valid["password"])
    #     if not login.privacy_checkbox()[1]:
    #         self.logger.logger(f"click on privacy checkbox")
    #         login.privacy_check_click()
    #     sleep(1)
    #     self.logger.logger(f"click on submit")
    #     login.submit()
    #     self.logger.logger(f"checking username_span....")
    #     username = Project(driver).username_span().text
    #     assert username == expect_username
    #     self.logger.logger(f"testcase //{inspect.stack()[0][3]}// is completed and passed")
