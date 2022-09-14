import time
import pytest
from selenium import webdriver
from Components.Component.VisibilityLayer.Dashboard.Dashboard import Dashboard
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from Components.Component.Project import Project
from Common.web_config_until import WebConfig
from Components.Business.Login import BusinessLogin
from Common.yaml_until import YamlUtil
from Common.dom_until import DomUntil
from Common.root_until import RootUntil

t = time.strftime("%Y-%m-%d %H:%M:%S")
driver_path = WebConfig('driver').get_appinfo()['Driver']
root = RootUntil()
url = YamlUtil(root.get_rootpath + "/Components/Business/config.yml").read_single_yml_name("url")
user = YamlUtil(root.get_rootpath + "/Components/Business/config.yml").read_single_yml_name("user")
pwd = YamlUtil(root.get_rootpath + "/Components/Business/config.yml").read_single_yml_name("pwd")
X = YamlUtil(root.get_rootpath + '/Resource/ChartEdit/dom_element.yaml').read_single_yml_name("X")
d = webdriver.Chrome(driver_path)
# @pytest.fixture(scope='session')
# def conn_database():
#     # conn = DataBaseUntil().mysql()
#     # ......
#     print('connecting database  %s' % t)
#     con_id = 1
#     return con_id


@pytest.fixture(scope='session')
def driver():
    yield d
    d.quit()


@pytest.fixture(scope='class')
def login(driver):
    BusinessLogin(driver=driver, url=url, username=user, pwd=pwd).login()
    return driver


@pytest.fixture(scope="class")
def pivtable(login):
    dashboard = Dashboard(_driver=login)
    chartedit = ChartEdit(_driver=login)
    project = Project(_driver=login)
    project.visit_project("AutomationTest")
    dashboard.visit_dashboard("Automation_visibilityLayer_pivotTable")
    time.sleep(1)
    dashboard.single_chart_body_click()
    time.sleep(1)
    dashboard.actiontool_edit_click()
    time.sleep(1)
    chartedit.properties_tab().click()
    yield login
    login.quit()


@pytest.fixture(scope="function")
def pivtable_handle_case(driver):
    yield driver
    dashboard = Dashboard(_driver=driver)
    chartedit = ChartEdit(_driver=driver)
    domutill = DomUntil(driver)
    time.sleep(6)
    domutill.findelements(X)[0].click()
    dashboard.single_chart_body_click()
    time.sleep(1)
    dashboard.actiontool_edit_click()
    time.sleep(1)
    chartedit.properties_tab().click()
    time.sleep(1)


#  ..... different version of driver


# @pytest.fixture(scope='class')
# def driver_headless():
#     global driver
#     caps = {"pageLoadStrategy": "eager"}
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(desired_capabilities=caps, executable_path=driver_path, options=chrome_options)
#     return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'setup':
        if report.failed:
            screen = _capture_screenshot()
            extra.append(pytest_html.extras.png(screen))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen = _capture_screenshot()
            extra.append(pytest_html.extras.png(screen))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


def _capture_screenshot():
    return d.get_screenshot_as_base64()
