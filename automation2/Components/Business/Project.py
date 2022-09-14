from Components.Component.Project import *
# from Login import BusinessLogin

from Components.Business.Login import BusinessLogin


class BusinessProject:

    def __init__(self, driver, url, username, pwd):
        self.driver = driver
        self.project = Project(driver)
        BusinessLogin(driver, url, username, pwd).login()

    def visit_project(self, project_name):
        self.project.visit_project(project_name)
