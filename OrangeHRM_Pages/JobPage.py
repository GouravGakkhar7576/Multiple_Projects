import math
import os
import time

from selenium.webdriver.common.by import By

from ControlledLocators.ActionClass import ActionClass
from ControlledLocators.DropDownPage import DropDownPage
from ControlledLocators.JScript_Scroll_Bar import ScrollBar
from ControlledLocators.ReusableActions import Locators


class JobPage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Common Locators
    Job_Menu_Text = (By.XPATH, "//a[@id='menu_admin_Job']")
    Table_Id = (By.XPATH, "//table[@id='resultTable']")

    # Job Title Page Locators
    Admin_Text = (By.XPATH, "//b[contains(text(),'Admin')]")
    Job_Title_Button = (By.XPATH, "//a[@id='menu_admin_viewJobTitleList']")
    Job_Title_Column_Id = (By.XPATH, "//table[@id='resultTable']//a[contains(text(),'Job Title')]")
    Column_Value_Id = (By.XPATH, "//tr[@class='odd']//a[contains(text(),'Software Testing Engineer')]")
    Job_Title_Text = (By.XPATH, "//input[@id='jobTitle_jobTitle']")
    Job_Description_Text = (By.XPATH, "//textarea[@id='jobTitle_jobDescription']")
    Choose_File_Button = (By.XPATH, "//input[@id='jobTitle_jobSpec']")

    # Test Data
    Job_Title = "Engineer Services"
    Job_Description = "Python Automation Testing"
    Column_Name = "Job Title"

    # Get Locator Ids Actions Performed
    def getPresenceOfAdminText(self):
        return self.Admin_Text

    def getPresenceOfJobMenuText(self):
        return self.Job_Menu_Text

    def getJobTitleButton(self):
        return self.Job_Title_Button

    def getColumnValueId(self):
        return self.Column_Value_Id

    def getJobTitleText(self):
        return self.Job_Title_Text

    def getJobDescriptionText(self):
        return self.Job_Description_Text

    def getChooseFileButton(self):
        return self.driver.find_element(*JobPage.Choose_File_Button)

    def getJobTitleColumnId(self):
        return self.Job_Title_Column_Id

    # Check Presence of element Actions Performed
    def moveCursorToAdminText(self):
        self.mouseHoverToElement(self.getPresenceOfAdminText())
        return JobPage(self.driver)

    def checkPresenceOfJobMenuText(self):
        self.mouseHoverToElement(self.getPresenceOfJobMenuText())
        return JobPage(self.driver)

    def checkPresenceOfJobTitleInColumn(self):
        jsc = ScrollBar(self.driver)
        jsc.scroll_To_Vertical_Down_Of_Page()
        act = ActionClass(self.driver)
        element = act.move_to_element(self.getColumnValueId())
        assert element.text == self.Job_Title
        self.getlogger().info("Job Title Added Successfully")

    # Click Actions Performed
    def clickJobTitleButton(self):
        self.click(self.getJobTitleButton())
        return JobPage(self.driver)

    def clickAddButton(self):
        self.click(self.getAddButtonId())
        return JobPage(self.driver)

    def clickSaveButton(self):
        self.click(self.getSaveButtonId())
        return JobPage(self.driver)

    # Enter Data in to the text field Actions Performed
    def enterJobTitle(self):
        self.sendKeys(self.getJobTitleText(), self.Job_Title)
        time.sleep(1)
        self.checkPresenceOfValidationError(self.getJobTitleText(), self.Job_Title)
        return JobPage(self.driver)

    def enterJobDescription(self):
        self.sendKeys(self.getJobDescriptionText(), self.Job_Description)
        return JobPage(self.driver)

    # Select the file from Local System Actions Performed
    def selectFile(self):
        file_path = r"C:\Users\GOURAV\Desktop\Sample Image\importData.csv"
        self.getChooseFileButton().send_keys(file_path)
        ext = os.path.splitext(file_path)[-1].lower()
        self.getlogger().info("Extension of Uploaded File is correct- " + str(ext))
        st = os.path.getsize(file_path)
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(st, 1024)))
        p = math.pow(1024, i)
        s = round(st / p, 2)
        fix = 1048576
        if st < fix:
            self.getlogger().info("File Size less than 1mb - " + "%s %s" % (s, size_name[i]))
            return "%s %s" % (s, size_name[i])
        else:
            self.getlogger().info("File Size greater than 1mb - " + "%s %s" % (s, size_name[i]))
            assert False


class PayGradePage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Pay Grade Page Locators
    Pay_Grades_Button = (By.XPATH, "//a[@id='menu_admin_viewPayGrades']")
    Pay_Grade_Column_Id = (By.XPATH, "//table[@id='resultTable']//a[contains(text(),'Pay Grade')]")
    Pay_Grade_Name_Text_Id = (By.XPATH, "//input[@id='payGrade_name']")

    # Test Data
    Pay_Grade_Column = "Pay Grade"
    Pay_Grade_Name = "Engineers Data Services"

    # Get Locator Ids Actions Performed
    def getPayGradeButtonId(self):
        return self.Pay_Grades_Button

    def getPayGradeColumnNameId(self):
        return self.Pay_Grade_Column_Id

    def getPayGradeNameId(self):
        return self.Pay_Grade_Name_Text_Id

    # Click Actions Performed
    def clickPayGradeButton(self):
        self.click(self.getPayGradeButtonId())
        return PayGradePage(self.driver)

    # Check Presence of element Actions Performed
    def checkPresenceOfPayGradeColumn(self):
        job = JobPage(self.driver)
        for col in job.Table_Id:
            self.verifyElementText(self.getPayGradeColumnNameId(), self.Pay_Grade_Column)
        return PayGradePage(self.driver)

    # Enter Data in to the text field Actions Performed
    def enterPayGradeName(self):
        self.sendKeys(self.getPayGradeNameId(), self.Pay_Grade_Name)
        self.checkPresenceOfValidationError(self.getPayGradeNameId(),self.Pay_Grade_Name)
        return PayGradePage(self.driver)


class EmploymentPage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Employment Status Page Locators
    Employment_Status_Button = (By.XPATH, "//a[@id='menu_admin_employmentStatus']")
    Employment_Status_Column_Id = (By.XPATH, "//table[@id='resultTable']//span[contains(text(),'Employment Status')]")
    Employment_Status_Name_Id = (By.XPATH, "//input[@id='empStatus_name']")

    # Test Data
    Employment_Status_Name = "Engineer Data Services"
    Employment_Status_Column_Name = "Employment Status"

    # Get Locator Ids Actions Performed
    def getEmploymentStatusButtonId(self):
        return self.Employment_Status_Button

    def getEmploymentStatusColumnId(self):
        return self.Employment_Status_Column_Id

    def getEmploymentStatusNameId(self):
        return self.Employment_Status_Name_Id

    # Click Actions Performed
    def clickEmploymentStatusButton(self):
        self.click(self.getEmploymentStatusButtonId())
        return EmploymentPage(self.driver)

    # Check Presence of element Actions Performed
    def checkPresenceOfEmploymentColumn(self):
        job = JobPage(self.driver)
        for col in job.Table_Id:
            self.verifyElementText(self.getEmploymentStatusColumnId(), self.Employment_Status_Column_Name)
        return EmploymentPage(self.driver)

    # Enter Data in to the text field Actions Performed
    def enterEmploymentName(self):
        self.sendKeys(self.getEmploymentStatusNameId(), self.Employment_Status_Name)
        self.checkPresenceOfValidationError(self.getEmploymentStatusNameId(), self.Employment_Status_Name)
        return EmploymentPage(self.driver)


class JobCategories(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Job Categories Page Locators
    Job_Categories_Button = (By.XPATH, "//a[@id='menu_admin_jobCategory']")
    Job_Categories_Column_Id = (By.XPATH, "//table[@id='resultTable']//span[contains(text(),'Job Category')]")
    Job_Category_Name_Id = (By.XPATH, "//input[@id='jobCategory_name']")

    # Test Data
    Job_Category_Name = "Engineer Data"
    Job_Categories_Column_Name = "Job Category"

    # Get Locator Ids Actions Performed
    def getJobCategoryButtonId(self):
        return self.Job_Categories_Button

    def getJobCategoryColumnId(self):
        return self.Job_Categories_Column_Id

    def getJobCategoryNameId(self):
        return self.Job_Category_Name_Id

    # Click Actions Performed
    def clickJobCategoryButton(self):
        self.click(self.getJobCategoryButtonId())
        return EmploymentPage(self.driver)

    # Check Presence of element Actions Performed
    def checkPresenceOfJobCategoryColumn(self):
        job = JobPage(self.driver)
        for col in job.Table_Id:
            self.verifyElementText(self.getJobCategoryColumnId(), self.Job_Categories_Column_Name)
        return EmploymentPage(self.driver)

    # Enter Data in to the text field Actions Performed
    def enterJobCategoryName(self):
        self.sendKeys(self.getJobCategoryNameId(), self.Job_Category_Name)
        self.checkPresenceOfValidationError(self.getJobCategoryNameId(), self.Job_Category_Name)
        return EmploymentPage(self.driver)


class WorkShiftsPage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Work Shifts Page Locators
    Work_Shifts_Id = (By.XPATH, "//a[@id='menu_admin_workShift']")
    Shift_Name_Column_Id = (By.XPATH, "//table[@id='resultTable']//span[contains(text(),'Shift Name')]")
    Work_Shift_Name_Id = (By.XPATH, "//input[@id='workShift_name']")
    Work_Shift_Hours_From_Drop_Down = "//select[@id='workShift_workHours_from']"
    Work_Shift_Hours_To_Drop_Down = "//select[@id='workShift_workHours_to']"
    Duration_Id = (By.XPATH, "//input[@class='time_range_duration']")
    Available_Employees_Drop_Down_Id = "//select[@id='workShift_availableEmp']"
    Add_Employee = (By.XPATH, "//a[@id='btnAssignEmployee']")
    Assigned_Employees_Drop_Down_Id = "//select[@id='workShift_assignedEmp']"

    # Test Data
    Shift_Column_Name = "Shift Name"
    Work_Shift_Name = "Night Shift"
    Work_ShiftHours_From = '08:00'
    Work_ShiftHours_To = '18:00'
    Time_Duration = '10'
    Available_Employee_Name = "1"
    Assigned_Employee_Name = "1"

    # Get Locator Ids Actions Performed
    def getWorkShiftButtonId(self):
        return self.Work_Shifts_Id

    def getShiftNameColumnId(self):
        return self.Shift_Name_Column_Id

    def getWorkShiftName(self):
        return self.Work_Shift_Name_Id

    def getShiftWorkFromDropDownId(self):
        return self.Work_Shift_Hours_From_Drop_Down

    def getWorkShiftFrom(self):
        return self.Work_ShiftHours_From

    def getShiftWorkToDropDownId(self):
        return self.Work_Shift_Hours_To_Drop_Down

    def getWorkShiftTo(self):
        return self.Work_ShiftHours_To

    def getDurationId(self):
        return self.Duration_Id

    def getDurationTime(self):
        return self.Time_Duration

    def getAvailableEmployeeNamesId(self):
        return self.Available_Employees_Drop_Down_Id

    def getAvailableEmpName(self):
        return self.Available_Employee_Name

    def getAssignEmpName(self):
        return self.Assigned_Employee_Name

    def getAddEmployeeButtonId(self):
        return self.Add_Employee

    def getAssignedEmployeeNameId(self):
        return self.Assigned_Employees_Drop_Down_Id

    # Click Actions Performed
    def clickWorkShiftsButton(self):
        self.click(self.getWorkShiftButtonId())
        return WorkShiftsPage(self.driver)

    def clickAddEmployeeButton(self):
        self.click(self.getAddEmployeeButtonId())

    def clickLogoutButton(self):
        self.click(self.getWelcomeButtonId())
        self.click(self.getLogoutButtonId())

    # Check Presence of element Actions Performed
    def checkPresenceOfShiftNameColumn(self):
        job = JobPage(self.driver)
        for col in job.Table_Id:
            self.verifyElementText(self.getShiftNameColumnId(), self.Shift_Column_Name)
        return WorkShiftsPage(self.driver)

    def checkPresenceOfDuration(self):
        time.sleep(1)
        element = self.getAttributeValue(self.getDurationId())
        if element == self.Time_Duration:
            self.getlogger().info("Time Duration for Work Shift are :" + str(element))
        else:
            self.getlogger().info("Time Duration should not be found")

    # Enter Data in to the text field Actions Performed
    def enterWorkShiftName(self):
        self.sendKeys(self.getWorkShiftName(), self.Work_Shift_Name)
        self.checkPresenceOfValidationError(self.getWorkShiftName(), self.Work_Shift_Name)
        return WorkShiftsPage(self.driver)

    # Select Value from Drop Down Actions Performed
    def selectShiftWorkFrom(self):
        time.sleep(1)
        global drop
        drop = DropDownPage(self.driver)
        drop.Select_By_Value_From_DropDown(self.getShiftWorkFromDropDownId(), self.Work_ShiftHours_From)
        return WorkShiftsPage(self.driver)

    def selectShiftWorkTo(self):
        time.sleep(1)
        drop.Select_By_Value_From_DropDown(self.getShiftWorkToDropDownId(), self.Work_ShiftHours_To)
        return WorkShiftsPage(self.driver)

    def selectAvailableEmployee(self):
        time.sleep(1)
        drop.Select_By_Value_From_DropDown(self.getAvailableEmployeeNamesId(), self.Available_Employee_Name)
        return WorkShiftsPage(self.driver)

    def selectAssignedEmployee(self):
        time.sleep(2)
        drop.Select_By_Value_From_DropDown(self.getAssignedEmployeeNameId(), self.Assigned_Employee_Name)
        return WorkShiftsPage(self.driver)
