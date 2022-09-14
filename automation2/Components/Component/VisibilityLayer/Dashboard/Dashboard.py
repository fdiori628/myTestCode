from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from Common.logger_until import Logger
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


class Dashboard(DomUntil):

    def __init__(self, _driver):
        DomUntil.__init__(self, _driver)
        self._log = Logger()
        self._webconfig = WebConfig('Dashboard')
        self._pageobj = self._webconfig.domelements
        self._driver = _driver
        self._findele = DomUntil(_driver).findelement
        self._waiturl = DomUntil(_driver).wait_url
        self.dom = DomUntil(_driver)
        self.common = Common(_driver)

    def dashboard_list(self):
        pass

    def get_dashboard(self, dashboard_name):
        css = self._pageobj['dashboardList']
        try:
            ele = self._findele(css).find_element_by_link_text(
                dashboard_name)
        except Exception as err:
            self._log.logger_error(err)
            raise err
        return ele

    def visit_dashboard(self, dashboard_name):
        try:
            ele = Dashboard(self._driver).get_dashboard(dashboard_name)
            href = ele.get_attribute("href")
            ele.click()
            result = self._waiturl(href)
            if result:
                self._log.logger(f'visit dashboard {dashboard_name}')
        except Exception as err:
            raise err and self._log.logger_error(err)

    def add_chart(self):
        pass

    def single_chart_body(self):
        css = self._pageobj["singleChartBody"]
        try:
            ele = self._findele(css, 15, 1)
            return ele
        except TimeoutError as err:
            raise err and self._log.logger_error(err)
        except Exception as err:
            raise err and self._log.logger_error(err)

    def single_chart_body_click(self):
        try:
            Dashboard(self._driver).single_chart_body().click()
            self._log.logger(f'click on singleChartBody')
        except Exception as err:
            raise err and self._log.logger_error(err)

    def chart_lock(self):
        css = self._pageobj["actionTool"]["lock"]
        ele = self._findele(css)
        return ele

    def chart_lock_status(self):
        ele = self.chart_lock()
        status = ele.get_attribute("aria-label")
        if status == "icon: lock":
            return "lock"
        else:
            return "unlock"

    def actiontool_edit(self):
        css = self._pageobj["actionTool"]["edit"]
        ele = self._findele(css, 15, 1)
        return ele

    def actionTool_drillDown(self):
        css = self._pageobj["actionTool"]["drillDown"]
        ele = self._findele(css, 15, 1)
        return ele

    def pivotTable_drillDown_navBar(self, num):
        """
        :param num: the number of navigation of pivot table
        :return: element (div)
        """
        css = self._pageobj["pivotTable_drillDown_navBar"]
        eles = DomUntil(self._driver).findelements(css)
        return eles[num - 1]

    def pivotTable_drillDown_navContainer(self):
        css = self._pageobj["pivotTable_drillDown_navContainer"]
        ele = DomUntil(self._driver).findelement(css)
        return ele

    def pivotTable_drillDown_nav_currentScreenCheckbox(self):
        allEle = self.pivotTable_drillDown_navContainer().find_elements_by_css_selector("*")
        spanEle = self.dom.contains(allEle, "Current Screen")
        ele = self.dom.previous_ele(spanEle).find_element_by_css_selector("input")
        return ele

    def pivotTable_drillDown_nav_crossScreenCheckbox(self):
        allEle = self.pivotTable_drillDown_navContainer().find_elements_by_css_selector("*")
        spanEle = self.dom.contains(allEle, "Cross Screen")
        ele = self.dom.previous_ele(spanEle).find_element_by_css_selector("input")
        return ele

    def pivotTable_drillDown_nav_eyeNewsScreenCheckbox(self):
        allEle = self.pivotTable_drillDown_navContainer().find_elements_by_css_selector("*")
        spanEle = self.dom.contains(allEle, "EyeNews")
        ele = self.dom.previous_ele(spanEle).find_element_by_css_selector("input")
        return ele

    def pivotTable_drillDown_nav_urlScreenCheckbox(self):
        allEle = self.pivotTable_drillDown_navContainer().find_elements_by_css_selector("*")
        spanEle = self.dom.contains(allEle, "URL")
        ele = self.dom.previous_ele(spanEle).find_element_by_css_selector("input")
        return ele

    def pivotTable_drillDown_screenSetup_container(self):
        css = self._pageobj["pivotTable_drillDown_screenSetup_container"]
        ele = self.findelement(css)
        return ele

    def pivotTable_drillDown_screenSetup_currentScreen_leftBtn(self):
        allEle = self.pivotTable_drillDown_screenSetup_container().find_elements_by_css_selector("*")
        dashboardFilter = self.dom.contains(allEle, "Dashboard Filter")
        chart = self.dom.contains(allEle, "Chart")
        widget = self.dom.contains(allEle, "Widget")
        return {"dashboardFilter": dashboardFilter, "chart": chart, "widget": widget}

    def pivotTable_drillDown_screenSetup_currentScreen_container(self):
        css = self._pageobj["pivotTable_drillDown_screenSetup_currentScreen_container"]
        ele = self.findelement(css)
        return ele

    def pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(self, num):
        dropDownCss = self._pageobj["dropDownCss"]
        eleText = self.pivotTable_drillDown_navBar(num).text[15:]
        allEle = self.pivotTable_drillDown_screenSetup_currentScreen_container().find_elements_by_css_selector("*")
        spanEle = self.contains(allEle, "Exclude itself")
        parEle = self.dom.parentnode(spanEle)
        excludeItselfEle = self.dom.next_ele(parEle).find_element_by_css_selector("button")
        spanEle = self.contains(allEle, eleText)
        preEle = self.dom.previous_ele(spanEle)
        parEle = self.parentnode(spanEle)
        sourceFieldCheckbox = preEle.find_element_by_css_selector("input")
        targetFilterDropDown = parEle.find_element_by_css_selector(dropDownCss)
        return {"excludeItselfEle": excludeItselfEle, "sourceFieldCheckbox": sourceFieldCheckbox,
                "targetFilterDropDown": targetFilterDropDown}

    def pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter_option(self, num):
        dropDown = self.pivotTable_drillDown_screenSetup_currentScreen_dashboardFilter(num)["targetFilterDropDown"]
        options = self.common.get_dropdown_options(dropDown)
        return options

    def pivotTable_drillDown_screenSetup_currentScreen_chart_InputDropDown(self, num=1):
        allEle = self.pivotTable_drillDown_screenSetup_currentScreen_container().find_elements_by_css_selector("*")
        chartInputText = self._pageobj["chartInputText"]
        chartInputDropDown = self.dom.parentnode(self.dom.parentnode(self.dom.contains(allEle, chartInputText)))

        return chartInputDropDown

    def pivotTable_drillDown_screenSetup_currentScreen_chart_InputDropDownOptions(self, num=1):
        dropDown = self.pivotTable_drillDown_screenSetup_currentScreen_chart_InputDropDown(num)
        options = self.common.get_dropdown_options(dropDown)
        return options

    def pivotTable_drillDown_screenSetup_currentScreen_chart_tab(self, num=1, tabText="sameDB"):
        chartTabContainerCss = self._pageobj["chartTabContainerCss"]
        chartTabContainer = self.pivotTable_drillDown_screenSetup_currentScreen_container() \
            .find_elements_by_css_selector(chartTabContainerCss)
        chartTab = self.dom.contains(chartTabContainer, tabText)
        return chartTab

    def pivotTable_drillDown_screenSetup_currentScreen_chart_soucreFieldCheckbox(self, num=1):
        navText = self.pivotTable_drillDown_navBar(num).text[15:]
        allEle = self.pivotTable_drillDown_screenSetup_currentScreen_container().find_elements_by_css_selector("*")
        sourceFieldTextEle = self.dom.contains(allEle, navText)
        sourceFieldCheckbox = self.dom.previous_ele(sourceFieldTextEle).find_element_by_css_selector("input")
        return sourceFieldCheckbox

    # ==============
    def pivotTable_drillDown_screenSetup_currentScreen_chart_targetFieldDropdown(self):
        tempText = "="
        dropDownCss = self._pageobj["dropDownCss"]
        allEle = self.pivotTable_drillDown_screenSetup_currentScreen_container().find_elements_by_css_selector("*")
        equal = self.dom.parentnode(self.dom.contains(allEle, tempText))
        parEle = self.dom.next_ele(equal)
        targetFieldDropdown = parEle.find_element_by_css_selector(dropDownCss)
        return targetFieldDropdown

    def pivotTable_drillDown_screenSetup_currentScreen_chart_targetFieldDropdown_options(self):
        dropDown = self.pivotTable_drillDown_screenSetup_currentScreen_chart_targetFieldDropdown()
        options = self.common.get_dropdown_options(dropDown)
        self._log.logger_debug(
            f"pivotTable_drillDown_screenSetup_currentScreen_chart_targetFieldDropdown_options: {options}")
        return options

    def  pivotTable_drillDown_screenSetup_currentScreen_chart_addInherentFilterBtn(self):
        tempText = "Add Inherent Filter"
        allEle = self.pivotTable_drillDown_screenSetup_currentScreen_container().find_elements_by_css_selector("*")
        tempSpan = self.dom.contains(allEle, tempText)
        targetEle = self.dom.parentnode(tempSpan)
        return targetEle

    def pivotTable_drillDown_screenSetup_currentScreen_chart_inherentDropdown(self, num=1):
        css = self._pageobj["pivotTable_drillDown_screenSetup_currentScreen_chart_inherentDropdown"]
        dropDownCss = self._pageobj["dropDownCss"]
        tempLi = self.dom.findelements(css)
        targetEle = tempLi[num-1].find_element_by_css_selector(dropDownCss)
        return targetEle

    def pivotTable_drillDown_screenSetup_currentScreen_chart_inherentDropdown_options(self, num=1):
        dropDown = self.pivotTable_drillDown_screenSetup_currentScreen_chart_inherentDropdown(num)
        options = self.common.get_dropdown_options(dropDown)
        self._log.logger_debug(
            f"pivotTable_drillDown_screenSetup_currentScreen_chart_inherentDropdown_options: {options}")
        return options

    def pivotTable_drillDown_screenSetup_currentScreen_chart_inherentDelBtn(self, num=1):
        css = self._pageobj["pivotTable_drillDown_screenSetup_currentScreen_chart_inherentDropdown"]
        tempLi = self.dom.findelements(css)
        targetEle = tempLi[num-1].find_element_by_css_selector("button")
        return targetEle



    def actiontool_edit_click(self):
        lock_status = self.chart_lock_status()
        if lock_status == "lock":
            self.chart_lock().click()
            Dashboard(self._driver).actiontool_edit().click()
            self._log.logger(f'click on actiontool_edit_click btn')
        else:
            Dashboard(self._driver).actiontool_edit().click()
            self._log.logger(f'click on actiontool_edit_click btn')

    def change_screen(self, screen_name):
        screen_css = self._pageobj["screen"]
        self._log.logger_debug("这个值是{}".format(self.findelements(screen_css)))
        screen_css = self.contains(self.findelements(screen_css), screen_name)
        self._log.logger_debug("这个值是{}".format(screen_css))
        screen_css.click()
