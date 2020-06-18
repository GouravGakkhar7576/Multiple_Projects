import pytest

from BaseFiles.BaseClass import Login_Applications
from OrangeHRM_Pages.JobPage import JobPage
from OrangeHRM_Pages.OrganizationPage import OrganizationPage, LocationsPage


class TestOrganizationPage(Login_Applications):
    @pytest.mark.Org
    def test_checkPresenceOfAdminText(self):
        global job
        job = JobPage(self.driver)
        job.moveCursorToAdminText()

    @pytest.mark.Org
    def test_checkPresenceOfOrganizationText(self):
        global org
        org = OrganizationPage(self.driver)
        org.moveCursorToOrganizationText()

    @pytest.mark.Org
    def test_clickGeneralInfoButton(self):
        org.clickGeneralInfoButton()

    @pytest.mark.Org
    def test_checkPresenceOfOrganizationNameField(self):
        org.checkPresenceOfOrganizationNameField()

    @pytest.mark.Org
    def test_enterOrganizationName(self):
        org.enterOrganizationName()

    @pytest.mark.skip
    def test_enterTaxId(self):
        org.enterTaxId()

    @pytest.mark.skip
    def test_enterRegistrationNumber(self):
        org.enterRegistrationNumber()

    @pytest.mark.xfail
    def test_enterPhoneNumber(self):
        org.enterPhoneNumber()

    @pytest.mark.Org
    def test_enterEmailId(self):
        org.enterEmailId()

    @pytest.mark.xfail
    def test_selectCountryName(self):
        org.selectCountryName()

    @pytest.mark.Org
    def test_enterNotes(self):
        org.enterNotes()

    @pytest.mark.Org
    def test_clickSaveButton(self):
        org.clickOrgSaveButton()