from Components.Business.Dashboard import BusinessDashboard
from Components.Component.VisibilityLayer.Dashboard.Dashboard import Dashboard
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from Common.logger_until import Logger
from Components.Component.VisibilityLayer.Dashboard.Properties.sort import Common
from time import sleep


class Properties:

    def __init__(self, driver, url, user, pwd, project_name):
        self.visit_dashboard = BusinessDashboard(driver, url, user, pwd, project_name).visit_dashboard
        self.dashboard = Dashboard(driver)
        self.chart_edit = ChartEdit(driver)
        self.log = Logger()
        self.com = Common(driver)

    def bussiness_values(self, dashboard_name, screen_name="", tag_name=None, chart_name=None):
        """
        this function wil leading to project_dashboard_chart_values properties section
        chart_name will be updated in future
        """
        self.visit_dashboard(dashboard_name)
        sleep(1)
        if screen_name == "":
            pass
        else:
            self.dashboard.change_screen(screen_name)
        self.dashboard.single_chart_body_click()
        sleep(1)
        self.dashboard.actiontool_edit_click()
        sleep(1)
        self.log.logger(f"click on properties tab")
        self.chart_edit.properties_tab().click()
        sleep(1)
        # self.com.tab_click(tag_name)
