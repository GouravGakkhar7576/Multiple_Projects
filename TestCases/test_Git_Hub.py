from BaseFiles.BaseClass import TestBaseClass
from Github_Pages.LoginPage import LoginPage


class TestGit(TestBaseClass):

    def test_clickLoginText(self):
        global login
        login = LoginPage(self.driver)
        login.clickLoginTextButton()

    def test_enterUsername(self):
        login.enterUsername()

    def test_enterPassword(self):
        login.enterPassword()

    def test_clickLoginButton(self):
        login.clickLoginButton()

    def test_clickToLoggedUser(self):
        login.clickToHeaderImage()

    def test_clickYourRepository(self):
        login.clickYourRepositoryId()

    def test_checkPresenceOfRepository(self):
        login.checkPresenceOfRepository()

    def test_clickToHeaderImage(self):
        login.clickToHeaderImage()

    def test_clickLogoutButton(self):
        login.clickLogoutButton()
