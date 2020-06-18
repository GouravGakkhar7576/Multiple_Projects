from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ActionClass:

    def __init__(self, driver):
        self.driver = driver

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def move_to_element(self, by_locator):
        global act
        act = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        act.move_to_element(element).perform()
        return element

    # this function select the complete data added in the text field whose locator has been passed to it.

    def selectAllDatainTextbox(self):
        act.send_keys(Keys.CONTROL).send_keys("a").perform()

    # this function used to right click on the web element whose locator has been passed to it.

    def rightClickOnElement(self, by_locator):
        act.context_click(by_locator).perform()

    # this function used to double click on the web element whose locator has been passed to it.

    def doubleClick(self):
        act.double_click().perform()
