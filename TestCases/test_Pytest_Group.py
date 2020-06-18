import pytest

from BaseFiles.BaseClass import TestBaseClass
from OrangeHRM_Pages.AdminPage import AdminPage
from OrangeHRM_Pages.LoginPage import LoginPage


@pytest.mark.LoginPage
class TestLoginPage(TestBaseClass):
    @pytest.mark.Admin
    @pytest.mark.Smoke
    def test_checkPresenceOfForgotPasswordText(self):
        global login
        login = LoginPage(self.driver)
        login.checkPresenceOfForgotPasswordText()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_enterUsername(self):
        login.enterUsername()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_enterPassword(self):
        login.enterPassword()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_clickLoginButton(self):
        login.clickLoginButton()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_checkPresenceOfPendingLeaveRequestText(self):
        global admin
        admin = AdminPage(self.driver)
        admin.checkPresenceOfPendingLeaveRequestText()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_checkPresenceOfAdminText(self):
        admin.moveCursorToAdminText()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_checkPresenceOfUserManagementText(self):
        admin.moveCursorToUserManagementText()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_clickUsersButton(self):
        admin.clickOnTheUsersButton()

    @pytest.mark.Smoke
    @pytest.mark.Admin
    def test_printAllUsersRecords(self):
        admin.printTableResult()

    @pytest.mark.Admin
    def test_enterSystemUserName(self):
        admin.enterSystemUserName()

    @pytest.mark.Admin
    def test_selectUserRole(self):
        admin.selectUserRoleValue()

    @pytest.mark.Admin
    def test_enterEmployeeName(self):
        admin.enterEmployeeName()

    @pytest.mark.Admin
    def test_selectEmployeeStatus(self):
        admin.selectEmployeeStatus()

    @pytest.mark.Admin
    def test_clickSearchButton(self):
        admin.clickSearchButton()

    @pytest.mark.Admin
    def test_verifySearchResult(self):
        admin.verifySearchResults()