import time

from selenium.webdriver.common.by import By

from ControlledLocators.DropDownPage import DropDownPage
from ControlledLocators.JScript_Scroll_Bar import ScrollBar
from ControlledLocators.ReusableActions import Locators


class AdminPage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Admin Page Locators
    Admin_Text = (By.XPATH, "//b[contains(text(),'Admin')]")
    Pending_Leave_Request_Text = (By.XPATH, "//legend[contains(text(),'Pending Leave Requests')]")
    User_Management_Text = (By.XPATH, "//a[@id='menu_admin_UserManagement']")
    Users_Button = (By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")
    Username_Text = (By.XPATH, "//input[@id='searchSystemUser_userName']")
    User_Role_DropDown = "//select[@id='searchSystemUser_userType']"
    Employee_Name_Text = (By.XPATH, "//input[@id='searchSystemUser_employeeName_empName']")
    Status_DropDown = "//select[@id='searchSystemUser_status']"
    Reset_Button = (By.XPATH, "//input[@id='resetBtn']")
    Table_Id = (By.XPATH, "//table[@id='resultTable']")
    Column_Name_ID = (By.XPATH, "//a[@class='null'][contains(text(),'Status')]")
    Column_Status_Value_Id = (By.XPATH, "//tr[@class='odd']//td[contains(text(),'Enabled')]")
    No_Record_Exist_Id = (By.XPATH, "//td[contains(text(),'No Records Found')]")

    # Test Data
    Presence_Of_Pending_Text = "Pending Leave Requests"
    Username = "Admin"
    Employee_Name = "Admin"
    UserRole = "Admin"
    Status = "Enabled"
    Column_Name = "Status"
    Column_Value = "Enabled"

    # Get Locator Ids Actions Performed
    def getPresenceOfAdminText(self):
        return self.Admin_Text

    def getPresenceOfPendingLeaveRequestText(self):
        return self.Pending_Leave_Request_Text

    def getPresenceOfUserManagementText(self):
        return self.User_Management_Text

    def getPresenceOfUsersButton(self):
        return self.Users_Button

    def getUsernameTextId(self):
        return self.Username_Text

    def getUserName(self):
        return self.Username

    def getUserRoleList(self):
        return self.User_Role_DropDown

    def getEmployeeNameId(self):
        return self.Employee_Name_Text

    def getEmployeeName(self):
        return self.Employee_Name

    def getStatusList(self):
        return self.Status_DropDown

    def getNoRecordExistId(self):
        return self.No_Record_Exist_Id

    def getColumnNameId(self):
        return self.Column_Name_ID

    def getColumnStatusValueId(self):
        return self.Column_Status_Value_Id

    # Check Presence of element Actions Performed
    def checkPresenceOfPendingLeaveRequestText(self):
        self.verifyElementText(self.getPresenceOfPendingLeaveRequestText(), self.Presence_Of_Pending_Text)
        return AdminPage(self.driver)

    # Click Actions Performed
    def clickOnTheUsersButton(self):
        self.click(self.Users_Button)
        return AdminPage(self.driver)

    def clickSearchButton(self):
        self.click(self.getSearchButtonId())

    def clickLogoutButton(self):
        self.click(self.getWelcomeButtonId())
        self.click(self.getLogoutButtonId())

    # Mouse Hover Actions Performed
    def moveCursorToAdminText(self):
        self.mouseHoverToElement(self.getPresenceOfAdminText())

    def moveCursorToUserManagementText(self):
        self.mouseHoverToElement(self.getPresenceOfUserManagementText())
        return AdminPage(self.driver)

    # Enter Data in to the text field Actions Performed
    def enterSystemUserName(self):
        self.sendKeys(self.getUsernameTextId(), self.getUserName())
        return AdminPage(self.driver)

    def enterEmployeeName(self):
        self.sendKeys(self.getEmployeeNameId(), self.getEmployeeName())
        return AdminPage(self.driver)

    # Select Value from Drop Down Actions Performed
    def selectUserRoleValue(self):
        global drop
        drop = DropDownPage(self.driver)
        drop.Select_By_Visible_Text_From_DropDown(self.getUserRoleList(), self.UserRole)
        return AdminPage(self.driver)

    def selectEmployeeStatus(self):
        drop.Select_By_Visible_Text_From_DropDown(self.getStatusList(), self.Status)
        return AdminPage(self.driver)

    # Print WebTable Records
    def printTableResult(self):
        scroll = ScrollBar(self.driver)
        scroll.scroll_To_Vertical_Down_Of_Page()
        table_id = self.driver.find_element_by_xpath("//table[@id='resultTable']")
        rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        row_count = len(table_id.find_elements(By.TAG_NAME, "tr")) - 1
        col_count = len(table_id.find_elements_by_xpath("//tr[1]/td"))
        self.getlogger().info("Total number of Rows = " + str(row_count))
        self.getlogger().info("Total Number of Columns = " + str(col_count))
        for row in rows:
            col = row.find_elements_by_xpath(".//td[@class='left'] | .//th[@class = 'header']")
            self.getlogger().info([td.text for td in col])

    # check presence of records in table

    def verifySearchResults(self):
        if self.checkPresenceOfElement(self.getNoRecordExistId()):
            self.getlogger().info("No Record Exist in the List")
            time.sleep(2)
        else:
            self.getlogger().info("Looking for search records")
            time.sleep(2)
            table_id = self.driver.find_element_by_xpath("//table[@id='resultTable']")
            row_count = len(table_id.find_elements(By.TAG_NAME, "tr")) - 1
            self.getlogger().info("Total number of Rows = " + str(row_count))
            if row_count == 0:
                self.getlogger().info("No Row Exist with this search details in the Table")
                assert False
            else:
                self.getlogger().info("Print all search records")
                self.printTableResult()
                self.getlogger().info("Looking for a column Name")
                if self.checkPresenceOfElement(self.getColumnNameId()):
                    self.getlogger().info("Column Name Exist in Table")
                    time.sleep(2)
                    if self.checkPresenceOfElement(self.getColumnStatusValueId()):
                        self.getlogger().info("Column Values exist in the search Record")
                        time.sleep(2)
                    else:
                        self.getlogger().info("Record not exist with this Column Value")
                        time.sleep(2)
                else:
                    self.getlogger().info("No Column Name Exist in the Table")
                    assert False

    def verifySearchColumnValue(self):
        self.getlogger().info("Verify Column Value exist in the Column List")
        if self.verifyElementText(self.getColumnStatusValueId(), self.Column_Value):
            self.getlogger().info("Column Values exist in the search Record")
            time.sleep(2)
        else:
            self.getlogger().info("Record not exist with this Column Value")
            time.sleep(2)
