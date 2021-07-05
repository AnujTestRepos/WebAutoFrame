from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E_C
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.homePage import HomePage
from utilites.BaseClass import BaseClass


# @pytest.mark.usefixtures('setup') # This is commented because we have created BaseClass where the fixtures are used
# And we inherited the BaseClass in Test class
class TestE2E(BaseClass):
    def test_e2e(self):

        log = BaseClass.logCapture(self)
        log.info("Test will run in chrome by default")

        # explicit wait is defined in BaseClass so I commented the below step
        # wait = WebDriverWait(self.driver, 10)  # self.driver defined in conftest.py and linked via BaseClass inherit

        # This below syntax will be created in HomePage.py file as page object model
        # self.driver.find_element_by_xpath("//*[contains(@href,'angularpractice/shop')]").click()
        # to link the Page object(HomePage) with this testcase, create object of HomePage class here
        # And import the class above from HomePage.py file
        homePage = HomePage(self.driver)
        # Now use the object to perform operations on elements and call the method of homePage
        purchasePage = homePage.shopItems()  # purchasePage = PurchasePage(self.driver), this is more optimized
        products = purchasePage.productList()
        for product in products:
            # product_name = product.find_element_by_xpath("div/h4/a") -> this is replaced by below code
            product_name = purchasePage.productName().text
            if product_name == 'iphone X':
                log.info("The product selected :" + product_name)
                # print(product_name)
                # wait.until(E_C.presence_of_element_located((By.XPATH, "//*[contains(@class,'btn btn-info')]")))
                # product.find_element_by_xpath("//*[contains(@class,'btn btn-info')]").click()
                purchasePage.productSelect()[0].click()

        # self.driver.find_element_by_css_selector(".btn-success").click()
        finalCheckout = purchasePage.checkoutButton()  # finalCheckout = CheckoutPage(self.driver)
        country = finalCheckout.finalCheckoutPageButton()  # self.driver.find_element_by_id("country").send_keys("Ind")
        # country = CountryPage(self.driver)

        log.info("Sending 'Ind' to search and select the country")
        country.enterCountry().send_keys('Ind')

        # wait.until(E_C.presence_of_element_located((By.XPATH, "//*[contains(@class,'suggestions')]/ul/li/a")))
        # This explicit wait is common function to testcases so these are defined in BaseClass.py
        self.checkXpathElementPresent("//*[contains(@class,'suggestions')]/ul/li/a")

        # self.driver.find_element_by_xpath("//*[contains(@class,'suggestions')]/ul/li/a").click()
        country.selectCountry().click()

        # self.driver.find_element_by_xpath("//*[contains(@class,'checkbox-primary')]").click()
        country.selectCheckbox().click()

        # self.driver.find_element_by_xpath("//*[contains(@type,'submit')]").click()
        country.clickPurchase().click()

        # successMsg = self.driver.find_element_by_css_selector(".alert-success").text
        successMsg = country.successMsg().text

        assert "Success! Thank you!" in successMsg

        # take screenshot to a file
        self.driver.get_screenshot_as_file("testComplete_get_pic.png")
