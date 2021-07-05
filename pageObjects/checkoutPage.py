from selenium.webdriver.common.by import By

from pageObjects.countryPage import CountryPage


class CheckoutPage:
    checkoutPageButton = (By.CSS_SELECTOR, ".btn-success")

    def __init__(self, driver):
        self.driver = driver

    def finalCheckoutPageButton(self):
        self.driver.find_element(*CheckoutPage.checkoutPageButton).click()
        countrypage = CountryPage(self.driver)
        return countrypage
        # Now to optimise further, first we find the interlink b/w the two webpages. Then in place of returning the
        # object of the page1, we perform the operations(like click() etc) here instead of doing it in testcase.
        # And also create the object of page 2 in same (Page1)file's method.
        # Then return this page 2 object only.
        # this should always be done in the method of page 1 which links to page 2.
