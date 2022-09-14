import inspect
import pytest
from Common.web_config_until import WebConfig
from Components.Business.Dashboard import BusinessDashboard
from Components.Component.VisibilityLayer.Dashboard.Dashboard import Dashboard
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from Components.Component.VisibilityLayer.Dashboard.Properties.values import Values
from time import sleep
from Common.logger_until import Logger
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common
from Common.dom_until import DomUntil
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestValues:
    """
    marker=
    smoke: marks tests as smoke
    critical: marks tests as critical
    high: marks tests as high
    mid: marks tests as mid
    low: marks tests as low

    cast count: 94
    """

    @pytest.fixture(scope="class", autouse=True)
    def init(self, driver):
        TestValues.config = WebConfig('Properties_common/values')
        TestValues.env = "Staging"
        # when running with execution file, env should be set to Execute
        # env = "Execute"
        TestValues.logger = Logger()
        TestValues.pageobj = self.config.domelements
        TestValues.values = Values(driver)
        TestValues.dashboard = Dashboard(driver)
        TestValues.chart_edit = ChartEdit(driver)
        TestValues.prop_common = Common(driver)
        TestValues.Dom_until = DomUntil(driver)

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

    @pytest.fixture(scope="function", autouse=True)
    def properties_op(self):
        try:
            self.dashboard.single_chart_body_click()
            self.dashboard.actiontool_edit_click()
            self.chart_edit.properties_tab().click()
            self.values.values_tab_click()
            sleep(2)
            yield
        except Exception as e:
            self.logger.logger_error(e)
            raise TimeoutError("Values setup Error, please find screen shot")
        finally:
            self.chart_edit.close().click()
            sleep(2)

    def handle_viewscreen(self):
        # use in test_value_bar_types_var_sum, var_.....
        try:
            self.logger.logger("getting test result")
            target_arr = []
            _actually_sum = []
            # waiting for data update in view_screen
            sleep(3)
            view_screen = self.chart_edit.view_screen("pivottable")[1]
            # self.logger.logger(view_screen)
            for i in range(2, 9):
                for j in range(1, 9, 3):
                    if j > 9:
                        break
                    target_arr.append(view_screen[i][j])
            target_arr = target_arr[:19]
            for t in target_arr:
                _t = t.find_element_by_css_selector("span")
                bcg = self.Dom_until.get_style(_t, "backgroundColor")
                _actually_sum.append(bcg)
            return _actually_sum
        except Exception as e:
            self.logger.logger_error(e)
            return []

    def handle_condition_dropdown(self, indicator):
        # use in test_value_bar_types_var_sum, var_.....
        # indicator = 1,2,3,4 (< = >= <=)
        indicator = int(indicator)
        self.logger.logger("click on condition drop down list")
        self.values.view_as_bar_controls_component(1)["condition"].click()
        sleep(1)
        self.values.view_as_bar_controls_condition_options(1)[indicator].click()
        sleep(2)

    def handle_viewas(self, view_as, _values_options):
        self.logger.logger("click on Values dropdown")
        self.values.values().click()
        sleep(1)
        # 'sales_count(sum)'
        values_options = _values_options
        self.logger.logger(f"click on options: {values_options}")
        self.values.values_options()[values_options].click()
        self.logger.logger(f"click on view As drop-down")
        self.values.view_as().click()
        sleep(1)
        self.logger.logger(f"click on the options: {view_as}")
        self.values.view_as_options()[view_as].click()
        sleep(1)

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

    def handle_value_bar_variables_agg(self, agg):
        self.handle_viewas("Bar", "sales_count(sum)")
        actually_result = []
        self.logger.logger("click on types dropdown list")
        self.values.view_as_bar()["types_dropdown"].click()
        sleep(1)
        self.logger.logger("select variables types")
        self.values.view_as_bar_types_options()[1].click()
        sleep(1)
        self.values.view_as_addnew_btn().click()
        sleep(1)
        self.logger.logger("click on color picker")
        self.values.view_as_bar_controls_component(1)["color_picker"].click()
        sleep(1)
        color = "#417505"
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        self.logger.logger("close color picker")
        self.values.view_as_bar_controls_component(1)["color_picker"].click()
        self.logger.logger("click on condition drop down list")
        self.values.view_as_bar_controls_component(1)["condition"].click()
        sleep(1)
        self.values.view_as_bar_controls_condition_options(1)[0].click()
        sleep(1)
        self.values.view_as_bar_controls_component(1)["var_dropdown"].click()
        sleep(1)
        target_field = "target_count"
        self.values.view_as_bar_controls_var_targetfield_options(1)[target_field].click()
        sleep(1)
        self.logger.logger("click on aggregation drop down list")
        self.values.view_as_bar_controls_var_aggregation().click()
        sleep(1)
        self.logger.logger(f"select {agg} for aggregation")
        self.values.view_as_bar_controls_var_aggregation_options()[agg].click()
        sleep(2)
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + <")
        self.logger.logger("select < for condition")
        self.handle_condition_dropdown(1)
        sleep(2)
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + =")
        self.logger.logger("select = for condition")
        self.handle_condition_dropdown(2)
        sleep(2)
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + >=")
        self.logger.logger("select >= for condition")
        self.handle_condition_dropdown(3)
        sleep(2)
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + <=")
        self.logger.logger("select <= for condition")
        self.handle_condition_dropdown(4)
        sleep(2)
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        return actually_result

    def handle_value_bar_variables_allowtoggle_agg(self, agg):
        self.handle_viewas("Bar", "sales_count(sum)")
        actually_result = []
        self.logger.logger("click on types dropdown list")
        self.values.view_as_bar()["types_dropdown"].click()
        sleep(1)
        self.logger.logger("select variables types")
        self.values.view_as_bar_types_options()[1].click()
        sleep(1)
        self.values.view_as_addnew_btn().click()
        sleep(1)
        self.logger.logger("click on color picker")
        self.values.view_as_bar_controls_component(1)["color_picker"].click()
        sleep(1)
        color = "#417505"
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        self.logger.logger("close color picker")
        self.values.view_as_bar_controls_component(1)["color_picker"].click()
        self.logger.logger("click on condition drop down list")
        self.values.view_as_bar_controls_component(1)["condition"].click()
        sleep(1)
        self.values.view_as_bar_controls_condition_options(1)[0].click()
        sleep(1)
        self.values.view_as_bar_controls_component(1)["var_dropdown"].click()
        sleep(1)
        target_field = "sales_count"
        self.values.view_as_bar_controls_var_targetfield_options(1)[target_field].click()
        sleep(1)
        self.logger.logger("click on aggregation drop down list")
        self.values.view_as_bar_controls_var_aggregation().click()
        sleep(1)
        self.logger.logger(f"select {agg} for aggregation")
        self.values.view_as_bar_controls_var_aggregation_options()[agg].click()
        sleep(2)
        self.logger.logger(f"start testing {agg} + >")
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + <")
        self.logger.logger("select < for condition")
        self.handle_condition_dropdown(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + =")
        self.logger.logger("select = for condition")
        self.handle_condition_dropdown(2)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + >=")
        self.logger.logger("select >= for condition")
        self.handle_condition_dropdown(3)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        self.logger.logger(f"start testing {agg} + <=")
        self.logger.logger("select <= for condition")
        self.handle_condition_dropdown(4)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        actually_sum = self.handle_viewscreen()
        actually_result.append(actually_sum)
        return actually_result

    def handle_bar_unitconversions(self):
        self.handle_viewas("Bar", "target_count(sum)")
        self.logger.logger("click on display value toggle")
        self.values.view_as_bar_displayvalue().click()

    def handld_value_indicator_values(self, value, num=1, indicator=0, condition=">", color="#417505"):
        """
        :param num: number of controls
        :param indicator: 0 or 1
        :param color: #...
        :param condition: <, > ,= ....
        :param value: int
        :return: actions
        """
        self.handle_viewas("Indicator", "sales_count(sum)")
        self.logger.logger("click on add button")
        self.values.view_as_add_btn().click()
        sleep(2)
        self.logger.logger("click on indicator style")
        self.values.view_as_indicator_control_styledropdown(num).click()
        sleep(1)
        self.logger.logger("click up for indicatior")
        self.values.view_as_indicator_control_styledropdown_options(num)[indicator].click()
        self.logger.logger("click on color picker component")
        self.values.view_as_indicator_control_colorpicker(num).click()
        sleep(1)
        self.prop_common.sketch_picker(color)[num - 1].click()
        self.logger.logger("click condition dropdown list")
        self.values.view_as_indicator_control_condition(num).click()
        sleep(1)
        self.logger.logger("select > for condition")
        self.values.view_as_indicator_control_condition_options(num)[condition].click()
        self.logger.logger(f"input {value} for control input")
        self.Dom_until.dely_input(self.values.view_as_indicator_control_input(num), value)

    @pytest.mark.mid
    def test_hide_value_headers(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.logger.logger(f"click on Hide value headers toggle")
        self.values.hide_value_headers().click()
        self.logger.logger(f"verify the value header is hiding...")
        # waiting for table data updating
        sleep(1)
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[0][0]
        expected_result = "item"
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_header_border(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.logger.logger("click on value header border dropdown element")
        options_org = self.values.value_header_border_options().keys()
        actually_result = list(options_org)
        self.logger.logger("verify the border options is correct")
        expected_result = ['Apr', 'Jan', 'Mar']
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_header_border_del(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.logger.logger("click on delete icon for existed header border")
        self.values.value_header_border_setting_innerdel().click()
        sleep(1)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[1][1]
        target_style = target_ele.get_attribute('style')
        if "border-left" in target_style:
            # "get screen shot ========================"
            self.logger.logger(f"screenShot has been done in path")
            raise AssertionError and self.logger.logger_error(AssertionError)
        else:
            assert "border-left" not in target_style, "border-right" not in target_style
            self.logger.logger(f"testing {inspect.stack()[0][3]} is completed and passed")

    @pytest.mark.mid
    def test_value_header_border_close(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.logger.logger("click on close icon for existed header border")
        self.values.value_header_border_delete().click()
        sleep(1)
        border_options = self.values.value_header_border().find_elements_by_css_selector("li")
        actually_result = len(border_options)
        expected_result = 1
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_emptycell(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        input_text = "emptyvalue"
        self.logger.logger(f"input text into Expty Cell Value field: {input_text}")
        input_ele = self.values.empty_cell_value()
        input_ele.clear()
        self.Dom_until.dely_input(input_ele, input_text, 1)
        sleep(1)
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[8][2]
        expected_indicator = input_text
        self.handle_assert(actually_result, expected_indicator)

    @pytest.mark.smoke
    def test_valueas_bar_basefunc(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Bar", "sales_count(sum)")
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][1].find_element_by_css_selector("div:nth-child(1)")
        actually_result = target_ele.get_attribute("class")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_valueas_bar_barcolor(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Bar", "sales_count(sum)")
        sleep(1)
        self.logger.logger(f"click on Bar Color picker")
        self.values.view_as_bar()["bar_color_btn"].click()
        color = "#417505"
        self.logger.logger(f"click on color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        self.logger.logger(f"close the color picker")
        self.values.view_as_bar()["bar_color_btn"].click()
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][1].find_element_by_css_selector("span")
        indicator = target_ele.get_attribute("style")
        expected_indicator = "background-color: rgb(65, 117, 5)"
        self.logger.logger(f"expected_indicator: {expected_indicator}, actually_indicator: {indicator}")
        if expected_indicator not in indicator:
            # "get screen shot ========================"
            self.logger.logger(f"screenShot has been done in path")
            raise AssertionError(f"{expected_indicator} not in {indicator}") and self.logger.logger_error(
                AssertionError)
        else:
            assert expected_indicator in indicator
            self.logger.logger(f"testing {inspect.stack()[0][3]} is completed and passed")

    # @pytest.mark.high
    # def test_valueas_bar_displaymode(self):
    #     self.logger.logger(f"Starting test TC {self.test_valueas_bar_displaymode.__name__}")
    #     self.logger.logger("click on Values dropdown")
    #     self.values.values().click()
    #     sleep(1)
    #     values_options = 'sales_count(sum)'
    #     view_as = "Bar"
    #     self.logger.logger(f"click on options: {values_options}")
    #     self.values.values_options()[values_options].click()
    #     self.logger.logger(f"click on view As drop-down")
    #     self.values.view_as().click()
    #     sleep(1)
    #     self.logger.logger(f"click on the options: {view_as}")
    #     self.values.view_as_options()['Bar'].click()
    #     sleep(1)
    #     self.logger.logger(f"click on display value toggle")
    #     self.values.view_as_bar_displayvalue().click()
    #     self.logger.logger(f"click on show percent of total")
    #     self.values.show_percent_total().click()
    #     sleep(1)
    #     self.logger.logger(f"click on display mode toggle")
    #     self.values.view_as_bar()["display_mode_toggle"].click()
    #     sleep(2)
    #     view_screen = self.chart_edit.view_screen("pivottable")[0]
    #     indicator = view_screen[4][1]
    #     expected_indicator = "25.76"
    #     self.logger.logger(f"expected_indicator: {expected_indicator}, actually_indicator: {indicator}")
    #     if expected_indicator != indicator:
    #         # "get screen shot ========================"
    #         self.logger.logger(f"screenShot has been done in path")
    #         raise AssertionError(f"{expected_indicator} != {indicator}") and self.logger.logger_error(
    #             AssertionError)
    #     else:
    #         assert expected_indicator == indicator
    #         self.logger.logger(f"testcase //{self.test_valueas_bar_displaymode.__name__}// is completed and passed")

    @pytest.mark.mid
    def test_valueas_bar_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Bar", "sales_count(sum)")
        target_result = []
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[8][1].find_element_by_css_selector("span")
        target_default = self.Dom_until.get_style(target_ele, "width")
        self.logger.logger(f"get min (default) bar width: {target_default}")
        target_result.append(target_default)
        self.logger.logger(f"click on Min drop-down list")
        self.values.view_as_bar()["min_dropdown"].click()
        sleep(1)
        self.logger.logger("select - 100% for min")
        self.values.view_as_bar_min_options()[1].click()
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[8][1].find_element_by_css_selector("span")
        target_default = self.Dom_until.get_style(target_ele, "width")
        self.logger.logger(f"get -100% bar width: {target_default}")
        target_result.append(target_default)
        self.logger.logger(f"click on Min drop-down list")
        self.values.view_as_bar()["min_dropdown"].click()
        sleep(1)
        self.logger.logger("select 0 for min")
        self.values.view_as_bar_min_options()[2].click()
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[8][1].find_element_by_css_selector("span")
        target_default = self.Dom_until.get_style(target_ele, "width")
        self.logger.logger(f"get -100% bar width: {target_default}")
        target_result.append(target_default)
        expected_result = self.handle_expectedresult()
        self.handle_assert(target_result, expected_result)

    @pytest.mark.mid
    def test_valueas_bar_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Bar", "sales_count(sum)")
        target_result = []
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[8][1].find_element_by_css_selector("span")
        target_default = self.Dom_until.get_style(target_ele, "width")
        self.logger.logger(f"get min (default) bar width: {target_default}")
        target_result.append(target_default)
        self.logger.logger(f"click on Max drop-down list")
        self.values.view_as_bar()["max_dropdown"].click()
        sleep(1)
        self.logger.logger("select 0 for max")
        self.values.view_as_bar_max_options()[1].click()
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[8][1].find_element_by_css_selector("span")
        target_default = self.Dom_until.get_style(target_ele, "width")
        self.logger.logger(f"get 0 bar max width: {target_default}")
        target_result.append(target_default)
        self.logger.logger(f"click on Max drop-down list")
        self.values.view_as_bar()["max_dropdown"].click()
        sleep(1)
        self.logger.logger("select 100% for max")
        self.values.view_as_bar_max_options()[2].click()
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[8][1].find_element_by_css_selector("span")
        target_default = self.Dom_until.get_style(target_ele, "width")
        self.logger.logger(f"get 100% bar max width: {target_default}")
        target_result.append(target_default)
        self.logger.logger(target_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(target_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_types_values(self):
        # will do refactor in future
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Bar", "sales_count(sum)")
        actually_result = []
        self.logger.logger("click on Add New button")
        self.values.view_as_bar()["addnew_btn"].click()
        sleep(1)
        self.logger.logger("click on color picker")
        self.values.view_as_bar_controls_component(1)["color_picker"].click()
        sleep(1)
        color = "#417505"
        self.logger.logger(f"click on color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        sleep(1)
        input_num = "210"
        self.logger.logger(f"input {input_num} to conditions value")
        input_ele = self.values.view_as_bar_controls_component(1)["value"]
        self.Dom_until.dely_input(input_ele, input_num)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        sleep(2)
        temp = view_screen[2][1].find_element_by_css_selector("span")
        temp2 = view_screen[2][1].find_element_by_css_selector("span")
        result_morethan = self.Dom_until.get_style(temp, "backgroundColor")
        result_morethan_effect = self.Dom_until.get_style(temp2, "backgroundColor")
        actually_result.append((result_morethan, result_morethan_effect))
        self.logger.logger(f"actually result: {actually_result}")
        sleep(1)
        self.logger.logger("click on control_condition drop down")
        condition_dropdown = self.values.view_as_bar_controls_component(1)["condition"]
        condition_dropdown.click()
        sleep(1)
        lessthan_indicator = self.values.view_as_bar_controls_condition_options(1)[1]
        self.logger.logger("select condition as <")
        lessthan_indicator.click()
        sleep(1)
        view_screen[0][0].click()
        sleep(2)
        temp = view_screen[2][1].find_element_by_css_selector("span")
        temp2 = view_screen[8][1].find_element_by_css_selector("span")
        result_lessthan = self.Dom_until.get_style(temp, "backgroundColor")
        result_lessthan_effect = self.Dom_until.get_style(temp2, "backgroundColor")
        actually_result.append((result_lessthan, result_lessthan_effect))
        self.logger.logger(f"actually result: {actually_result}")
        sleep(1)
        self.logger.logger("click on control_condition drop down")
        condition_dropdown = self.values.view_as_bar_controls_component(1)["condition"]
        condition_dropdown.click()
        sleep(1)
        equal_indicator = self.values.view_as_bar_controls_condition_options(1)[2]
        self.logger.logger("select condition as =")
        equal_indicator.click()
        sleep(1)
        view_screen[0][0].click()
        sleep(2)
        temp = view_screen[2][1].find_element_by_css_selector("span")
        temp2 = view_screen[8][1].find_element_by_css_selector("span")
        result_equal = self.Dom_until.get_style(temp, "backgroundColor")
        result_equal_effect = self.Dom_until.get_style(temp2, "backgroundColor")
        actually_result.append((result_equal, result_equal_effect))
        self.logger.logger(f"actually result: {actually_result}")
        sleep(1)
        self.logger.logger("click on control_condition drop down")
        condition_dropdown = self.values.view_as_bar_controls_component(1)["condition"]
        condition_dropdown.click()
        sleep(1)
        mq_indicator = self.values.view_as_bar_controls_condition_options(1)[3]
        self.logger.logger("select condition as >=")
        mq_indicator.click()
        sleep(1)
        view_screen[0][0].click()
        sleep(2)
        temp = view_screen[2][1].find_element_by_css_selector("span")
        temp2 = view_screen[8][1].find_element_by_css_selector("span")
        result_mq = self.Dom_until.get_style(temp, "backgroundColor")
        result_mq_effect = self.Dom_until.get_style(temp2, "backgroundColor")
        actually_result.append((result_mq, result_mq_effect))
        self.logger.logger(f"actually result: {actually_result}")
        sleep(1)
        self.logger.logger("click on control_condition drop down")
        condition_dropdown = self.values.view_as_bar_controls_component(1)["condition"]
        condition_dropdown.click()
        sleep(1)
        lq_indicator = self.values.view_as_bar_controls_condition_options(1)[4]
        self.logger.logger("select condition as >=")
        lq_indicator.click()
        sleep(1)
        view_screen[0][0].click()
        sleep(2)
        temp = view_screen[2][1].find_element_by_css_selector("span")
        temp2 = view_screen[8][1].find_element_by_css_selector("span")
        result_lq = self.Dom_until.get_style(temp, "backgroundColor")
        result_lq_effect = self.Dom_until.get_style(temp2, "backgroundColor")
        actually_result.append((result_lq, result_lq_effect))
        sleep(1)
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_types_values_multiple(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Bar", "sales_count(sum)")
        actually_result = []
        self.logger.logger("click on Add New button")
        self.values.view_as_bar()["addnew_btn"].click()
        sleep(1)
        self.logger.logger("click on color picker")
        self.values.view_as_bar_controls_component(1)["color_picker"].click()
        sleep(1)
        color = "#417505"
        self.logger.logger(f"click on color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        sleep(1)
        input_num = "210"
        self.logger.logger(f"input {input_num} to conditions value")
        input_ele = self.values.view_as_bar_controls_component(1)["value"]
        self.Dom_until.dely_input(input_ele, input_num)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        sleep(1)
        self.logger.logger("click on Add New button")
        self.values.view_as_bar()["addnew_btn"].click()
        sleep(1)
        self.logger.logger("click on color picker")
        self.values.view_as_bar_controls_component(2)["color_picker"].click()
        sleep(1)
        color = "#F8E71C"
        self.logger.logger(f"click on color: {color}")
        self.prop_common.sketch_picker(color)[1].click()
        sleep(1)
        self.logger.logger("click on control_condition drop down")
        condition_dropdown = self.values.view_as_bar_controls_component(2)["condition"]
        condition_dropdown.click()
        sleep(1)
        indicator = self.values.view_as_bar_controls_condition_options(2)[1]
        self.logger.logger("select condition as =")
        indicator.click()
        view_screen[0][0].click()
        sleep(2)
        temp = view_screen[3][1].find_element_by_css_selector("span")
        result_morethan = self.Dom_until.get_style(temp, "backgroundColor")
        actually_result.append(result_morethan)
        temp = view_screen[8][1].find_element_by_css_selector("span")
        result_equal = self.Dom_until.get_style(temp, "backgroundColor")
        actually_result.append(result_equal)
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_valueas_bar_types_values_delete(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_viewas("Bar", "sales_count(sum)")
        self.logger.logger("click on Add New button")
        self.values.view_as_bar()["addnew_btn"].click()
        sleep(1)
        self.logger.logger("click on color picker")
        self.values.view_as_bar_controls_component(1)["color_picker"].click()
        sleep(1)
        color = "#417505"
        self.logger.logger(f"click on color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][1].find_element_by_css_selector("span")
        actually_result.append(self.Dom_until.get_style(target_ele, "backgroundColor"))
        self.values.view_as_bar_controls_component(1)["delete"].click()
        sleep(3)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][1].find_element_by_css_selector("span")
        actually_result.append(self.Dom_until.get_style(target_ele, "backgroundColor"))
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_types_var_sum(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_agg("Sum")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_types_var_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_agg("Min")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_types_var_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_agg("Max")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_types_var_avg(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_agg("Average")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_types_var_counntd(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_agg("Count Distinct")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_types_var_counnt(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_agg("Count")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_types_var_allowgroup_sum(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_allowtoggle_agg("Sum")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_types_var_allowgroup_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_allowtoggle_agg("Min")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_types_var_allowgroup_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_allowtoggle_agg("Max")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_types_var_allowgroup_avg(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_allowtoggle_agg("Average")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_types_var_allowgroup_countd(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_allowtoggle_agg("Count Distinct")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_types_var_allowgroup_count(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = self.handle_value_bar_variables_allowtoggle_agg("Count")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_bar_displayvalue(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_bar_unitconversions()
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[7][8]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_unit_auto(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_bar_unitconversions()
        sleep(1)
        self.logger.logger("click on Auto toggle")
        self.values.view_as_bar_unitconversion()["auto_toggle"].click()
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[7][8]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_unit_unit_static(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_bar_unitconversions()
        sleep(1)
        self.logger.logger("click on display unit toggle")
        self.values.view_as_bar_unitconversion()["display_unit_toggle"].click()
        self.logger.logger("select unit value default, K, Mn, Bn, % and get testing result")
        for i in range(0, 5):
            sleep(1)
            self.logger.logger("click on unit dropdown list")
            self.values.view_as_bar_unitconversion()["unit_dropdown"].click()
            sleep(1)
            self.values.view_as_bar_unitconversion_unit_options()[i].click()
            sleep(2)
            self.logger.logger("getting test result")
            view_screen = self.chart_edit.view_screen("pivottable")[0]
            actually_result.append(view_screen[7][8])
            sleep(1)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_unit_unit_dynamic(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_bar_unitconversions()
        sleep(1)
        self.logger.logger("click on display unit toggle")
        self.values.view_as_bar_unitconversion()["display_unit_toggle"].click()
        self.logger.logger("click on unit toggle to turn on Dynamic")
        self.values.view_as_bar_unitconversion()["unit_toggle"].click()
        sleep(1)
        self.logger.logger("click on unit dropdown list")
        self.values.view_as_bar_unitconversion()["unit_dropdown"].click()
        sleep(1)
        self.values.view_as_bar_unitconversion_unit_options()[1].click()
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result.append(view_screen[7][8])
        sleep(1)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_unit_decimal_static(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_bar_unitconversions()
        sleep(1)
        ele = self.values.view_as_bar_unitconversion()["Decimal_input"]
        test_input = 2
        self.logger.logger(f"input {test_input} to decimal input element")
        ele.send_keys(test_input)
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[7][8]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_unit_decimal_dynamic(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_bar_unitconversions()
        sleep(1)
        self.logger.logger("click on deciaml toggle")
        self.values.view_as_bar_unitconversion()["Decimal_toggle"].click()
        sleep(1)
        self.logger.logger("open decimal dropdown and select field")
        self.values.view_as_bar_unitconversion_decimal_dropdown().click()
        sleep(1)
        self.values.view_as_bar_unitconversion_decimal_options()["sales_count"].click()
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[7][8]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_unit_separator(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_bar_unitconversions()
        sleep(1)
        self.logger.logger("click on separator dropdown list and select values, recording test result")
        self.values.view_as_bar_unitconversion()["Separator_dropdown"].click()
        sleep(1)
        options = self.values.view_as_bar_unitconversion_separator_options()
        for i in options.keys():
            sleep(1)
            self.values.view_as_bar_unitconversion_separator_options()[i].click()
            view_screen = self.chart_edit.view_screen("pivottable")[0]
            result = view_screen[7][8]
            actually_result.append(result)
            sleep(1)
            self.values.view_as_bar_unitconversion()["Separator_dropdown"].click()
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_bar_unit_prefixAndSuffix(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_bar_unitconversions()
        sleep(1)
        test_text = "!@#1,-aC%"
        self.logger.logger(f"input {test_text} to prefix input element ")
        prefix_input = self.values.view_as_bar_unitconversion()["Prefix_inpput"]
        self.Dom_until.dely_input(prefix_input, test_text)
        self.logger.logger(f"input {test_text} to suffix input element ")
        suffix_input = self.values.view_as_bar_unitconversion()["Suffix_inpput"]
        self.Dom_until.dely_input(suffix_input, test_text)
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[2][2]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_bar_unit_format(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_bar_unitconversions()
        sleep(1)
        self.logger.logger("set format B, I, underline")
        self.prop_common.format_setting()["format_bold_btn"].click()
        self.prop_common.format_setting()["format_italic_btn"].click()
        self.prop_common.format_setting()["format_underline_btn"].click()
        self.prop_common.format_setting()["format_colorpicker_btn"].click()
        sleep(1)
        self.prop_common.sketch_picker("#417505")[0].click()
        self.prop_common.format_setting()["format_size"].click()
        sleep(1)
        self.prop_common.format_setting_size_options()["10px"].click()
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][2].find_element_by_css_selector("span")
        actually_result = [
            self.Dom_until.get_style(target_ele, "color"),
            self.Dom_until.get_style(target_ele, "fontStyle"),
            self.Dom_until.get_style(target_ele, "fontWeight"),
            self.Dom_until.get_style(target_ele, "textDecoration"),
            self.Dom_until.get_style(target_ele, "fontSize"),
        ]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_bar_unit_alignment(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_bar_unitconversions()
        sleep(1)
        actually_result = []
        self.logger.logger("set format left, center, right")
        self.logger.logger("getting center test result")
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][2].find_element_by_css_selector("span")
        actually_result.append(self.Dom_until.get_style(target_ele, "textAlign"))
        self.logger.logger("click on left btn")
        self.prop_common.format_setting_position("left").click()
        sleep(2)
        self.logger.logger("getting left test result")
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][2].find_element_by_css_selector("span")
        actually_result.append(self.Dom_until.get_style(target_ele, "textAlign"))
        self.logger.logger("click on left btn")
        self.prop_common.format_setting_position("right").click()
        sleep(2)
        self.logger.logger("getting right test result")
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][2].find_element_by_css_selector("span")
        actually_result.append(self.Dom_until.get_style(target_ele, "textAlign"))
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_indicator_style(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        indicator_css = self.pageobj["view_as_indicator_indicatorCssStyle"]
        actually_result = []
        test_value = 0
        self.handld_value_indicator_values(test_value)
        sleep(2)
        self.values.view_as_indicator_style_dropdown().click()
        sleep(1)
        options = self.values.view_as_indicator_style_dropdown_options()
        for option in options:
            option.click()
            sleep(1)
            self.values.view_as_indicator_style_dropdown().click()
            sleep(2)
            view_screen = self.chart_edit.view_screen("pivottable")[1]
            target_ele = view_screen[2][1].find_element_by_css_selector(indicator_css)
            actually_result.append(target_ele.get_attribute("class"))
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_indicator_size(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_value = 0
        self.handld_value_indicator_values(test_value)
        self.logger.logger("set size = 10px")
        self.values.view_as_indicator_size_dropdown().click()
        sleep(1)
        self.values.view_as_indicator_size_dropdown_options()["10px"].click()
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[2][1].find_element_by_css_selector(".arrowIcon")
        actually_result.append(self.Dom_until.get_style(target_ele, "width"))
        actually_result.append(self.Dom_until.get_style(target_ele, "height"))
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_values(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        indicator_css = self.pageobj["view_as_indicator_indicatorCssStyle"]
        actually_result = []
        test_value = 210
        options = [">", "<", "=", ">=", "<="]
        self.handld_value_indicator_values(test_value)
        for option in options:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {option} for condition")
            self.values.view_as_indicator_control_condition_options()[option].click()
            view_screen = self.chart_edit.view_screen("pivottable")[1]
            self.logger.logger("getting test result")
            for i in range(2, 9):
                for j in range(1, 9, 3):
                    if j > 9:
                        break
                    ele = view_screen[i][j].find_element_by_css_selector(indicator_css)
                    actually_result.append(ele.get_attribute("class"))
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_types_values_multiple(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handld_value_indicator_values("210")
        sleep(1)
        self.handld_value_indicator_values(num=2, color="#F8E71C", value="400")
        actually_result = self.handle_indicator_result()
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_indicator_values_delete(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handld_value_indicator_values("210")
        sleep(2)
        before_delete = self.handle_indicator_result()
        actually_result.append(before_delete)
        self.logger.logger("click on delete icon")
        self.values.view_as_indicator_control_delete().click()
        sleep(2)
        after_delete = self.handle_indicator_result()
        actually_result.append(after_delete)
        self.logger.logger(f"{actually_result}")
        # expected_result = self.handle_expectedresult()
        # self.handle_assert(actually_result, expected_result)

    def handle_indicator_var(self, agg="Sum", num=1, indicator=0, condition=">", color="#417505", var="target_count"):
        self.handle_viewas("Indicator", "sales_count(sum)")
        self.logger.logger("click on type dropdown list")
        self.values.view_as_indicator_type_dropdown().click()
        sleep(1)
        self.logger.logger("select Variables for type")
        self.values.view_as_indicator_type_dropdown_options()["Variables"].click()
        sleep(1)
        self.logger.logger("click on add button")
        self.values.view_as_add_btn().click()
        sleep(2)
        self.logger.logger("click on indicator style")
        self.values.view_as_indicator_control_styledropdown(num).click()
        sleep(1)
        self.logger.logger("click up for indicatior")
        self.values.view_as_indicator_control_styledropdown_options(num)[indicator].click()
        self.logger.logger("click on color picker component")
        self.values.view_as_indicator_control_colorpicker(num).click()
        sleep(1)
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[num - 1].click()
        self.logger.logger("click condition dropdown list")
        self.values.view_as_indicator_control_condition(num).click()
        sleep(1)
        self.logger.logger(f"select {condition} for condition")
        self.values.view_as_indicator_control_condition_options(num)[condition].click()
        sleep(1)
        self.logger.logger("click on reference var dropdown list")
        self.values.view_as_indicator_control_vardropdown(num).click()
        sleep(2)
        self.logger.logger("select reference var")
        self.values.view_as_indicator_control_vardropdown_options(num)[var].click()
        sleep(1)
        self.logger.logger("click on agg dropdown list")
        self.values.view_as_indicator_control_vardropdown(num).click()
        sleep(1)
        self.logger.logger(f"select Sum for {agg}")
        self.values.view_as_indicator_control_vardropdown_options(num)[agg].click()

    def handle_indicator_result(self):
        indicator_css = self.pageobj["view_as_indicator_indicatorCssStyle"]
        actually_result = []
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        for i in range(2, 9):
            for j in range(1, 9, 3):
                if j > 9:
                    break
                ele = view_screen[i][j].find_element_by_css_selector(indicator_css)
                ele_bcg = view_screen[i][j].find_element_by_css_selector(".value-viewer")
                bcgColor = self.Dom_until.get_style(ele_bcg, "backgroundColor")
                result = (ele.get_attribute("class"), bcgColor)
                actually_result.append(result)
        return actually_result

    @pytest.mark.critical
    def test_value_indicator_var_sum(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var()
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Min")
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Max")
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_avg(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Average")
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_count(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Count")
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_countd(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Count Distinct")
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_allowby_sum(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var()
        sleep(1)
        self.logger.logger("open allow group by row and col toggle")
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_allowby_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Min")
        sleep(1)
        self.logger.logger("open allow group by row and col toggle")
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_allowby_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Max")
        sleep(1)
        self.logger.logger("open allow group by row and col toggle")
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_allowby_avg(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Average")
        sleep(1)
        self.logger.logger("open allow group by row and col toggle")
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_allowby_count(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Count")
        sleep(1)
        self.logger.logger("open allow group by row and col toggle")
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_allowby_countd(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        test_conditions = ["<", "=", "<=", ">="]
        self.handle_indicator_var(agg="Count Distinct")
        sleep(1)
        self.logger.logger("open allow group by row and col toggle")
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        for condition in test_conditions:
            self.logger.logger("click condition dropdown list")
            self.values.view_as_indicator_control_condition().click()
            sleep(1)
            self.logger.logger(f"select {condition} for condition")
            self.values.view_as_indicator_control_condition_options()[condition].click()
            sleep(2)
            actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_multiple(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_indicator_var(condition="<")
        sleep(1)
        self.handle_indicator_var(num=2, condition="<", color="#F8E71C", var="sales_count/ amount")
        sleep(2)
        actually_result.append(self.handle_indicator_result())
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_indicator_var_delete(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_indicator_var(condition="<")
        sleep(2)
        before_delete_result = self.handle_indicator_result()
        actually_result.append(before_delete_result)
        sleep(1)
        self.logger.logger("click on delete button")
        self.values.view_as_indicator_control_delete().click()
        sleep(2)
        after_delete_result = self.handle_indicator_result()
        actually_result.append(after_delete_result)
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_indicator_valueborder(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handld_value_indicator_values("210")
        self.logger.logger(f"open Show Value Border toggle")
        self.values.view_as_indicator_showvalue_toggle()["Show Value Border"].click()
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[3][1].find_element_by_css_selector(".value-viewer")
        border = self.Dom_until.get_style(target_ele, "border")
        margin = self.Dom_until.get_style(target_ele, "margin")
        self.logger.logger_debug(f"border: {border}, margin: {margin}")
        actually_result.append(border)
        actually_result.append(margin)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_indicator_valuelabels(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handld_value_indicator_values("210")
        sleep(1)
        self.logger.logger(f"open Show Value Labels toggle")
        self.values.view_as_indicator_showvalue_toggle()["Show Value Labels"].click()
        sleep(1)
        self.logger.logger("click on bold btn")
        self.values.view_as_indicator_showvalue_format()["format_bold_btn"].click()
        sleep(1)
        self.logger.logger("click on italic btn")
        self.values.view_as_indicator_showvalue_format()["format_italic_btn"].click()
        sleep(1)
        self.logger.logger("click on underline btn")
        self.values.view_as_indicator_showvalue_format()["format_underline_btn"].click()
        sleep(1)
        self.logger.logger("click on color picker btn")
        self.values.view_as_indicator_showvalue_format()["format_colorpicker_btn"].click()
        sleep(1)
        color = "#417505"
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[1].click()
        self.logger.logger("click on size dropdown")
        self.values.view_as_indicator_showvalue_format()["format_size"].click()
        sleep(1)
        self.logger.logger("select 10 px for size")
        self.values.view_as_indicator_showvalue_format_sizeoptions()["10px"].click()
        sleep(2)
        self.logger.logger("getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        target_ele = view_screen[3][1].find_elements_by_css_selector("span")[1]
        color_css = self.Dom_until.get_style(target_ele, "color")
        fontSize = self.Dom_until.get_style(target_ele, "fontSize")
        fontStyle = self.Dom_until.get_style(target_ele, "fontStyle")
        fontWeight = self.Dom_until.get_style(target_ele, "fontWeight")
        textDecoration = self.Dom_until.get_style(target_ele, "textDecoration")
        actually_result.append(color_css)
        actually_result.append(fontSize)
        actually_result.append(fontStyle)
        actually_result.append(fontWeight)
        actually_result.append(textDecoration)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_indicator_valuelabels_position(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handld_value_indicator_values("210")
        sleep(1)
        self.logger.logger(f"open Show Value Labels toggle")
        self.values.view_as_indicator_showvalue_toggle()["Show Value Labels"].click()
        sleep(1)
        positions = ["left", "top", "right", "bottom"]
        for i in positions:
            self.logger.logger(f"click on position: {i}")
            self.values.view_as_indicator_showvalue_format_position(i).click()
            sleep(2)
            self.logger.logger("getting test result")
            view_screen = self.chart_edit.view_screen("pivottable")[1]
            target_ele = view_screen[3][1].find_elements_by_css_selector("span")[0]
            flexDirection = self.Dom_until.get_style(target_ele, "flexDirection")
            actually_result.append(flexDirection)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    def handle_starRate(self):
        self.handle_viewas("Star Rate", "sales_count(sum)")
        fullStar = 5
        fullScore = 400
        self.logger.logger(f"input full star: {fullStar}")
        self.values.view_as_starrate_fullstar_input().send_keys(fullStar)
        sleep(1)
        self.logger.logger(f"input full star: {fullScore}")
        fullScoreEle = self.values.view_as_starrate_fullscore_input()
        self.Dom_until.dely_input(fullScoreEle, fullScore)

    def handle_starRate_result(self):
        resultCountCss = self.pageobj["handle_starRate_result"]
        actually_result = []
        self.logger.logger("getting test result")
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        for i in range(2, 8):
            for j in range(1, 9, 3):
                if j > 9:
                    break
                ele = view_screen[i][j].find_element_by_css_selector("ul")
                resultColor = self.Dom_until.get_style(ele, "color")
                resultCount = len(ele.find_elements_by_css_selector(resultCountCss))
                actually_result.append((resultColor, resultCount))
        return actually_result

    @pytest.mark.critical
    def test_value_starRate_base(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_starRate()
        actually_result = str(self.handle_starRate_result())
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_starRate_roundness(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_starRate()
        roundDown = self.handle_starRate_result()
        self.logger.logger(f"click on roundness dropdown")
        self.values.view_as_starrate_roundness_dropdown().click()
        sleep(1)
        self.logger.logger(f"select round up for roundness field")
        self.values.view_as_starrate_roundness_dropdown_options()["Round Up"].click()
        upDown = self.handle_starRate_result()
        actually_result.append(roundDown)
        actually_result.append(upDown)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    def handle_starRate_values(self, num=1, condition=">", test_input=210):
        self.handle_starRate()
        self.logger.logger("click on Add New button")
        self.values.view_as_addnew_btn().click()
        sleep(3)
        self.logger.logger("click on color picker button")
        self.values.view_as_starrate_control_colorpicker(num).click()
        color = "#417505"
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        self.logger.logger("click on conditions dropdown list")
        self.values.view_as_starrate_control_condition_dropdown(num).click()
        sleep(1)
        self.logger.logger(f"select condition: {condition}")
        self.values.view_as_starrate_control_condition_dropdown_options(num)[condition].click()
        sleep(1)
        test_input = test_input
        self.logger.logger(f"input values: {test_input}")
        ele = self.values.view_as_starrate_control_condition_input(num)
        self.Dom_until.dely_input(ele, test_input)

    @pytest.mark.critical
    def test_value_starRate_values(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        conditions = ["<", "=", ">=", "<="]
        actually_result = []
        self.handle_starRate_values()
        sleep(1)
        actually_result.append(self.handle_starRate_result())
        for condition in conditions:
            self.logger.logger("click on conditions dropdown list")
            self.values.view_as_starrate_control_condition_dropdown(1).click()
            sleep(1)
            self.logger.logger(f"select condition: {condition}")
            self.values.view_as_starrate_control_condition_dropdown_options(1)[condition].click()
            actually_result.append(self.handle_starRate_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_starRate_values_multiple(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_starRate_values()
        sleep(1)
        self.logger.logger("click on Add New button")
        self.values.view_as_addnew_btn().click()
        sleep(3)
        self.logger.logger("click on color picker button")
        self.values.view_as_starrate_control_colorpicker(2).click()
        color = "#D0021B"
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[1].click()
        self.logger.logger("click on conditions dropdown list")
        self.values.view_as_starrate_control_condition_dropdown(2).click()
        sleep(1)
        self.logger.logger(f"select condition: <")
        self.values.view_as_starrate_control_condition_dropdown_options(2)["<"].click()
        sleep(1)
        test_input = 400
        self.logger.logger(f"input values: {test_input}")
        ele = self.values.view_as_starrate_control_condition_input(2)
        self.Dom_until.dely_input(ele, test_input)
        sleep(2)
        actually_result = self.handle_starRate_result()
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    def handle_starRate_var(self, num=1, condition=">", var="target_count", agg="Sum"):
        self.handle_starRate()
        self.logger.logger("click on types dropdown list")
        self.values.view_as_types_dropdown().click()
        sleep(1)
        self.logger.logger("select Variables for types")
        self.values.view_as_types_dropdown_options()["Variables"].click()
        self.logger.logger("click on Add New button")
        self.values.view_as_addnew_btn().click()
        sleep(3)
        self.logger.logger("click on color picker button")
        self.values.view_as_starrate_control_colorpicker(num).click()
        color = "#417505"
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[0].click()
        self.logger.logger("click on conditions dropdown list")
        self.values.view_as_starrate_control_var_dropdown(num)[0].click()
        sleep(1)
        self.logger.logger(f"select condition: {condition}")
        self.values.view_as_starrate_control_var_dropdown_options_condition(num)[condition].click()
        sleep(1)
        self.logger.logger("click on var dropdown")
        self.values.view_as_starrate_control_var_dropdown(num)[1].click()
        sleep(1)
        self.logger.logger(f"select {var} for var")
        self.values.view_as_starrate_control_var_dropdown_options_var(num)[var].click()
        sleep(2)
        self.logger.logger(f"select {agg} for Aggregation")
        self.values.view_as_starrate_control_aggregation(num).click()
        sleep(1)
        self.values.view_as_starrate_control_aggregation_options(num)[agg].click()

    @pytest.mark.critical
    def test_value_starRate_var_sum(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        conditions = ["<", "=", ">=", "<="]
        actually_result = []
        self.handle_starRate_var()
        sleep(1)
        actually_result.append(self.handle_starRate_result())
        for condition in conditions:
            self.logger.logger("click on conditions dropdown list")
            self.values.view_as_starrate_control_var_dropdown(1)[0].click()
            sleep(1)
            self.logger.logger(f"select condition: {condition}")
            self.values.view_as_starrate_control_var_dropdown_options_condition(1)[condition].click()
            actually_result.append(self.handle_starRate_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_starRate_var_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        conditions = ["<", "=", ">=", "<="]
        actually_result = []
        self.handle_starRate_var(agg="Min")
        sleep(1)
        actually_result.append(self.handle_starRate_result())
        for condition in conditions:
            self.logger.logger("click on conditions dropdown list")
            self.values.view_as_starrate_control_var_dropdown(1)[0].click()
            sleep(1)
            self.logger.logger(f"select condition: {condition}")
            self.values.view_as_starrate_control_var_dropdown_options_condition(1)[condition].click()
            actually_result.append(self.handle_starRate_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_starRate_var_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        conditions = ["<", "=", ">=", "<="]
        actually_result = []
        self.handle_starRate_var(agg="Max")
        sleep(1)
        actually_result.append(self.handle_starRate_result())
        for condition in conditions:
            self.logger.logger("click on conditions dropdown list")
            self.values.view_as_starrate_control_var_dropdown(1)[0].click()
            sleep(1)
            self.logger.logger(f"select condition: {condition}")
            self.values.view_as_starrate_control_var_dropdown_options_condition(1)[condition].click()
            actually_result.append(self.handle_starRate_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_starRate_var_avg(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        conditions = ["<", "=", ">=", "<="]
        actually_result = []
        self.handle_starRate_var(agg="Average")
        sleep(1)
        actually_result.append(self.handle_starRate_result())
        for condition in conditions:
            self.logger.logger("click on conditions dropdown list")
            self.values.view_as_starrate_control_var_dropdown(1)[0].click()
            sleep(1)
            self.logger.logger(f"select condition: {condition}")
            self.values.view_as_starrate_control_var_dropdown_options_condition(1)[condition].click()
            actually_result.append(self.handle_starRate_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_starRate_var_count(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        conditions = ["<", "=", ">=", "<="]
        actually_result = []
        self.handle_starRate_var(agg="Count")
        sleep(1)
        actually_result.append(self.handle_starRate_result())
        for condition in conditions:
            self.logger.logger("click on conditions dropdown list")
            self.values.view_as_starrate_control_var_dropdown(1)[0].click()
            sleep(1)
            self.logger.logger(f"select condition: {condition}")
            self.values.view_as_starrate_control_var_dropdown_options_condition(1)[condition].click()
            actually_result.append(self.handle_starRate_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_starRate_var_countd(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        conditions = ["<", "=", ">=", "<="]
        actually_result = []
        self.handle_starRate_var(agg="Count Distinct")
        sleep(1)
        actually_result.append(self.handle_starRate_result())
        for condition in conditions:
            self.logger.logger("click on conditions dropdown list")
            self.values.view_as_starrate_control_var_dropdown(1)[0].click()
            sleep(1)
            self.logger.logger(f"select condition: {condition}")
            self.values.view_as_starrate_control_var_dropdown_options_condition(1)[condition].click()
            actually_result.append(self.handle_starRate_result())
            sleep(1)
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_starRate_var_allowby(self):
        # not effect for starRate
        pass

    @pytest.mark.critical
    def test_value_starRate_var_multiple(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_starRate_var(agg="Average", var="sales_count")
        sleep(1)
        self.logger.logger("click on Add New button")
        self.values.view_as_addnew_btn().click()
        sleep(3)
        self.logger.logger("click on color picker button")
        self.values.view_as_starrate_control_colorpicker(2).click()
        color = "#D0021B"
        self.logger.logger(f"select color: {color}")
        self.prop_common.sketch_picker(color)[1].click()
        self.logger.logger("click on conditions dropdown list")
        self.values.view_as_starrate_control_var_dropdown(2)[0].click()
        sleep(1)
        self.logger.logger(f"select condition: >")
        self.values.view_as_starrate_control_var_dropdown_options_condition(2)["<"].click()
        sleep(1)
        self.logger.logger("click on var dropdown")
        self.values.view_as_starrate_control_var_dropdown(2)[1].click()
        sleep(1)
        self.logger.logger(f"select sales_count for var")
        self.values.view_as_starrate_control_var_dropdown_options_var(2)["sales_count"].click()
        sleep(1)
        self.logger.logger(f"select Average for Aggregation")
        self.values.view_as_starrate_control_aggregation(2).click()
        sleep(1)
        self.values.view_as_starrate_control_aggregation_options(2)["Average"].click()
        sleep(2)
        actually_result = self.handle_starRate_result()
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_starRate_var_delete(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_starRate_var(agg="Average", var="sales_count")
        sleep(2)
        beforeDelete = self.handle_starRate_result()
        actually_result.append(beforeDelete)
        self.logger.logger("click on delete button")
        self.values.view_as_starrate_control_delete(1).click()
        sleep(2)
        afterDelete = self.handle_starRate_result()
        actually_result.append(afterDelete)
        expected_result = self.handle_expectedresult()
        actually_result = str(actually_result)
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.mid
    def test_value_starRate_size(self, driver):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_starRate()
        sleep(1)
        inputEle = self.values.view_as_starrate_size_input()
        action = ActionChains(driver)
        action.key_down(Keys.BACKSPACE, element=inputEle)
        sleep(1)
        action.key_down(Keys.BACKSPACE, element=inputEle)
        action.perform()
        sleep(1)
        fontSize = self.handle_expectedresult()[:2]
        self.Dom_until.dely_input(inputEle, fontSize)
        sleep(1)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        ele = view_screen[2][1].find_element_by_css_selector("ul")
        actually_result = self.Dom_until.get_style(ele, "fontSize")
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.high
    def test_value_starRate_overScore(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_starRate()
        sleep(1)
        self.values.view_as_starrate_overallscore_toggle().click()
        sleep(1)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        for i in range(2, 8):
            for j in range(1, 9, 3):
                if j > 9:
                    break
                eleText = view_screen[i][j]
                actually_result.append(eleText)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    def handle_colorCodingValues(self, num=1, bcColor="#8B572A", color="#F5A623", condition=">", inputText=330,
                                 sketch_1=0, sketch_2=1):
        sleep(1)
        self.logger.logger("click on Add New Button")
        self.values.view_as_addnew_btn().click()
        sleep(1)
        self.logger.logger("Click on background color picker")
        self.values.view_as_colorcoding_control_values_bcColorpicker(num).click()
        sleep(1)
        self.logger.logger(f"select {bcColor} for background color")
        self.prop_common.sketch_picker(bcColor)[sketch_1].click()
        self.logger.logger("Click on color picker")
        self.values.view_as_colorcoding_control_values_fontColorpicker(num).click()
        sleep(1)
        self.logger.logger(f"select {color} for background color")
        self.prop_common.sketch_picker(color)[sketch_2].click()
        self.logger.logger("click on condition dropdown list")
        self.values.view_as_colorcoding_control_values_condition_dropdown(num).click()
        sleep(1)
        self.values.view_as_colorcoding_control_values_condition_dropdown_options(num)[condition].click()
        sleep(1)
        inputTextEle = self.values.view_as_colorcoding_control_values_input(num)
        self.Dom_until.dely_input(inputTextEle, inputText)

    def handle_colorCoding_result(self):
        handle_colorCoding_result_bc = self.pageobj["handle_colorCoding_result_bc"]
        handle_colorCoding_result_font = self.pageobj["handle_colorCoding_result_font"]
        actually_result = []
        self.logger.logger("getting test result")
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        for i in range(2, 8):
            for j in range(1, 9, 3):
                if j > 9:
                    break
                bcEle = view_screen[i][j].find_element_by_css_selector(handle_colorCoding_result_bc)
                fontEle = view_screen[i][j].find_element_by_css_selector(handle_colorCoding_result_font)
                bcColor = self.Dom_until.get_style(bcEle, "backgroundColor")
                fontColor = self.Dom_until.get_style(fontEle, "color")
                actually_result.append((bcColor, fontColor))
        return actually_result

    @pytest.mark.smoke
    def test_value_colorCoding_values(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCodingValues()
        actually_result.append(self.handle_colorCoding_result())
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorcoding_control_values_condition_dropdown(1).click()
            sleep(1)
            self.logger.logger(f"select {condition}")
            self.values.view_as_colorcoding_control_values_condition_dropdown_options(1)[condition].click()
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.smoke
    def test_value_colorCoding_values_multiple(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCodingValues()
        sleep(1)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        sleep(1)
        self.handle_colorCodingValues(num=2, inputText=400, sketch_1=2, sketch_2=3, color="#F8E71C")
        actually_result = self.handle_colorCoding_result()
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_values_delete(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.logger.logger("click on Add New Button")
        self.values.view_as_addnew_btn().click()
        sleep(1)
        beforeDelete = self.handle_colorCoding_result()
        self.values.view_as_colorcoding_control_values_delete(1).click()
        sleep(1)
        afterDelete = self.handle_colorCoding_result()
        actually_result.append(beforeDelete)
        actually_result.append(afterDelete)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    def handle_colorCoding_var(self, num=1, bcColor="#8B572A", color="#F5A623", condition=">", var="target_count",
                               sketch_1=0, sketch_2=1, agg="Sum"):
        self.logger.logger("click on type dropdown list")
        self.values.view_as_type_dropdown().click()
        sleep(1)
        self.logger.logger("select Variables for type")
        self.values.view_as_type_dropdown_options()["Variables"].click()
        sleep(1)
        self.logger.logger("click on Add New Button")
        self.values.view_as_add_btn().click()
        sleep(1)
        self.logger.logger("Click on background color picker")
        self.values.view_as_colorCoding_controlVar_bcgColor(num).click()
        sleep(1)
        self.logger.logger(f"select {bcColor} for background color")
        self.prop_common.sketch_picker(bcColor)[sketch_1].click()
        self.logger.logger("Click on color picker")
        self.values.view_as_colorCoding_controlVar_fontColor(num).click()
        sleep(1)
        self.logger.logger(f"select {color} for background color")
        self.prop_common.sketch_picker(color)[sketch_2].click()
        self.logger.logger("click on condition dropdown list")
        self.values.view_as_colorCoding_controlVar_conditionDropdown(num).click()
        sleep(1)
        self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(num)[condition].click()
        sleep(1)
        self.logger.logger("click on variables dropdown list")
        self.values.view_as_colorCoding_controlVar_varDropdown(num).click()
        sleep(1)
        self.logger.logger(f"select {var}")
        self.values.view_as_colorCoding_controlVar_varDropdownOptions(num)[var].click()
        sleep(1)
        self.logger.logger("click on aggregation dropdown list")
        self.values.view_as_colorCoding_controlVar_aggDropdown(num).click()
        sleep(1)
        self.logger.logger(f"select {var}")
        self.values.view_as_colorCoding_controlVar_aggDropdownOptions(num)[agg].click()

    @pytest.mark.smoke
    def test_value_colorCoding_var_sum(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var()
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Min")
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Max")
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_avg(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Average")
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_count(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Count")
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_countd(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Count Distinct")
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.smoke
    def test_value_colorCoding_var_allowGrounp_sum(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var()
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.smoke
    def test_value_colorCoding_var_allowGrounp_min(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Min")
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_allowGrounp_max(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Max")
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_allowGrounp_avg(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Average")
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_allowGrounp_count(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Count")
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_allowGrounp_countd(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        actually_result = []
        conditions = ["<", "=", ">=", "<="]
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(agg="Count Distinct")
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Row"].click()
        sleep(1)
        self.values.view_as_allowgroup_toggle()["Allow Group by Col"].click()
        sleep(1)
        actually_result.append(self.handle_colorCoding_result())
        sleep(1)
        for condition in conditions:
            self.logger.logger("click on condition dropdown list")
            self.values.view_as_colorCoding_controlVar_conditionDropdown(1).click()
            sleep(1)
            self.values.view_as_colorCoding_controlVar_conditionDropdownOptions(1)[condition].click()
            sleep(1)
            actually_result.append(self.handle_colorCoding_result())
            sleep(1)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_multiple(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        control1_condition = "<"
        control1_aggregation = "Min"
        control2_bcg = "#417505"
        control2_font = "#D0021B"
        control2_condition = ">"
        control2_aggregation = "Max"
        control2_var = "sales_count"
        self.handle_viewas("Color Coding", "sales_count(sum)")
        self.handle_colorCoding_var(condition=control1_condition, agg=control1_aggregation)
        sleep(1)
        self.handle_colorCoding_var(num=2, bcColor=control2_bcg, color=control2_font, condition=control2_condition,
                                    agg=control2_aggregation, var=control2_var, sketch_1=2, sketch_2=3)
        actually_result = self.handle_colorCoding_result()
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_colorCoding_var_delete(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Color Coding", "sales_count(sum)")
        actually_result = []
        self.handle_colorCoding_var(condition="<")
        beforeDel = self.handle_colorCoding_result()
        sleep(1)
        self.values.view_as_colorcoding_control_variables_delete().click()
        afterDel = self.handle_colorCoding_result()
        actually_result.append(beforeDel)
        actually_result.append(afterDel)
        actually_result = str(actually_result)
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_value_baseFunc(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Value", "target_count(sum)")
        sleep(2)
        self.logger.logger("Getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[7][8]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    @pytest.mark.critical
    def test_value_value_unitConversion(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Value", "target_count(sum)")
        self.values.view_as_unitconversion_auto_toggle().click()
        sleep(2)
        self.logger.logger("Getting test result")
        view_screen = self.chart_edit.view_screen("pivottable")[0]
        actually_result = view_screen[7][8]
        expected_result = self.handle_expectedresult()
        self.handle_assert(actually_result, expected_result)

    def handle_gradientColor_result(self):
        handle_gradientColor_result_bc = self.pageobj["handle_gradientColor_result_bc"]
        handle_gradientColor_result_font = self.pageobj["handle_gradientColor_result_font"]
        actually_result = []
        self.logger.logger("getting test result")
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        view_screen[0][0].click()
        sleep(2)
        view_screen = self.chart_edit.view_screen("pivottable")[1]
        for i in range(2, 8):
            for j in range(1, 9, 3):
                if j > 9:
                    break
                bcEle = view_screen[i][j].find_element_by_css_selector(handle_gradientColor_result_bc)
                fontEle = view_screen[i][j].find_element_by_css_selector(handle_gradientColor_result_font)
                bcColor = self.Dom_until.get_style(bcEle, "backgroundColor")
                fontColor = self.Dom_until.get_style(fontEle, "color")
                actually_result.append((bcColor, fontColor))
        return actually_result

    @pytest.mark.smoke
    def test_value_gradient_baseFunc(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Gradient Color", "sales_count(sum)")
        sleep(2)
        self.logger.logger("Getting test result")
        actually_result = self.handle_gradientColor_result()
        # expected_result = self.handle_expectedresult()
        # self.handle_assert(actually_result, expected_result)
        # expected_result = self.handle_expectedresult()
        # print(expected_result)

    @pytest.mark.critical
    def test_value_gradient_customize(self):
        self.logger.logger(f"Starting test TC {inspect.stack()[0][3]}")
        self.handle_viewas("Gradient Color", "sales_count(sum)")
        self.logger.logger("click on customize toggle")
        self.values.view_as_gradientcolor_customize_toggle().click()
        sleep(1)
        actually_result = self.handle_gradientColor_result()
        self.logger.logger(actually_result)
        # expected_result = self.handle_expectedresult()
        # self.handle_assert(actually_result, expected_result)


    # column border
