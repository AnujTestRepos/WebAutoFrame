from selenium.webdriver.common.by import By


class CountryPage:
    countryPageLocator = (By.ID, "country")
    select_Country = (By.XPATH, "//*[contains(@class,'suggestions')]/ul/li/a")
    checkbox = (By.XPATH, "//*[contains(@class,'checkbox-primary')]")
    click_Purchase = (By.XPATH, "//*[contains(@type,'submit')]")
    success_msg = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def enterCountry(self):
        return self.driver.find_element(*CountryPage.countryPageLocator)

    def selectCountry(self):
        return self.driver.find_element(*CountryPage.select_Country)

    def selectCheckbox(self):
        return self.driver.find_element(*CountryPage.checkbox)

    def clickPurchase(self):
        return self.driver.find_element(*CountryPage.click_Purchase)

    def successMsg(self):
        return self.driver.find_element(*CountryPage.success_msg)
