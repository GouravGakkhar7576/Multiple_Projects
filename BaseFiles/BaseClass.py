import pytest

from OrangeHRM_Pages.LoginPage import LoginPage


@pytest.mark.usefixtures('setup')
class TestBaseClass:
    pass


@pytest.mark.usefixtures('startBrowser')
class Login_Applications:

    def test_checkPresenceOfForgotPasswordText(self):
        global login
        login = LoginPage(self.driver)
        login.checkPresenceOfForgotPasswordText()

    def test_enterUsername(self):
        login.enterUsername()

    def test_enterPassword(self):
        login.enterPassword()

    def test_clickLoginButton(self):
        login.clickLoginButton()
