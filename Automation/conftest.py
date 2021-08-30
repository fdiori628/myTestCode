import time
import pytest
from selenium import webdriver
from Common.web_config_until import WebConfig

t = time.strftime("%Y-%m-%d %H:%M:%S")
driver_path = WebConfig('driver').get_appinfo()['Driver']


@pytest.fixture(scope='function')
def con_database():
    print('connecting database  %s' % t)
    con_id = 1
    return con_id


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen = _capture_screenshot()
            extra.append(pytest_html.extras.png(screen))
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


def _capture_screenshot():
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session')
def driver():
    global driver
    driver = webdriver.Chrome(driver_path)
    return driver


# @pytest.fixture(scope='session', autouse=True)
# def driverm1():
#     global driver
#     driver = webdriver.Chrome(driverM1_path)
#     return driver
#

@pytest.fixture(scope='session')
def driver_headless():
    global driver
    caps = {"pageLoadStrategy": "eager"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(desired_capabilities=caps, executable_path=driver_path, options=chrome_options)
    return driver
