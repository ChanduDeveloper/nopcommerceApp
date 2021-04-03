from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver")
        print("Launching chrome browser...................")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Drivers/geckodriver-v0.29.0-win64/geckodriver")
        print("Launching Firefox browser......................")
    else:
        driver = webdriver.Chrome(executable_path="C:/Drivers/IEDriverServer_Win32_3.150.1/IEDriverServer")
    return driver

def pytest_addoption(parser):    #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       #This will return the Browser value to setup method
    return request.config.getoption("--browser")


################################# PyTest HTML Report #################################3
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

#It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)



















