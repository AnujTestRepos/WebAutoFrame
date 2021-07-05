from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class PurchasePage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//app-card[contains(@class,'col-lg-3')]/div")
    selectedProduct = (By.XPATH, "//*[contains(@class,'btn btn-info')]")
    checkout = (By.CSS_SELECTOR, ".btn-primary")
    productText = (By.XPATH, "//app-card[contains(@class,'col-lg-3')]/div/div/h4/a")

    def productList(self):
        return self.driver.find_elements(*PurchasePage.products)

    def productSelect(self):
        return self.driver.find_elements(*PurchasePage.selectedProduct)

    def productName(self):
        return self.driver.find_element(*PurchasePage.productText)

    def checkoutButton(self):
        self.driver.find_element(*PurchasePage.checkout).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        # Now to optimise further, first we find the interlink b/w the two webpages. Then in place of returning the
        # object of the page1, we perform the operations(like click() etc) here instead of doing it in testcase.
        # And also create the object of page 2 in same (Page1)file's method.
        # Then return this page 2 object only.
        # this should always be done in the method of page 1 which links to page 2.
