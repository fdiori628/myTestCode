import time

from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from Common.logger_until import Logger


class ChartEdit:

    def __init__(self, _driver):
        self._log = Logger()
        self._webconfig = WebConfig('ChartEdit')
        self._pageobj = self._webconfig.domelements
        self._driver = _driver
        self._findele = DomUntil(_driver).findelement
        self._findeles = DomUntil(_driver).findelements
        self._waiturl = DomUntil(_driver).wait_url

    def dataset(self):
        pass

    def dimensions(self, name):
        try:
            css = self._pageobj['dimensions_container']
            dimensions_container = self._findeles(css)
            dimensions_arr = dimensions_container[1].find_elements_by_css_selector("span")
            for i in dimensions_arr:
                if i.text == name:
                    return i
        except Exception as err:
            raise err and self._log.logger_error(err)

    def measures(self, name):
        try:
            css = self._pageobj['measures_container']
            measures_container = self._findele(css)
            measures_arr = measures_container.find_elements_by_css_selector("span")
            for i in measures_arr:
                if i.text == name:
                    return i
        except Exception as err:
            raise err and self._log.logger_error(err)

    def derivedfield_add(self):
        pass

    def filters(self):
        pass

    def columns(self):
        pass

    def rows(self):
        pass

    def coldrilldown(self):
        pass

    def rowdrilldown(self):
        pass

    def values(self):
        pass

    def dimensions_tab(self):
        pass

    def properties_tab(self):
        try:
            css = self._pageobj['properties_tab']
            ele = self._findele(css)
            return ele
        except Exception as err:
            raise err and self._log.logger_error(err)

    def properties_select(self, name):
        try:
            css = ".ant-collapse>div"
            eles = self._findeles(css)
            for i in eles:
                if i.text == name:
                    return i
        except Exception as err:
            raise err and self._log.logger_error(err)

    def view_screen(self, chart_name):
        """

        :param chart_name: chartname, eg: pivottable, bar, ......
        :return: pivottable: [][]
        if user wants to get the 1st row 3rd col value:  view_screen("pivottable")[0][2]
        """
        time.sleep(2)
        table = []
        table_ele = []
        if chart_name == 'pivottable':
            tr_css = self._pageobj["pivot_table_viewScreen_tr"]
            table_row_org = self._findeles(tr_css)
            for tr in table_row_org:
                tds = tr.find_elements_by_css_selector("td")
                td_text = []
                for td in tds:
                    if td.text != '':
                        td_text.append(td.text)
                    else:
                        continue
                table.append(td_text)
                table_ele.append(tds)
        return table, table_ele

    def save_btn(self):
        pass

    def save_as_library(self):
        pass

    def visualize_as(self):
        pass

    def close(self):
        css = self._pageobj["X"]
        ele = self._findeles(css)
        return ele[0]
