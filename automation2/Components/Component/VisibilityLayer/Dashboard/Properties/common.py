import time
from Common.dom_until import DomUntil
from Common.logger_until import Logger
from Common.web_config_until import WebConfig
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from time import sleep
from selenium.webdriver.common.keys import Keys


class Common(DomUntil):
    """
    common function in properties
    """

    def __init__(self, driver):
        DomUntil.__init__(self, driver)
        self.findele = DomUntil(driver).findelement
        self.findeles = DomUntil(driver).findelements
        self.log = Logger()
        self._webconfig = WebConfig('Properties_common')
        self._pageobj = self._webconfig.domelements
        self.CharEdit = ChartEdit(driver)

    def sketch_picker(self, color):
        """

        :param color: eg: green {#417505}
        :return: element []
        """
        sleep(1)
        try:
            css = ".sketch-picker div[title='" + color + "']"
            color_btn = self.findeles(css)
            return color_btn
        except Exception as e:
            raise e and self.log.logger_error(e)

    def get_dropdown_options(self, element):
        """
        find the drop-down options value
        :param aria: aria-controls id
        :return: elements[] (options)
        """
        options = {}
        options_arr = []
        css = ''
        aria = element.get_attribute("aria-controls")
        if aria[0].isalpha():
            css = "#" + aria + " li"
        elif aria[0].isnumeric():
            css = "#\\3" + aria[0] + ' ' + aria[1:] + " li"
        ele = self.findeles(css)
        if ele[0].text != '':
            for i in ele:
                options[i.text] = i
            return options
        else:
            for i in ele:
                options_arr.append(i)
            return options_arr

    def format_setting(self):
        """
        format component for properties setting
        :return: {}
        """
        options = {}
        format_bold_css = self._pageobj["format_bold_css"]
        format_italic_css = self._pageobj["format_italic_css"]
        format_underline_css = self._pageobj["format_underline_css"]
        format_colorpicker_css = self._pageobj["format_colorPicker_css"]
        format_size_css = self._pageobj["format_siez_css"]
        options["format_bold_btn"] = self.findele(format_bold_css)
        options["format_italic_btn"] = self.findele(format_italic_css)
        options["format_underline_btn"] = self.findele(format_underline_css)
        options["format_colorpicker_btn"] = self.findele(format_colorpicker_css)
        options["format_size"] = self.findele(format_size_css)
        return options

    def format_setting_size_options(self):
        """
        return format_size options
        :return:{}
        """
        try:
            unit_dropdown = self.format_setting()["format_size"]
            options = self.get_dropdown_options(unit_dropdown)
            return options
        except Exception as e:
            raise e and self.log.logger_error(e)

    def format_setting_position(self, position):
        css_obj = "position_" + position
        css = self._pageobj[css_obj]
        ele = self.findele(css)
        return ele

    def all_element(self):
        css_all = self._pageobj["all_elements"]
        eles = self.findeles(css_all)
        return eles

    def toggle(self, toggle_name, sign=False):
        if sign == False:
            all_ele = self.all_element()
            toggle = self.next_ele(self.parentnode(self.contains(all_ele, toggle_name))).find_element_by_css_selector(
                "button").click()
            return toggle
        else:
            all_ele = self.all_element()
            toggle = self.next_ele(self.contains(all_ele, toggle_name)).find_element_by_css_selector(
                "button").click()
            return toggle

    def tab_click(self, tag_name):
        """
        click on values section
        usage: values_tab_click()
        :return: action
        """
        try:
            ele = self.CharEdit.properties_select(tag_name)
            self.log.logger(f'click on Values section')
            ele.click()
        except Exception as err:
            raise err and self.log.logger_error(err)

    def assert_text(self):
        table_dict = {}
        table_list = []
        table_element = self._pageobj["table"]
        table_tr = self.findeles(table_element)[0].find_elements_by_css_selector("td")
        num_table = len(self.findeles(table_element))
        for i in range(len(table_tr)):
            for j in range(0 + 1, num_table):
                table_td = self.findeles(table_element)[j].find_elements_by_css_selector("td")[i]
                if table_td.text.isdigit():
                    table_list.append(int(table_td.text))
                else:
                    table_list.append(table_td.text)
            table_dict[table_tr[i].text] = table_list
            table_list = []
        return table_dict

    def input_text(self, toggle_name, text):
        """
        对不带默认值的输入框进行输入操作
        :param toggle_name: 输入框的名字
        :param text: 输入内容
        :return: None
        """
        all_ele = self.all_element()
        try:
            toggle = self.next_ele(self.contains(all_ele, toggle_name)).find_element_by_css_selector(
                "input")
        except:
            toggle = self.parentnode(self.contains(all_ele, toggle_name)).find_element_by_css_selector(
                "input")
        toggle.clear()
        toggle.send_keys(text)
        toggle.send_keys(Keys.ENTER)

    def dropdown(self, dropdown_name, name):
        all_ele = self.all_element()
        drop_down_css = self._pageobj["drop_down"]
        try:
            toggle = self.next_ele(self.contains(all_ele, dropdown_name)).find_element_by_css_selector(drop_down_css)
        except:
            toggle = self.next_ele(self.parentnode(self.contains(all_ele, dropdown_name))).find_element_by_css_selector(
                drop_down_css)
        toggle.click()
        time.sleep(2)
        self.get_dropdown_options(toggle)[name].click()
