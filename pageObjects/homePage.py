# Here we define all the elements related to Home page of web application
# This is example of Page object model
# Also to optimize further, we created object of next page class in this page, instead of creating it in testcase file
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     # Keys are used to perform keyboard arrow operations


from pageObjects.purchasePage import PurchasePage


class HomePage:

    # created constructor to link the (instance variable)-driver to the object of class(HomePage) in Testcase
    def __init__(self, driver):
        self.driver = driver

    # Class variable which is of type tuple and hold type of locator(as 1st element) and actual locator(as 2nd element)
    shopButton = (By.XPATH, "//*[contains(@href,'angularpractice/shop')]")
    username = (By.XPATH, "//*[contains(@name,'name')]")
    emailid = (By.NAME, "email")
    password = (By.XPATH, "//*[contains(@type,'password')]")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    radiobutton = (By.XPATH, "//form[contains(@class,'ng-pristine ng-invalid ng-touched')]/div[6]")
    bday = (By.CSS_SELECTOR, "input[name='bday']")
    twowaytext = (By.XPATH, "//h4/input")
    successtext = (By.XPATH, "//*[contains(@class,'alert alert-success alert-dismissible')]")

    def shopItems(self):
        self.driver.find_element(*HomePage.shopButton).click()
        purchasepage = PurchasePage(self.driver)    # Created object of next page to optimize code further
        return purchasepage

        #  now this find_element() method takes the class variable as argument and breaks it to below type:
        # driver.find_element_by_xpath("xpath locator")
        # '*'(star) represents or tells find_element() method that the passed variable is of tuple type
        # return the element to the testcase for further operations

        # Now to optimise further, first we find the interlink b/w the two webpages. Then in place of returning the
        # object of the page1, we perform the operations(like click() etc) here instead of doing it in testcase.
        # And also create the object of page 2 in same (Page1)file's method.
        # Then return this page 2 object only.
        # this should always be done in the method of page 1 which links to page 2.

    def getuserName(self):
        user_name = self.driver.find_element(*HomePage.username)
        return user_name

    def getemailID(self):
        email = self.driver.find_element(*HomePage.emailid)
        return email

    def getpassWord(self):
        pass_word = self.driver.find_element(*HomePage.password)
        return pass_word

    def getcheckBox(self):
        check_box = self.driver.find_element(*HomePage.checkbox)
        return check_box

    def getstaticDropDown(self):
        staticDrop = self.driver.find_element(*HomePage.dropdown)
        return staticDrop

    def getradioButtons(self):
        selectRadios = self.driver.find_elements(*HomePage.radiobutton)
        return selectRadios

    def getbDay(self):
        b_day = self.driver.find_element(*HomePage.bday)
        return b_day

    def gettwoWayText(self):
        two_way_text = self.driver.find_element(*HomePage.twowaytext)
        return two_way_text

    def readsuccessAlert(self):
        successmsg = self.driver.find_element(*HomePage.successtext).text
        return successmsg


