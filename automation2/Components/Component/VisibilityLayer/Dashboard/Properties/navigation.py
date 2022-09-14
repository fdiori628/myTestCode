from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from Common.logger_until import Logger
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from time import sleep
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


class Navigation:

    def __init__(self, _driver):
        self._log = Logger()
        self._webconfig = WebConfig('Properties_common/navigation')
        self._pageobj = self._webconfig.domelements
        self.dom = DomUntil(_driver)
        self.CharEdit = ChartEdit(_driver)
        self.common = Common(_driver)

    def nav_all(self):
        """
        find all eles in values component
        :return: elements
        """
        css_all = self._pageobj['all_elements']
        eles = self.dom.findelements(css_all)
        return eles

    def nav_tab_click(self):
        """
        click on Navigation section
        usage: nav_tab_click()
        :return: action
        """
        try:
            ele = self.CharEdit.properties_select('Navigation')
            self._log.logger(f'click on Navigation section')
            ele.click()
        except Exception as err:
            raise err and self._log.logger_error(err)

    def nav_customizeStyle(self):
        pass

    def nav_createNewBtn(self):
        allEle = self.nav_all()
        tempEle = self.dom.contains(allEle, "Create New")
        ele = self.dom.parentnode(tempEle)
        return ele

    def nav_typeDropDown(self, navNum):
        dropDownCss = self._pageobj["dropDown"]
        allEle = self.nav_all()
        tempEle = self.dom.containsAll(allEle, "Type")[navNum]
        tempEle_par = self.dom.parentnode(tempEle)
        tempChild = self.dom.next_ele(tempEle_par)
        ele = tempChild.find_element_by_css_selector(dropDownCss)
        return ele

    def nav_typeDropDown_options(self, navNum):
        dropDown = self.nav_typeDropDown(navNum)
        options = self.common.get_dropdown_options(dropDown)
        return options

    def nav_fieldDropDown(self, navNum):
        dropDownCss = self._pageobj["dropDown"]
        allEle = self.nav_all()
        tempEle = self.dom.containsAll(allEle, "Field")[navNum]
        tempEle_par = self.dom.parentnode(tempEle)
        tempChild = self.dom.next_ele(tempEle_par)
        ele = tempChild.find_element_by_css_selector(dropDownCss)
        return ele

    def nav_fieldDropDown_options(self, navNum):
        dropDown = self.nav_fieldDropDown(navNum)
        options = self.common.get_dropdown_options(dropDown)
        return options
