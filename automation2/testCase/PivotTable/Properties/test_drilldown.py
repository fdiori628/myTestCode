import inspect
import pytest
from Common.web_config_until import WebConfig
from Components.Business.Dashboard import BusinessDashboard
from Components.Component.VisibilityLayer.Dashboard.Dashboard import Dashboard
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from Components.Component.VisibilityLayer.Dashboard.Properties.navigation import Navigation
from time import sleep
from Common.logger_until import Logger
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common
from Common.dom_until import DomUntil


class TestNavigation:
    """
    marker=
    smoke: marks tests as smoke
    critical: marks tests as critical
    high: marks tests as high
    mid: marks tests as mid
    low: marks tests as low

    """

    @pytest.fixture(scope="class", autouse=True)
    def init(self, driver):
        TestNavigation.config = WebConfig('Properties_common/navigation')
        TestNavigation.env = "ADG"
        # when running with execution file, env should be set to Execute
        # env = "Execute"
        TestNavigation.logger = Logger()
        TestNavigation.pageobj = self.config.domelements
        TestNavigation.nav = Navigation(driver)
        TestNavigation.dashboard = Dashboard(driver)
        TestNavigation.chart_edit = ChartEdit(driver)
        TestNavigation.prop_common = Common(driver)
        TestNavigation.Dom_until = DomUntil(driver)

    @pytest.fixture(scope="class", autouse=True)
    def visit_dashboard(self, driver):
        try:
            env_info = self.config.get_env_info(self.env)
            url = env_info["url"]
            user = env_info["userName"]
            pwd = env_info["passWord"]
            project_name = env_info["project_name"]
            dashboard_name = env_info["dashboard_name"]
            self.logger.logger(
                "===================values testing STEUP started==============================================")
            bussiness_dashboard = BusinessDashboard(driver, url, user, pwd, project_name)
            self.logger.logger(f"visit dashboard: {dashboard_name}")
            bussiness_dashboard.visit_dashboard(dashboard_name)
        except Exception as e:
            self.logger.logger_error(e)
            raise TimeoutError("visit dashboard setup Error, please find screen shot")

    @pytest.fixture(scope="function")
    def properties_op(self):
        try:
            self.dashboard.single_chart_body_click()
            self.dashboard.actiontool_edit_click()
            self.chart_edit.properties_tab().click()
            self.nav.nav_tab_click()
            sleep(2)
            yield
        except Exception as e:
            self.logger.logger_error(e)
            raise TimeoutError("Navigation setup Error, please find screen shot")
        finally:
            self.chart_edit.close().click()
            sleep(2)

    def handle_assert(self, actually_result, expected_result):
        self.logger.logger(f"expected value: {expected_result}, actually_result: {actually_result}")
        if actually_result != expected_result:
            # "get screen shot ========================"
            self.logger.logger(f"screenShot has been done in path")
            raise AssertionError(f"{actually_result} != {expected_result}") and self.logger.logger_error(
                AssertionError)
        else:
            assert actually_result == expected_result
            self.logger.logger(f"testing {inspect.stack()[1][3]} is completed and passed")

    def handle_expectedresult(self):
        tcname = inspect.stack()[1][3]
        expected_result = self.config.testdata["test_data"]["expected_result"][tcname]
        return expected_result

    def handle_navSetup(self, navNum=1, navType="Row Headers", navField="item"):
        navType = navType
        navField = navField
        self.logger.logger("click on type dropdown list")
        self.nav.nav_typeDropDown(navNum - 1).click()
        sleep(1)
        self.logger.logger(f"select {navType}")
        self.nav.nav_typeDropDown_options(navNum - 1)[navType].click()
        sleep(1)
        self.logger.logger("click on field dropdown list")
        self.nav.nav_fieldDropDown(navNum - 1).click()
        sleep(1)
        self.logger.logger(f"select {navField}")
        self.nav.nav_fieldDropDown_options(navNum - 1)[navField].click()

    def handle_navResult(self):
        sleep(2)
        divCss = self.pageobj["viewScreenDivResult"]
        result = []
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        for i in range(2, 9):
            targetEle = view_screen[i][0].find_element_by_css_selector(divCss)
            color = self.Dom_until.get_style(targetEle, "color")
            testStyle = self.Dom_until.get_style(targetEle, "textDecoration")
            result.append((color, testStyle))
        return result

    @pytest.mark.smoke
    def test_navSetup(self, properties_op):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.logger.logger("click on Create New button")
        sleep(1)
        self.nav.nav_createNewBtn().click()
        sleep(2)
        self.handle_navSetup()
        actually_result = str(self.handle_navResult())
        expect_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expect_result)

    def nav_visitScreen(self, screenName):
        sleep(2)
        self.dashboard.change_screen(screenName)

    @pytest.mark.smoke
    def test_navDrillDown_currentScreen_dashBoardFilter(self):
        self.nav_visitScreen("pivotTable_drilldown")
        sleep(1)
        self.dashboard.single_chart_body_click()
        sleep(1)
        self.dashboard.actionTool_drillDown().click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_nav_currentScreenCheckbox().click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(1)["excludeItselfEle"].click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(1)["sourceFieldCheckbox"].click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(1)["targetFilterDropDown"].click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter_option(1)[
            "dashboardFilter"].click()

    @pytest.mark.smoke
    def test_navDrillDown_currentScreen_chart(self):
        self.nav_visitScreen("pivotTable_drilldown")
        sleep(1)
        self.dashboard.single_chart_body_click()
        sleep(1)
        self.dashboard.actionTool_drillDown().click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_nav_currentScreenCheckbox().click()
        sleep(1)
        # self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(1)["excludeItselfEle"].click()
        # sleep(1)
        # self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(1)["sourceFieldCheckbox"].click()
        # sleep(1)
        # self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(1)["targetFilterDropDown"].click()
        # sleep(1)
        # self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter_option(1)["dashboardFilter"].click()
        # sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_leftBtn()["chart"].click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_chart_InputDropDown().click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_chart_InputDropDownOptions()["sameDB"].click()
        sleep(1)
        self.dashboard.pivotTable_drillDown_screenSetup_currentScreen_chart_soucreFieldCheckbox().click()

        sleep(10)
