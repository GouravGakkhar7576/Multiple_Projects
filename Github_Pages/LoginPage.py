import time

from selenium.webdriver.common.by import By

from ControlledLocators.DropDownPage import DropDownPage
from ControlledLocators.JScript_Scroll_Bar import ScrollBar
from ControlledLocators.ReusableActions import Locators


class LoginPage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    Sign_In_Button_Id = (By.XPATH, "//a[contains(text(),'Sign in')]")
    Username_Textbox = (By.XPATH, "//input[@id='login_field']")
    Password_Textbox = (By.XPATH, "//input[@id='password']")
    Login_Button = (By.XPATH, "//input[@name='commit']")
    Header_Link_Id = (By.XPATH, "//summary[@class='Header-link']//img[contains(@class,'avatar avatar-user')]")
    Repositories_Id = (By.XPATH, "//a[contains(text(),'Your repositories')]")
    Sign_out_Button_Id = (By.XPATH, "//button[contains(text(),'Sign out')]")
    Repository_Name_Id = (By.XPATH, "//a[contains(text(),'PytestAnnoationsFramework')]")

    Username = "GouravGakkhar7576"
    Password = "gourav7576"
    Repository = "PytestAnnoationsFramework"

    def getSignInTextId(self):
        return self.Sign_In_Button_Id

    def getUsernameFieldId(self):
        return self.Username_Textbox

    def getUsername(self):
        return self.Username

    def getPasswordFieldId(self):
        return self.Password_Textbox

    def getPassword(self):
        return self.Password

    def getLoginButton(self):
        return self.Login_Button

    def getHeaderImageId(self):
        return self.Header_Link_Id

    def getRepositoriesId(self):
        return self.Repositories_Id

    def getMyRepositoriesId(self):
        return self.Repository_Name_Id

    def getSignOutId(self):
        return self.Sign_out_Button_Id

    def clickLoginTextButton(self):
        self.click(self.getSignInTextId())

    def enterUsername(self):
        self.sendKeys(self.getUsernameFieldId(), self.getUsername())
        return LoginPage(self.driver)

    def enterPassword(self):
        self.sendKeys(self.getPasswordFieldId(), self.getPassword())
        return LoginPage(self.driver)

    def clickLoginButton(self):
        self.click(self.getLoginButton())
        return LoginPage(self.driver)

    def clickToHeaderImage(self):
        self.click(self.getHeaderImageId())
        time.sleep(3)

    def clickYourRepositoryId(self):
        self.click(self.getRepositoriesId())

    def checkPresenceOfRepository(self):
        global log
        log = self.getlogger()
        element = self.shouldBeDisplayed(self.getMyRepositoriesId())
        print("Repository exist with Name : " + str(element.text))
        assert (element.text == self.Repository)

    def clickLogoutButton(self):
        self.click(self.getSignOutId())