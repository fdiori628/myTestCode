from Components.Component.VisibilityLayer.Dashboard.Dashboard import *
from Components.Business.Project import BusinessProject


class BusinessDashboard:

    def __init__(self, driver, url, username, pwd, project_name):
        self.driver = driver
        self.project = BusinessProject(driver, url, username, pwd).visit_project(project_name)
        self.dashboard = Dashboard(driver)

    def visit_dashboard(self, dashboard_name):
        self.dashboard.visit_dashboard(dashboard_name)
