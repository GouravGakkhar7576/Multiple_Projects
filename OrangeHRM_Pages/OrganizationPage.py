import time

from selenium.webdriver.common.by import By

from ControlledLocators.DropDownPage import DropDownPage
from ControlledLocators.JScript_Scroll_Bar import ScrollBar
from ControlledLocators.ReusableActions import Locators


class OrganizationPage(Locators):
    def __init__(self, driver):
        super().__init__(driver)

    # Organization Page Locators
    Organization_Text = (By.XPATH, "//a[@id='menu_admin_Organization']")
    General_Information_Button = (By.XPATH, "//a[@id='menu_admin_viewOrganizationGeneralInformation']")
    Edit_Button = (By.XPATH, "//input[@id='btnSaveGenInfo']")
    Organization_Name_Id = (By.XPATH, "//input[@id='organization_name']")
    Tax_Name_Id = (By.XPATH, "//input[@id='organization_taxId']")
    Registration_Name_Id = (By.XPATH, "//input[@id='organization_registraionNumber']")
    Org_Phone_Numb_Id = (By.XPATH, "//input[@id='organization_phone']")
    Org_Email_Id = (By.XPATH, "//input[@id='organization_email']")
    Org_Country_Name_Id = "//select[@id='organization_country']"
    Org_Note_Box_Id = (By.XPATH, "//textarea[@id='organization_note']")
    Org_Edit_Button_Id = (By.XPATH,"//input[@id='btnSaveGenInfo']")

    # Test Data
    Organization_Name = "QaTesting Experts"
    Tax_Id = "25965"
    Registration_Number = "A12B34"
    Phone_Number = "9859586225"
    Email_Id = "gouravgakkhar1@gmail.com"
    Country_Name = "India"
    Note = "This is Automation Testing Site"

    # Get Locator Ids Actions Performed
    def getPresenceOfOrganizationTextId(self):
        return self.Organization_Text

    def getGeneral_Info_Button_Id(self):
        return self.General_Information_Button

    def getOrganizationNameId(self):
        return self.Organization_Name_Id

    def getOrgTaxId(self):
        return self.Tax_Name_Id

    def getRegistrationNumberId(self):
        return self.Registration_Name_Id

    def getOrgPhoneNumId(self):
        return self.Org_Phone_Numb_Id

    def getOrgEditButtonId(self):
        return self.Org_Edit_Button_Id

    def getOrgEmailId(self):
        return self.Org_Email_Id

    def getOrgCountryNameId(self):
        return self.Org_Country_Name_Id

    def getOrgNoteBoxId(self):
        return self.Org_Note_Box_Id

    # Check Presence of element Actions Performed
    def checkPresenceOfOrganizationNameField(self):
        element = self.shouldBeDisplayed(self.getOrganizationNameId())
        if element.is_enabled():
            element.click()
            self.sendKeys(self.getOrganizationNameId(), self.Organization_Name)
        else:
            self.click(self.getOrgEditButtonId())
        return OrganizationPage(self.driver)

    # Mouse Hover Actions Performed
    def moveCursorToOrganizationText(self):
        self.mouseHoverToElement(self.getPresenceOfOrganizationTextId())
        return OrganizationPage(self.driver)

    # Click Actions Performed
    def clickOrgSaveButton(self):
        self.click(self.getOrgEditButtonId())

    def clickGeneralInfoButton(self):
        self.click(self.getGeneral_Info_Button_Id())

    # Enter Data in to the text field Actions Performed
    def enterOrganizationName(self):
        time.sleep(2)
        self.clearTheTextData(self.getOrganizationNameId())
        self.sendKeys(self.getOrganizationNameId(), self.Organization_Name)

    def enterTaxId(self):
        time.sleep(2)
        self.clearTheTextData(self.getOrgTaxId())
        self.sendKeys(self.getOrgTaxId(), self.Tax_Id)

    def enterRegistrationNumber(self):
        time.sleep(2)
        self.clearTheTextData(self.getRegistrationNumberId())
        self.sendKeys(self.getRegistrationNumberId(), self.Registration_Number)

    def enterPhoneNumber(self):
        time.sleep(2)
        self.clearTheTextData(self.getOrgPhoneNumId())
        self.sendKeys(self.getOrgPhoneNumId(), self.Phone_Number)

    def enterEmailId(self):
        time.sleep(2)
        self.clearTheTextData(self.getOrgEmailId())
        self.sendKeys(self.getOrgEmailId(), self.Email_Id)

    def enterNotes(self):
        time.sleep(2)
        self.clearTheTextData(self.getOrgNoteBoxId())
        self.sendKeys(self.getOrgNoteBoxId(), self.Note)

    # Select Value from Drop Down Actions Performed
    def selectCountryName(self):
        global drop
        drop = DropDownPage(self.driver)
        drop.Select_By_Visible_Text_From_DropDown(self.getOrgCountryNameId(), self.Country_Name)


class LocationsPage(Locators):
    def __init__(self, driver):
        super().__init__(driver)

    # Locations Page Locators
    Location_Button = (By.XPATH, "//a[@id='menu_admin_viewLocations']")
    Location_Name_Id = (By.XPATH, "//input[@id='searchLocation_name']")
    City_Name_Id = (By.XPATH, "//input[@id='searchLocation_city']")
    Country_ID = "//select[@id='searchLocation_country']"
    New_Location_Name_Id = (By.XPATH, "//input[@id='location_name']")
    New_Country_Name_Id = "//select[@id='location_country']"
    New_City_Name_Id = (By.XPATH, "//input[@id='location_city']")
    Table_Id = (By.XPATH, "//input[@id='btnSearch']")
    Column_Name_Id = (By.XPATH, "//a[@class='null'][contains(text(),'Country')]")
    Column_Value_Id = (By.XPATH, "//tr[@class='odd']//td[contains(text(),'India')]")
    Add_Button_Id = (By.XPATH, "//input[@id='btnAdd']")
    Save_Button_Id = (By.XPATH, "//input[@id='btnSave']")
    No_Record_Exist_Id = (By.XPATH, "//td[contains(text(),'No Records Found')]")
    Location_Search_Button_Id = (By.XPATH,"//input[@id='btnSearch']")

    # Test Data
    Location_Name = "India"
    City_Name = "India"
    Country_Name = "India"
    Column_Name = "Country"
    Column_Value = "India"

    # Get Locator Ids Actions Performed
    def getLocationButtonId(self):
        return self.Location_Button

    def getSearchLocationNameId(self):
        return self.Location_Name_Id

    def getSearchCityNameId(self):
        return self.City_Name_Id

    def getNoRecordExistId(self):
        return self.No_Record_Exist_Id

    def getSearchCountryNameId(self):
        return self.Country_ID

    def getNewLocationNameId(self):
        return self.New_Location_Name_Id

    def getNewCountryNameId(self):
        return self.New_Country_Name_Id

    def getNewCityNameId(self):
        return self.New_City_Name_Id

    def getCountryColumnNameId(self):
        return self.Column_Name_Id

    def getColumnName(self):
        return self.Column_Name

    def getColumnValue(self):
        return self.Column_Value

    def getCountryColumnValueId(self):
        return self.Column_Value_Id

    def getLocationSearchButtonId(self):
        return self.Location_Search_Button_Id

    # Click Actions Performed
    def clickLocationButton(self):
        self.click(self.getLocationButtonId())

    def clickLocationSearchButton(self):
        self.click(self.getLocationSearchButtonId())

    def clickLogoutButton(self):
        self.click(self.getWelcomeButtonId())
        self.click(self.getLogoutButtonId())

    # Enter Data in to the text field Actions Performed
    def enterSearchLocationName(self):
        self.sendKeys(self.getSearchLocationNameId(), self.Location_Name)
        return LocationsPage(self.driver)

    def enterSearchCityName(self):
        self.sendKeys(self.getSearchCityNameId(), self.City_Name)

    # Select Value from Drop Down Actions Performed
    def selectSearchCountryName(self):
        drop.Select_By_Visible_Text_From_DropDown(self.Country_ID, self.Country_Name)

    # Check Presence of element Actions Performed
    def checkPresenceOfStatusColumn(self):
        for col in self.Table_Id:
            element = self.verifyElementText(self.getCountryColumnNameId(), self.getColumnName())
            return OrganizationPage(self.driver)

    def checkPresenceOfColumnStatus(self):
        for col in self.Table_Id:
            if self.checkPresenceOfElement(self.getCountryColumnValueId()):
                print("India country exists")
                pass
            else:
                print("No Country exists")
                self.click(self.getAddButtonId())
                self.sendKeys(self.getNewLocationNameId(), self.Location_Name)
                drop.Select_By_Visible_Text_From_DropDown(self.New_Country_Name_Id, self.Country_Name)
                self.sendKeys(self.getNewCityNameId(), self.City_Name)
                self.click(self.getSaveButtonId())
                pass

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
        time.sleep(5)
        scroll = ScrollBar(self.driver)
        scroll.scroll_To_Vertical_Down_Of_Page()
        if self.checkPresenceOfElement(self.getNoRecordExistId()):
            self.getlogger().info("No Record Exist in the List")
            time.sleep(2)
            assert False
        else:
            self.getlogger().info("Looking for search records")
            time.sleep(2)
            table_id = self.driver.find_element_by_xpath("//table[@id='resultTable']")
            row_count = len(table_id.find_elements(By.TAG_NAME, "tr")) - 1
            self.getlogger().info("Total number of Rows = " + str(row_count))
            if row_count == 0:
                self.getlogger().info("No Row Exist with this search details in the Table")
            else:
                self.getlogger().info("Print all search records")
                self.printTableResult()
                self.getlogger().info("Looking for a column Name")
                if self.checkPresenceOfElement(self.getCountryColumnNameId()):
                    self.getlogger().info("Column Name Exist in Table")
                    time.sleep(2)
                    if self.checkPresenceOfElement(self.getCountryColumnValueId()):
                        self.getlogger().info("Column Values exist in the search Record")
                        time.sleep(2)
                    else:
                        self.getlogger().info("Record not exist with this Column Value")
                        time.sleep(2)
                else:
                    self.getlogger().info("No Column Name Exist in the Table")
                    assert False
