import time

from selenium.webdriver.support.select import Select


class DropDownPage:

    def __init__(self, driver):
        self.driver = driver

    # this function used to select the value from Drop Down by using INDEX whose locator has been passed to it.
    def Select_By_Index_From_DropDown(self, locator, int_index):
        data = self.driver.find_element_by_xpath(locator)
        sel = Select(data)
        sel.select_by_index(int_index)

    # this function used to select the value from Drop Down by using VALUE whose locator has been passed to it.
    def Select_By_Value_From_DropDown(self, locator, value):
        sel = Select(self.driver.find_element_by_xpath(locator))
        sel.select_by_value(value)

    # this function used to select the value from Drop Down by using VISIBLE TEXT whose locator has been passed to it.
    def Select_By_Visible_Text_From_DropDown(self, locator, str_data):
        data = self.driver.find_element_by_xpath(locator)
        sel = Select(data)
        sel.select_by_visible_text(str_data)

    # this function used to select the value from Dynamic Result in the DROP DOWN whose locator has been passed to it.

    def Select_Dynamic_Value_Drop_Down(self, locator):
        time.sleep(5)
        element = self.driver.find_element_by_xpath(locator.DYNAMIC_DROP_DOWN)
        element.click()

