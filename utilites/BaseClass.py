# This is base class where we define all the common functions to the testcases.

import inspect
import pytest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E_C
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures('setup')
class BaseClass:
    def logCapture(self):
        # inspect.stack() method gets the test file name
        testFileName = inspect.stack()[1][3]
        # the test file name is passed to getLogger() method to find for which Testcase the log is reported
        testLogFile = logging.getLogger(testFileName)   # logger
        logFileHandler = logging.FileHandler("C:\\Users\\anuj_shukla\\PycharmProjects\\WebAutoFramework\\utilites\\TestLogFile.log") # fileHandler(Log file name)
        logFormatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") # Log Format
        logFileHandler.setFormatter(logFormatter) # link log format to log file
        testLogFile.addHandler(logFileHandler) # link log file to test file
        testLogFile.setLevel(logging.DEBUG)
        return testLogFile

    def checkXpathElementPresent(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        xpathElement = wait.until(E_C.presence_of_element_located((By.XPATH, xpath)))
        return xpathElement

    def selectOptionsByText(self, locator, text):
        dropdown = Select(locator)  # create object of select class , dropdown = Select(find_element_by_xpath or css)
        return dropdown.select_by_visible_text(text)    # performed operation on static dropdown
