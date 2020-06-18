from selenium.webdriver.common.by import By

from ControlledLocators.ReusableActions import Locators


class LoginPage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    Forgot_Password_Text_ID = (By.XPATH, "//a[contains(text(),'Forgot your password?')]")
    Username_Textbox = (By.XPATH, "//input[@id='txtUsername']")
    Password_Textbox = (By.XPATH, "//input[@id='txtPassword']")
    Login_Button = (By.XPATH, "//input[@id='btnLogin']")

    # Test Data
    Username = "Admin"
    Password = "admin123"
    ForgotPasswordText = "Forgot"

    def getForgetPasswordTextId(self):
        return self.Forgot_Password_Text_ID

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

    def checkPresenceOfForgotPasswordText(self):
        global log
        log = self.getlogger()
        element = self.shouldBeDisplayed(self.getForgetPasswordTextId())
        assert (element.text == "Forgot your password?")

    def enterUsername(self):
        self.sendKeys(self.getUsernameFieldId(), self.getUsername())
        return LoginPage(self.driver)

    def enterPassword(self):
        self.sendKeys(self.getPasswordFieldId(), self.getPassword())
        return LoginPage(self.driver)

    def clickLoginButton(self):
        self.click(self.getLoginButton())
        return LoginPage(self.driver)

    def clickLogoutButton(self):
        self.click(self.getWelcomeButtonId())
        self.click(self.getLogoutButtonId())