import pytest

from pageObjects.homePage import HomePage
from testData.homePageData import HomePageData
from utilites.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys


class TestHomePage(BaseClass):

    def test_form(self, getDataLoad):
        log = self.logCapture()
        log.info("Form submission test started")
        homepage = HomePage(self.driver)
        log.info("firstname: "+ getDataLoad['firstname'])
        homepage.getuserName().send_keys(getDataLoad['firstname'])
        homepage.getemailID().send_keys(getDataLoad['email'])
        homepage.getpassWord().send_keys(getDataLoad['password'])
        homepage.getcheckBox().click()

        # calling select and send location of static dropdown and text to select from it
        self.selectOptionsByText(homepage.getstaticDropDown(), getDataLoad["gender"])

        radio_buttons = homepage.getradioButtons()
        for button in radio_buttons:
            if button.find_element_by_xpath("div/label").text == getDataLoad['emp_status']:
                button.find_element_by_xpath("div/label").click()

        homepage.getbDay().send_keys(getDataLoad['dob'])
        homepage.getbDay().send_keys(Keys.ARROW_RIGHT)
        homepage.getbDay().send_keys(getDataLoad['yob'])

        self.driver.find_element_by_css_selector(".btn-success").click()
        assert "Success!" in homepage.readsuccessAlert()
        log.info("Form success message : "+ homepage.readsuccessAlert())
        self.driver.refresh()

    # Data processing using fixture.
    # fixtures are defined in same testcase file because these data is only specific to this testcase.
    # data processing are defined in separate data file under testData package/folder.
    # Earlier the data was directly passed in fixtures here,
    # but to optimize this we created class in homePageData file under testData package.

    #  now getting the data with dictionary from fixtures(params) instead of tuple.
    #   This is more optimized way of fetching data to testcases.
    """@pytest.fixture(params=[("TestUser", "testuser@gmail.com", "Test@123", "Male", "Student", "08Aug", "1990"),
                        ("TestUser1", "testuser2@gmail.com", "Test@123", "Female", "Employed", "08Aug", "1990")])"""
    @pytest.fixture(params=HomePageData.test_homePage_Data)
    def getDataLoad(self, request):
        return request.param

