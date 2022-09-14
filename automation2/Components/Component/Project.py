from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from Common.logger_until import Logger


class Project:

    def __init__(self, _driver):
        self._log = Logger()
        self._webconfig = WebConfig('Project')
        self._pageobj = self._webconfig.domelements
        self._driver = _driver
        self._findele = DomUntil(_driver).findelement
        self._waiturl = DomUntil(_driver).wait_url

    def get_project(self, project_name):
        try:
            ele = self._findele(self._pageobj['projectList']).find_element_by_link_text(
                project_name)
        except Exception as err:
            self._log.logger_error(err)
            raise err
        return ele

    def visit_project(self, project_name):
        try:
            ele = Project(self._driver).get_project(project_name)
            href = ele.get_attribute("href")
            ele.click()
            result = self._waiturl(href)
            if result:
                self._log.logger(f'Visit project {project_name}')
        except TimeoutError as e:
            raise e and self._log.logger_error(e)

    def username_span(self):
        css = self._pageobj["username_span"]
        ele = self._findele(css)
        return ele



