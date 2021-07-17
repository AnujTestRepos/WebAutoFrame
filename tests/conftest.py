# In this file we define all the fixtures used for testcases.
# To run the test on browser of user choice from terminal, we have to create a hook(cmdopt) and
# Pass different values to a test function, depending on command line options using pytest_addoption() method

import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="my options : chrome or firefox or Edge")
    parser.addoption("--site_url", action="store", default="testUrl", help="UrlOptions : testUrl and prodUrl")


@pytest.fixture(scope='class')
def setup(request):
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    firefox_option = webdriver.FirefoxOptions()
    firefox_option.add_argument("--start-maximized")

    # now here we will link hook(command line arg method to fixture)
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\anuj_shukla\\PycharmProjects"
                                                  "\\LearnPyhtonSelenium_RahulShetty\\chromedriver_win32"
                                                  "\\chromedriver.exe",
                                  options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\anuj_shukla\\PycharmProjects\\geckodriver-v0.29.1"
                                                   "-win64\\geckodriver.exe", options=firefox_option)

    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path='C:\\Users\\anuj_shukla\\PycharmProjects'
                                                '\\LearnPyhtonSelenium_RahulShetty\\edgedriver_win64\\msedgedriver.exe')

    url_option = request.config.getoption("--site_url")
    if url_option == 'testUrl':
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif url_option == 'prodUrl':
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    driver.maximize_window()

    # This 'request' instance will return the local diver object to class object(cls.driver)
    # and with the help of request we can achieve to run the code after yield
    request.cls.driver = driver
    yield
    driver.close()


#     This Pytest annotation wil help us to capture screenshot at failure of testcase
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
