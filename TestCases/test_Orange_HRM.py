from BaseFiles.BaseClass import TestBaseClass
from OrangeHRM_Pages.LoginPage import LoginPage


class TestOrangeHRM(TestBaseClass):
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
