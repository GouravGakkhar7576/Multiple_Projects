import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Locators:

    def __init__(self, driver):
        self.driver = driver

    # Reusable methods in the complete Application

    # This function used to automate the complete Admin section details
    Search_Button = (By.XPATH, "//input[@id='searchBtn']")
    Add_Button = (By.XPATH, "//input[@id='btnAdd']")
    Save_Button = (By.XPATH, "//input[@id='btnSave']")
    Validation_Error_Id = (By.XPATH, "//span[@class='validation-error']")
    Welcome_Id_Button = (By.XPATH, "//a[@id='welcome']")
    Logout_Button_Id = (By.XPATH, "//a[contains(text(),'Logout')]")
    Edit_Button_Id = (By.XPATH, "//input[@id='btnSave']")

    def getSearchButtonId(self):
        return self.Search_Button

    def getAddButtonId(self):
        return self.Add_Button

    def getSaveButtonId(self):
        return self.Save_Button

    def getWelcomeButtonId(self):
        return self.Welcome_Id_Button

    def getLogoutButtonId(self):
        return self.Logout_Button_Id

    def getEditButtonId(self):
        return self.Edit_Button_Id

    # Methods to perform actions on the pages

    # Time Period to wait until element located
    def staticWaitTime(self):
        timeout = 20
        return timeout

    # Method to perform action on the Browser
    def backBrowserButton(self):
        self.driver.execute_script("window.history.go(-1)")

    # Method for Traceable actions
    def executionStartTime(self):
        starting = time.perf_counter()
        return round(starting)

    def executionStopTime(self):
        showtime = time.perf_counter()
        return round(showtime)

    def getValidationErrorId(self):
        return self.Validation_Error_Id

    # this function used to verify that data should already exist or not.
    def checkPresenceOfValidationError(self, by_locator, text):
        if self.checkPresenceOfElement(self.getValidationErrorId()):
            print("Validation Error Exists")
            time.sleep(1)
            self.clearTheTextData(by_locator)
            rename_text = ("Rename" + str(text))
            print("Data should be renamed : " + str(rename_text))
            self.sendKeys(by_locator, rename_text)
            pass
        else:
            print("No Validation Error exists")
            pass

    # this function used to click on the button in any page.
    def click(self, by_locator):
        start = self.executionStartTime()
        WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator)).click()
        stop = self.executionStopTime()
        total_time = round(stop - start)
        self.getlogger().info("Element should be found and clicked in = " + str(total_time) + "ms")

    # this function asserts comparison of a web element's text with passed in text.
    def verifyElementText(self, by_locator, element_text):
        start = self.executionStartTime()
        web_element = WebDriverWait(self.driver, self.staticWaitTime()).until(
            EC.visibility_of_element_located(by_locator))
        stop = self.executionStopTime()
        total_time = round(stop - start)
        self.getlogger().info("Element - " + str(web_element.text) + " should be found in " + str(total_time) + "ms")
        if web_element.text == element_text:
            self.getlogger().info("Assertion of element should be Passed Successfully - ")
        else:
            self.getlogger().info("Expected Element not Matched with Actual Element: Assertion Failed")
            assert False

    # this function return a web element's for used for any other purpose in the script.
    def getElementText(self, by_locator):
        web_element = WebDriverWait(self.driver, self.staticWaitTime()).until(
            EC.visibility_of_element_located(by_locator))
        self.getlogger().info("Element/Text present on the page - " + str(web_element.text))
        if web_element.text:
            return web_element.text
        else:
            return "No Text found on the page"

    # this function clear the data added in the text field
    def clearTheTextData(self, by_locator):
        WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator)).clear()
        self.getlogger().info("Data should be deleted from the field successfully")

    # this function performs enter text in the field, in a web element whose locator is passed to it.
    def sendKeys(self, by_locator, text):
        element = WebDriverWait(self.driver, self.staticWaitTime()). \
            until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        self.getlogger().info("Text Data should be entered in the field - " + str(text))
        return element

    # this function checks if the web element is present on the page or not whose locator has been passed to it
    def shouldBeDisplayed(self, by_locator):
        element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator))
        self.getlogger().error("Element should be displayed on the page - " + str(element.text))
        return element

    def getAttributeValue(self, by_locator):
        self.getlogger().info("Looking for an Attribute value")
        element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.presence_of_element_located(by_locator))
        value = element.get_attribute('value')
        return value

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def visibilityOfElement(self, by_locator):
        element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function checks if the web element whose locator has been passed to it, is present on the web page or not.
    # return true or false depending upon its presence.
    def checkAssertion(self, by_locator, text):
        global not_found
        try:
            web_element = WebDriverWait(self.driver, self.staticWaitTime()).until(
                EC.presence_of_element_located(by_locator))
            if web_element.text == text:
                not_found = True
                print("Expected value should be equal to Actual value: Assertion Passed")
        except:
            not_found = False
            print("Expected value should not be equal to Actual value: Assertion Failed")
        return not_found

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def mouseHoverToElement(self, by_locator):
        element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
        self.getlogger().info("Mouse hover to the element - " + str(element.text))

    # this function return presence of Element on Web page or not.
    def checkPresenceOfElement(self, by_locator):
        try:
            WebDriverWait(self.driver, self.staticWaitTime()).until(EC.presence_of_element_located(by_locator))
            not_found = True
            print("Element present on the page")
        except:
            not_found = False
            print("No Error/Element present on the page")
        return not_found

    # this function used to add logger message and generate log report in the framework.
    def getlogger(self):
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.setLevel(logging.DEBUG)
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        logger.addHandler(console)
        handler = logging.FileHandler('C:\\Users\\GOURAV\\PycharmProjects\\MultipleProjects\\LogFiles\\LogDetails.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
