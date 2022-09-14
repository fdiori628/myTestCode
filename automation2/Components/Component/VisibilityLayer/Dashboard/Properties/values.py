from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from Common.logger_until import Logger
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from time import sleep
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


class Values:

    def __init__(self, _driver):
        self._log = Logger()
        self._webconfig = WebConfig('Properties_common/values')
        self._pageobj = self._webconfig.domelements
        self.dom = DomUntil(_driver)
        self._findele = DomUntil(_driver).findelement
        self._findeles = DomUntil(_driver).findelements
        self._contains = DomUntil(_driver).contains
        self._waiturl = DomUntil(_driver).wait_url
        self.nextele = DomUntil(_driver).next_ele
        self.CharEdit = ChartEdit(_driver)
        self.childele = DomUntil(_driver).child_ele
        self.parentnode = DomUntil(_driver).parentnode
        self.common = Common(_driver)

    def values_all(self):
        """
        find all eles in values component
        :return: elements
        """
        try:
            css_all = self._pageobj['values_elements']
            eles = self._findeles(css_all)
            return eles
        except Exception as e:
            raise e and self._log.logger_error(e)

    def values_tab_click(self):
        """
        click on values section
        usage: values_tab_click()
        :return: action
        """
        try:
            ele = self.CharEdit.properties_select('Values')
            self._log.logger(f'click on Values section')
            ele.click()
        except Exception as err:
            raise err and self._log.logger_error(err)

    def view_as_allowgroup_toggle(self):
        """
        available only if type = variables
        :return: {}
        """
        toggle = {}
        all_ele = self.values_all()
        toggle["Allow Group by Row"] = self.nextele(self._contains(all_ele, "Allow Group by Row")) \
            .find_element_by_css_selector("button")
        toggle["Allow Group by Col"] = self.nextele(self._contains(all_ele, "Allow Group by Col")) \
            .find_element_by_css_selector("button")
        return toggle

    def view_as_types_dropdown(self):
        dropdown_css = self._pageobj["view_as_dropdown"]
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Types")).find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_types_dropdown_options(self):
        dropdown = self.view_as_types_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_type_dropdown(self):
        dropdown_css = self._pageobj["view_as_dropdown"]
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Type")).find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_type_dropdown_options(self):
        dropdown = self.view_as_type_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_add_btn(self):
        """
        "Add" btn
        :return:
        """
        all_ele = self.values_all()
        add_span = self._contains(all_ele, "Add")
        add_btn = self.parentnode(add_span)
        return add_btn

    def view_as_addnew_btn(self):
        """
        "Add New" btn
        :return:
        """
        all_ele = self.values_all()
        add_span = self._contains(all_ele, "Add New")
        addnew_btn = self.parentnode(add_span)
        return addnew_btn

    def view_as_unitconversion_auto_toggle(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Auto")) \
            .find_element_by_css_selector("button")
        return ele

    def view_as_unitconversion_units_toggle(self):
        all_ele = self.values_all()
        ele = self.nextele(self.parentnode(self._contains(all_ele, "Units"))) \
            .find_element_by_css_selector("button")
        return ele

    def view_as_unitconversion_units_dropdown(self):
        dropdown = self._pageobj["view_as_dropdown"]
        ele = self.nextele(self.parentnode(self.parentnode(self.view_as_unitconversion_units_toggle()))) \
            .find_element_by_css_selector(dropdown)
        return ele

    def view_as_unitconversion_units_options(self):
        ele = self.view_as_unitconversion_units_dropdown()
        options = self.common.get_dropdown_options(ele)
        self._log.logger_debug(f"view_as_unitconversion_units_options: {options.keys()}")
        return options

    def view_as_unitconversion_displayunit_toggle(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Display Unit")) \
            .find_element_by_css_selector("button")
        return ele

    def view_as_unitconversion_decimal_toggle(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Decimal"))
        return ele

    def view_as_unitconversion_decimal_input(self):
        ele_css = self._pageobj["view_as_unitconversion_decimal"]
        ele = self._findele(ele_css).find_element_by_css_selector("input")
        return ele

    def view_as_unitconversion_decimal_dropdown(self):
        dropdown_css = self._pageobj["view_as_dropdown"]
        ele_css = self._pageobj["view_as_unitconversion_decimal"]
        ele = self._findele(ele_css).find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_unitconversion_decimal_options(self):
        """

        :return: (dropdown-element, dropdown-options)
        """
        dropdown = self.view_as_unitconversion_decimal_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        self._log.logger_debug(f"view_as_unitconversion_units_options: {options.keys()}")
        return options

    def occupy_whole_area(self):
        """
        Occupy The Whole Area toggle
        usage: occupy_whole_area().click()
        :return: element
        """
        try:
            eles = self.values_all()
            ele = self._contains(eles, "Occupy The Whole Area")
            targetele = self.childele(self.nextele(ele), 1)
            return targetele
        except Exception as err:
            raise err and self._log.logger_error(err)

    def hide_value_headers(self):
        """
        hide value header toggle
        usage: hide_value_headers().click()
        :return: element
        """
        try:
            eles = self.values_all()
            ele = self._contains(eles, "Hide Value Headers")
            targetele = self.childele(self.nextele(ele), 1)
            return targetele
        except Exception as err:
            raise err and self._log.logger_error(err)

    def value_header_border(self):
        """
        value header border drop down
        usage: value_header_border().click()
        :return: element
        """
        try:
            eles = self.values_all()
            ele = self._contains(eles, "Value Header Border")
            target = self.nextele(ele)
            return target
        except Exception as err:
            raise err and self._log.logger_error(err)

    def value_header_border_options(self):
        """
        Value Header Border selection box options
        usage: value_header_border_options()["options"].click()
        :return: dict
        """
        ele = self.value_header_border()
        ele.click()
        sleep(2)
        options = self.common.get_dropdown_options(ele)
        return options
        # option_eles = []
        # options = []
        # target_dict = {}
        # try:
        #     css_eles = self._pageobj["header_border_options"]
        #     self.value_header_border().click()
        #     eles = self._findeles(css_eles)
        #     for i in eles:
        #         option_eles.append(i)
        #         options.append(i.text)
        #     self._log.logger(f"value_header_border options: {options}")
        #     for i in range(0, len(options)):
        #         target_dict[options[i]] = option_eles[i]
        #     return target_dict
        # except Exception as err:
        #     raise err and self._log.logger_error(err)

    def value_header_border_setting(self):
        """
        usage: value_header_border_set().click()
        :return: element
        """
        try:
            border_ele = self.value_header_border()
            set_container = self.nextele(border_ele)
            border_set = self.childele(set_container, 2)
            return border_set
        except Exception as e:
            raise e and self._log.logger_error(e)

    def value_header_border_setting_innerdel(self):
        setting_ele = self.value_header_border_setting()
        delete_btn = setting_ele.find_element_by_css_selector('i[aria-label="icon: close-circle"]')
        return delete_btn

    def value_header_border_setting_options(self):
        options = {}
        sleep(2)
        left_border = self._findeles(self._pageobj["header_border_set_options"])[0]
        right_border = self._findeles(self._pageobj["header_border_set_options"])[1]
        options["left_border"] = left_border
        options["right_border"] = right_border
        self._log.logger_debug(f"value_header_border_set_options:{options}")
        return options

    def value_header_border_delete(self):
        """
        usage: value_header_border_delete().click()
        :return: element
        """
        try:
            css = self._pageobj["header_border_delete_icon"]
            ele = self._findele(css)
            return ele
        except Exception as e:
            raise e and self._log.logger_error(e)

    def values(self):
        """
        usage: values().click()
        :return: element
        """
        try:
            eles = self.values_all()
            ele = self.nextele(self._contains(eles, "Values"))
            target = self.childele(ele, 1)
            return target
        except Exception as err:
            raise err and self._log.logger_error(err)

    def values_options(self):
        """
        # before searching / clicking on options, click on the selection drop-down first.
        # values_options()["options"]
        :return: dict

        """
        option_eles = []
        options = []
        target_dict = {}
        try:
            ele = self.values()
            aria_controls = ele.get_attribute("aria-controls")
            self._log.logger_debug(f'value options_aria_controls: {aria_controls}')
            css = self.get_ariacontrols_id(aria_controls)
            eles = self._findeles(css)
            for i in eles:
                option_eles.append(i)
                options.append(i.text)
            self._log.logger_debug(f"values options: {options}")
            for i in range(0, len(options)):
                target_dict[options[i]] = option_eles[i]
            return target_dict
        except Exception as err:
            raise err and self._log.logger_error(err)

    def hide(self):
        try:
            eles = self.values_all()
            ele = self.nextele(self._contains(eles, "Hide"))
            target = self.childele(ele, 1)
            return target
        except Exception as err:
            raise err and self._log.logger_error(err)

    def empty_cell_value(self):
        # Empty cell value input
        try:
            eles = self.values_all()
            ele = self.nextele(self._contains(eles, "Empty Cell Value"))
            target = self.childele(ele, 1)
            return target
        except Exception as err:
            raise err and self._log.logger_error(err)

    def show_percent_total(self):
        # show percent total toggle
        try:
            eles = self.values_all()
            ele = self._contains(eles, "Show Percent of Total")
            targetele = self.childele(self.nextele(ele), 1)
            return targetele
        except Exception as err:
            raise err and self._log.logger_error(err)

    def view_as(self):
        # view_As drop-down
        try:
            eles = self.values_all()
            ele = self.nextele(self._contains(eles, "View As"))
            target = self.childele(ele, 1)
            self.common.scroll_to(target)
            return target
        except Exception as err:
            raise err and self._log.logger_error(err)

    def view_as_options(self):
        """
        # before searching / clicking on options, click on the selection drop-down first.
        # view_as_options()["options"]
        :return: dict

        """
        option_eles = []
        options = []
        target_dict = {}
        try:
            ele = self.view_as()
            aria_controls = ele.get_attribute("aria-controls")
            self._log.logger_debug(f'view as options_aria_controls: {aria_controls}')
            css = self.get_ariacontrols_id(aria_controls)
            eles = self._findeles(css)
            for i in eles:
                option_eles.append(i)
                options.append(i.text)
            self._log.logger_debug(f"values options: {options}")
            for i in range(0, len(options)):
                target_dict[options[i]] = option_eles[i]
            return target_dict
        except Exception as err:
            raise err and self._log.logger_error(err)

    def view_as_bar(self):
        """
        will return view as _ bar elements:
                bar_color_btn, display_mode_toggle, min_dropdown, max_dropdown, types_dropdown, addnew_btn
        usage： view_as_bar()["options"]
        :return: dict
        """
        options = {}
        try:
            min_dropdown_css = self._pageobj["view_as_min"]
            max_dropdown_css = self._pageobj["view_as_max"]
            addnew_btn_css = self._pageobj["view_as_bar_addNew_btn"]

            all_ele = self.values_all()
            bar_color = self._contains(all_ele, "Bar Color")
            types = self._contains(all_ele, "Types")
            display_mode = self._contains(all_ele, "Display Mode")

            bar_color_btn = self.nextele(bar_color)
            display_mode_toggle = self.nextele(display_mode)
            min_dropdown = self._findele(min_dropdown_css)
            max_dropdown = self._findele(max_dropdown_css)
            types_dropdown = self.childele(self.nextele(types), 1)
            addnew_btn = self._findele(addnew_btn_css)

            options["bar_color_btn"] = bar_color_btn
            options["display_mode_toggle"] = display_mode_toggle
            options["min_dropdown"] = min_dropdown
            options["max_dropdown"] = max_dropdown
            options["types_dropdown"] = types_dropdown
            options["addnew_btn"] = addnew_btn
            self._log.logger_debug(f"view_as_bar eles: {options}")
            return options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_min_options(self):
        """
        ?????
        :return: []

        """
        try:
            min_dropdown = self.view_as_bar()["min_dropdown"]
            min_ariacontrols = min_dropdown.get_attribute("aria-controls")
            min_dropdown_options_css = self.get_ariacontrols_id(min_ariacontrols)
            min_options = self._findeles(min_dropdown_options_css)
            self._log.logger_debug(f"view_as_bar_min_options: {min_options}")
            return min_options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_max_options(self):
        """
        ?????
        :return: []

        """
        try:
            max_dropdown = self.view_as_bar()["max_dropdown"]
            max_ariacontrols = max_dropdown.get_attribute("aria-controls")
            self._log.logger(f"max_ariacontrols: {max_ariacontrols}")
            max_dropdown_options_css = self.get_ariacontrols_id(max_ariacontrols)
            max_options = self._findeles(max_dropdown_options_css)
            self._log.logger_debug(f"view_as_bar_min_options: {max_options}")
            return max_options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_types_options(self):
        """
        0 for values, 1 for variables
        :return: []
        """
        try:
            types_dropdown = self.view_as_bar()['types_dropdown']
            types_ariacontrols = types_dropdown.get_attribute("aria-controls")
            self._log.logger(f"types_ariacontrols: {types_ariacontrols}")
            types_dropdown_options_css = self.get_ariacontrols_id(types_ariacontrols)
            types_options = self._findeles(types_dropdown_options_css)
            self._log.logger_debug(f"view_as_bar_types_options: {types_options}")
            return types_options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_controls(self):
        """
        counts depend on customer added
        :return: []
        """
        try:
            view_as_bar_controls_css = self._pageobj["view_as_bar_controls"]
            view_as_bar_controls = self._findeles(view_as_bar_controls_css)
            return view_as_bar_controls
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_controls_component(self, num):
        """
        color_picker, condition, value, delete
        :param num: control which to be selected
        :return: dict
        """
        options = {}
        try:
            color_pick_css = self._pageobj["view_as_bar_controls_color-picker"]
            condition_css = self._pageobj["view_as_bar_controls_condition"]
            value_css = self._pageobj["view_as_bar_controls_values"]
            delete_css = self._pageobj["view_as_bar_controls_delete"]
            var_css = self._pageobj["view_as_bar_controls_var"]
            control = self.view_as_bar_controls()[num - 1]
            color_picker = control.find_element_by_css_selector(color_pick_css)
            condition = control.find_element_by_css_selector(condition_css)
            value = control.find_element_by_css_selector(value_css)
            delete = control.find_element_by_css_selector(delete_css)
            var_dropdown = control.find_element_by_css_selector(var_css)
            options["color_picker"] = color_picker
            options["condition"] = condition
            options["value"] = value
            options["delete"] = delete
            options["var_dropdown"] = var_dropdown
            self._log.logger_debug(f"view_as_bar_controls_component: {options}")
            return options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_controls_condition_options(self, num):
        """
        0,1,2,3,4: >, <, =, >=, <=
        usage: view_as_bar_controls_condition_options[0-4]
        :param num: control which to be selected
        :return: []
        """
        try:
            condition_dropdown = self.childele(self.view_as_bar_controls_component(num)["condition"], 1)
            condition_ariacontrols = condition_dropdown.get_attribute("aria-controls")
            self._log.logger_debug(f"condition_ariacontrols: {condition_ariacontrols}")
            condition_ariacontrols_css = self.get_ariacontrols_id(condition_ariacontrols)
            contidion_options = self._findeles(condition_ariacontrols_css)
            self._log.logger_debug(f"view_as_bar_controls_condition_options: {contidion_options}")
            return contidion_options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_controls_var_targetfield_options(self, num):
        """

        :return: {}
        """
        dropdown = self.view_as_bar_controls_component(num)["var_dropdown"]
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_bar_controls_var_aggregation(self):
        dropdown_css = self._pageobj["view_as_dropdown"]
        all_ele = self.values_all()
        ele_text = "Aggregation"
        ele = self.nextele(self._contains(all_ele, ele_text))
        target_ele = ele.find_element_by_css_selector(dropdown_css)
        return target_ele

    def view_as_bar_controls_var_aggregation_options(self):
        ele = self.view_as_bar_controls_var_aggregation()
        options = self.common.get_dropdown_options(ele)
        return options

    def view_as_bar_displayvalue(self):
        try:
            all_ele = self.values_all()
            display_value = self._contains(all_ele, "Display Value")
            self.common.scroll_to(display_value)
            display_value_toggle = self.nextele(display_value)
            return display_value_toggle
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_unitconversion(self):
        """
        Auto toggle, Unit toggle, unit dropdown, display unit toggle, decimal toggle, decimal input/ dropdown,
        separator dropdown, prefix input, suffix input, format btns, format color, format size, harizontal alignemnt btns
        :return: dict
        """
        options = {}
        try:
            decimal_input_css = self._pageobj["view_as_bar_unitconversion_Decimal_input"]
            prefix_inpput_css = self._pageobj["view_as_bar_unitconversion_Prefix_inpput"]
            suffix_inpput_css = self._pageobj["view_as_bar_unitconversion_Suffix_inpput"]
            format_bold_css = self._pageobj["view_as_bar_unitconversion_format_bold_css"]
            format_italic_css = self._pageobj["view_as_bar_unitconversion_format_italic_css"]
            format_underline_css = self._pageobj["view_as_bar_unitconversion_format_underline_css"]
            format_colorpicker_css = self._pageobj["view_as_bar_unitconversion_format_colorPicker_css"]
            format_size_css = self._pageobj["view_as_bar_unitconversion_format_siez_css"]
            alignment_left_css = self._pageobj["view_as_bar_alignment_left"]
            alignment_center_css = self._pageobj["view_as_bar_alignment_center"]
            alignment_right_css = self._pageobj["view_as_bar_alignment_right"]
            all_ele = self.values_all()
            options["auto_toggle"] = self.nextele(self._contains(all_ele, "Auto")) \
                .find_element_by_css_selector("button")
            options["unit_toggle"] = self.nextele(self.parentnode(self._contains(all_ele, "Unit"))) \
                .find_element_by_css_selector("button")
            options["display_unit_toggle"] = self.nextele(self._contains(all_ele, "Display Unit")) \
                .find_element_by_css_selector("button")
            options["unit_dropdown"] = self.nextele(self.parentnode(self.parentnode(self._contains(all_ele, "Unit")))) \
                .find_element_by_css_selector(".ant-select-selection--single")
            options["Decimal_toggle"] = self.nextele(self.parentnode(self._contains(all_ele, "Decimal"))) \
                .find_element_by_css_selector("button")
            options["Decimal_input"] = self._findele(decimal_input_css).find_element_by_css_selector("input")
            # Decimal_dropdown only available with decimal = dynamic, added to options set to direct select options

            options["Separator_dropdown"] = self.nextele(self.parentnode(self._contains(all_ele, "Separator"))) \
                .find_element_by_css_selector(".ant-select-selection--single")
            # options["Prefix_inpput"] = self.nextele(self.parentnode(self._contains(all_ele, "Prefix"))) \
            #     .find_element_by_css_selector("input")
            options["Prefix_inpput"] = self._findele(prefix_inpput_css)
            options["Suffix_inpput"] = self._findele(suffix_inpput_css)
            options["format_bold_btn"] = self._findele(format_bold_css)
            options["format_italic_btn"] = self._findele(format_italic_css)
            options["format_underline_btn"] = self._findele(format_underline_css)
            options["format_colorpicker_btn"] = self._findele(format_colorpicker_css)
            options["format_size"] = self._findele(format_size_css)
            options["Alignment_left"] = self._findele(alignment_left_css)
            options["Alignment_center"] = self._findele(alignment_center_css)
            options["Alignment_right"] = self._findele(alignment_right_css)
            return options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_unitconversion_unit_options(self):
        """
        static: [default, K, Mn, Bn, %]
        Dynamic: dynamic
        :return:[]
        """
        options = []
        try:
            unit_dropdown = self.view_as_bar_unitconversion()["unit_dropdown"]
            aria_control = unit_dropdown.get_attribute("aria-controls")
            options_css = self.get_ariacontrols_id(aria_control)
            for i in self._findeles(options_css):
                options.append(i)
            self._log.logger_debug(f"view_as_bar_unitconversion_unit_options: {options}")
            return options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_bar_unitconversion_decimal_dropdown(self):
        dropdown_css = self._pageobj["view_as_dropdown"]
        all_ele = self.values_all()
        ele = self.nextele(
            self.parentnode(self.parentnode(self._contains(all_ele, "Decimal")))).find_element_by_css_selector(
            dropdown_css)
        return ele

    def view_as_bar_unitconversion_decimal_options(self):
        """
        Dynamic: dynamic
        :return:[]
        """
        decimal_dropdown = self.view_as_bar_unitconversion_decimal_dropdown()
        options = self.common.get_dropdown_options(decimal_dropdown)
        return options

    def view_as_bar_unitconversion_separator_options(self):
        """
        #### # ### #,###
        :return:[]
        """
        unit_dropdown = self.view_as_bar_unitconversion()["Separator_dropdown"]
        options = self.common.get_dropdown_options(unit_dropdown)
        return options

    def view_as_bar_unitconversion_size_options(self):
        """
        #### # ### #,###
        :return:[]
        """
        options = []
        try:
            unit_dropdown = self.view_as_bar_unitconversion()["format_size"]
            aria_control = unit_dropdown.get_attribute("aria-controls")
            options_css = self.get_ariacontrols_id(aria_control)
            for i in self._findeles(options_css):
                options.append(i)
            self._log.logger_debug(f"view_as_bar_unitconversion_size_options: {options}")
            return options
        except Exception as e:
            raise e and self._log.logger_error(e)

    def view_as_indicator_style_dropdown(self):
        all_ele = self.values_all()
        dropdown_css = self._pageobj["view_as_indicator_Dropdown"]
        dropdown = self.nextele(self._contains(all_ele, "Style")) \
            .find_element_by_css_selector(dropdown_css)
        return dropdown

    def view_as_indicator_style_dropdown_options(self):
        """
        will return indicator - style options
        :return: {}
        """
        dropdown = self.view_as_indicator_style_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        self._log.logger_debug(f"indicator style count: {len(options)}")
        return options

    def view_as_indicator_size_dropdown(self):
        all_ele = self.values_all()
        dropdown_css = self._pageobj["view_as_indicator_Dropdown"]
        dropdown = self.nextele(self._contains(all_ele, "Size")) \
            .find_element_by_css_selector(dropdown_css)
        return dropdown

    def view_as_indicator_size_dropdown_options(self):
        """
        will return indicator - size options
        :return: {}
        """
        dropdown = self.view_as_indicator_size_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_indicator_type_dropdown(self):
        all_ele = self.values_all()
        dropdown_css = self._pageobj["view_as_indicator_Dropdown"]
        dropdown = self.nextele(self._contains(all_ele, "Type")) \
            .find_element_by_css_selector(dropdown_css)
        return dropdown

    def view_as_indicator_type_dropdown_options(self):
        """
        will return indicator - type options
        :return: {}
        """
        dropdown = self.view_as_indicator_type_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        self._log.logger_debug(f"indicator type options: {options.keys()}")
        return options

    def view_as_indicator_control_addbtn(self):
        """
        Add set condition to indicator
        :return: element
        """

        all_ele = self.values_all()
        addbtn = self.parentnode(self._contains(all_ele, "Add"))
        return addbtn

    def view_as_indicator_control_styledropdown(self, num=1):
        dropdown_css = self._pageobj["view_as_indicator_Dropdown"]
        view_as_indicator_control = self.dom.child_ele_all(self.parentnode(self.view_as_indicator_control_addbtn()))[
            num]
        ele = view_as_indicator_control.find_elements_by_css_selector(".ant-row-flex")[0].find_elements_by_css_selector(
            ".ant-col")[0].find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_indicator_control_styledropdown_options(self, num=1):
        dropdown = self.view_as_indicator_control_styledropdown(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_indicator_control_colorpicker(self, num=1):
        view_as_indicator_control = self.dom.child_ele_all(self.parentnode(self.view_as_indicator_control_addbtn()))[
            num]
        ele = view_as_indicator_control.find_elements_by_css_selector(".ant-row-flex")[0].find_elements_by_css_selector(
            ".ant-col")[1]
        return ele

    def view_as_indicator_control_condition(self, num=1):
        dropdown_css = self._pageobj["view_as_indicator_Dropdown"]
        view_as_indicator_control = self.dom.child_ele_all(self.parentnode(self.view_as_indicator_control_addbtn()))[
            num]
        ele = view_as_indicator_control.find_elements_by_css_selector(".ant-row-flex")[0].find_elements_by_css_selector(
            ".ant-col")[3].find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_indicator_control_condition_options(self, num=1):
        dropdown = self.view_as_indicator_control_condition(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_indicator_control_input(self, num=1):
        view_as_indicator_control = self.dom.child_ele_all(self.parentnode(self.view_as_indicator_control_addbtn()))[
            num]
        ele = view_as_indicator_control.find_elements_by_css_selector(".ant-row-flex")[0].find_elements_by_css_selector(
            ".ant-col")[4].find_element_by_css_selector("input")
        return ele

    def view_as_indicator_control_vardropdown(self, num=1):
        dropdown_css = self._pageobj["view_as_indicator_Dropdown"]
        view_as_indicator_control = self.dom.child_ele_all(self.parentnode(self.view_as_indicator_control_addbtn()))[
            num]
        ele = view_as_indicator_control.find_elements_by_css_selector(".ant-row-flex")[0].find_elements_by_css_selector(
            ".ant-col")[4].find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_indicator_control_vardropdown_options(self, num=1):
        dropdown = self.view_as_indicator_control_vardropdown(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_indicator_control_delete(self):
        view_as_indicator_control_delete = self.childele(self.nextele(self.view_as_indicator_control_addbtn()), 2)
        return view_as_indicator_control_delete

    def view_as_indicator_showvalue_toggle(self):
        """
        :return: {}
        """
        toggle = {}
        all_ele = self.values_all()
        toggle["Show Value Border"] = self.nextele(self._contains(all_ele, "Show Value Border")) \
            .find_element_by_css_selector("button")
        toggle["Show Value Labels"] = self.nextele(self._contains(all_ele, "Show Value Labels")) \
            .find_element_by_css_selector("button")
        return toggle

    def view_as_indicator_showvalue_border(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Border Margin (%)")).find_element_by_css_selector("input")
        return ele

    def view_as_indicator_showvalue_format(self):
        """
        keys: format_bold_btn, format_italic_btn, format_underline_btn, format_colorpicker_btn, format_size
        :return: {}
        """
        return self.common.format_setting()

    def view_as_indicator_showvalue_format_sizeoptions(self):
        """
        options{}
        """
        return self.common.format_setting_size_options()

    def view_as_indicator_showvalue_format_position(self, position):

        return self.common.format_setting_position(position)

    def view_as_starrate_fullstar_input(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Full Stars")).find_element_by_css_selector("input")
        return ele

    def view_as_starrate_fullscore_input(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Full Score")).find_element_by_css_selector("input")
        return ele

    def view_as_starrate_roundness_dropdown(self):
        dropdown_css = self._pageobj["view_as_dropdown"]
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Roundness")).find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_starrate_roundness_dropdown_options(self):
        dropdown = self.view_as_starrate_roundness_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        self._log.logger_debug(f"view_as_starrate_roundness_dropdown_options: {options.keys()}")
        return options

    def view_as_starrate_control_addbtn(self):
        """
        Add set condition
        :return: element
        """

        all_ele = self.values_all()
        addbtn = self.parentnode(self._contains(all_ele, "Add New"))
        return addbtn

    def view_as_starrate_control_container(self, num):
        colorpicker_css = self._pageobj["view_as_color_pickercontainer"]
        ele = self.parentnode(self._findeles(colorpicker_css)[num - 1])
        return ele

    def view_as_starrate_control_colorpicker(self, num):
        container = self.view_as_starrate_control_container(num)
        colorpicker_css = self._pageobj["view_as_color_pickercontainer"]
        colorpicker_btn = container.find_element_by_css_selector(colorpicker_css)
        return colorpicker_btn

    def view_as_starrate_control_condition_dropdown(self, num):
        container = self.view_as_starrate_control_container(num)
        dropdown_css = self._pageobj["view_as_dropdown"]
        dropdown = container.find_element_by_css_selector(dropdown_css)
        return dropdown

    def view_as_starrate_control_var_dropdown(self, num):
        """
        [0] for condition, [1] for var
        :param num:
        :return:
        """
        container = self.view_as_starrate_control_container(num)
        dropdown_css = self._pageobj["view_as_dropdown"]
        dropdown = container.find_elements_by_css_selector(dropdown_css)
        return dropdown

    def view_as_starrate_control_var_dropdown_options_var(self, num):
        dropdown = self.view_as_starrate_control_var_dropdown(num)[1]
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_starrate_control_var_dropdown_options_condition(self, num):
        dropdown = self.view_as_starrate_control_var_dropdown(num)[0]
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_starrate_control_condition_dropdown_options(self, num):
        dropdown = self.view_as_starrate_control_condition_dropdown(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_starrate_control_aggregation(self, num):
        css = self._pageobj["view_as_starRate_aggregation_dropdown"]
        dropdown_css = self._pageobj["view_as_dropdown"]
        container = self._findeles(css)[num - 1]
        dropdown = container.find_element_by_css_selector(dropdown_css)
        return dropdown

    def view_as_starrate_control_aggregation_options(self, num):
        dropdown = self.view_as_starrate_control_aggregation(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_starrate_control_condition_input(self, num):
        container = self.view_as_starrate_control_container(num)
        condition_input = container.find_element_by_css_selector("input")
        return condition_input

    def view_as_starrate_control_delete(self, num):
        container = self.view_as_starrate_control_container(num)
        delete_icon_css = self._pageobj["view_as_icon_delete"]
        control_delete = self.parentnode(container.find_element_by_css_selector(delete_icon_css))
        return control_delete

    def view_as_starrate_size_input(self):
        all_ele = self.values_all()
        size_span = self._contains(all_ele, "Size")
        size_container = self.parentnode(size_span)
        size_input = size_container.find_element_by_css_selector("input")
        return size_input

    def view_as_starrate_overallscore_toggle(self):
        all_ele = self.values_all()
        toggle = self.nextele(self._contains(all_ele, "Overall Score")) \
            .find_element_by_css_selector("button")
        return toggle

    def view_as_colorcoding_type_dropdown(self):
        dropdown_css = self._pageobj['view_as_dropdown']
        all_ele = self.values_all()
        dropdown = self.nextele(self._contains(all_ele, "Type")) \
            .find_element_by_css_selector(dropdown_css)
        return dropdown

    def view_as_colorcoding_type_dropdown_options(self):
        """
        values, Variables, with reference
        :return:{}
        """
        dropdown = self.view_as_colorcoding_type_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        self._log.logger_debug(f"view_as_colorcoding_type_dropdown_options: {options.keys()}")
        return options

    def view_as_colorcoding_control_variables_colorpicker(self):
        """
        variables_control has 2 color picker
        :return: [] 0 for first one(bgc), 1 for second one(font)
        """
        container = self.childele(self.nextele(self.view_as_add_btn()), 1)
        eles = container.find_elements_by_css_selector(".ant-col")
        return eles

    def view_as_colorcoding_control_variables_condition_dropdown(self):
        drppdown_css = self._pageobj["view_as_dropdown"]
        container = self.childele(self.nextele(self.view_as_add_btn()), 1)
        ele = container.find_elements_by_css_selector(drppdown_css)[0]
        return ele

    def view_as_colorcoding_control_variables_condition_dropdown_options(self):
        drppdown = self.view_as_colorcoding_control_variables_condition_dropdown()
        options = self.common.get_dropdown_options(drppdown)
        self._log.logger(f"view_as_colorcoding_control_variables_condition_dropdown_options count: {len(options)}")
        return options

    def view_as_colorcoding_control_variables_condition_measures_dropdown(self):
        drppdown_css = self._pageobj["view_as_dropdown"]
        container = self.childele(self.nextele(self.view_as_add_btn()), 1)
        ele = container.find_elements_by_css_selector(drppdown_css)[1]
        return ele

    def view_as_colorcoding_control_variables_condition_measures_dropdown_options(self):
        """
        :return:{}
        """
        drppdown = self.view_as_colorcoding_control_variables_condition_measures_dropdown()
        options = self.common.get_dropdown_options(drppdown)
        self._log.logger_debug(
            f"view_as_colorcoding_control_variables_condition_measures_dropdown_options: {options.keys()}")
        return options

    def view_as_colorcoding_control_variables_condition_method_dropdown(self):
        drppdown_css = self._pageobj["view_as_dropdown"]
        container = self.childele(self.nextele(self.view_as_add_btn()), 1)
        ele = container.find_elements_by_css_selector(drppdown_css)[1]
        return ele

    def view_as_colorcoding_control_variables_condition_method_dropdown_options(self):
        """
        :return:{}
        """
        drppdown = self.view_as_colorcoding_control_variables_condition_method_dropdown()
        options = self.common.get_dropdown_options(drppdown)
        self._log.logger_debug(
            f"view_as_colorcoding_control_variables_condition_method_dropdown_options: {options.keys()}")
        return options

    def view_as_colorcoding_control_variables_delete(self):
        delete_icon_css = self._pageobj["view_as_icon_delete"]
        container = self.nextele(self.view_as_add_btn())
        delete_icon = container.find_element_by_css_selector(delete_icon_css)
        return delete_icon

    def view_as_colorCoding_control_values_container(self, num):
        containerCss = self._pageobj["handle_colorCoding_values_control_container"]
        container = self.dom.findelements(containerCss)
        return container[num - 1]

    def view_as_colorcoding_control_values_bcColorpicker(self, num):
        container = self.view_as_colorCoding_control_values_container(num)
        elements = self.dom.child_ele_all(container)
        color_picker_ele = elements[0]
        return color_picker_ele

    def view_as_colorcoding_control_values_fontColorpicker(self, num):
        container = self.view_as_colorCoding_control_values_container(num)
        elements = self.dom.child_ele_all(container)
        color_picker_ele = elements[1]
        return color_picker_ele

    def view_as_colorcoding_control_values_condition_dropdown(self, num):
        drppdown_css = self._pageobj["view_as_dropdown"]
        container = self.view_as_colorCoding_control_values_container(num)
        elements = self.dom.child_ele_all(container)
        dropdown = elements[2].find_element_by_css_selector(drppdown_css)
        return dropdown

    def view_as_colorcoding_control_values_condition_dropdown_options(self, num):
        dropdown = self.view_as_colorcoding_control_values_condition_dropdown(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_colorcoding_control_values_input(self, num):
        container = self.view_as_colorCoding_control_values_container(num)
        ele = container.find_element_by_css_selector("input")
        return ele

    def view_as_colorcoding_control_values_delete(self, num):
        container = self.view_as_colorCoding_control_values_container(num)
        ele = container.find_element_by_css_selector("button")
        return ele

    def view_as_colorCoding_controlVar_container(self, num):
        container = self.dom.child_ele_all(self.parentnode(self.view_as_add_btn()))
        return container[num]

    def view_as_colorCoding_controlVar_bcgColor(self, num):
        container = self.view_as_colorCoding_controlVar_container(num)
        ele = container.find_elements_by_css_selector(".ant-col")
        return ele[1].find_element_by_css_selector("div")

    def view_as_colorCoding_controlVar_fontColor(self, num):
        container = self.view_as_colorCoding_controlVar_container(num)
        ele = container.find_elements_by_css_selector(".ant-col")
        return ele[2].find_element_by_css_selector("div")

    def view_as_colorCoding_controlVar_conditionDropdown(self, num):
        dropdownCss = self._pageobj["view_as_dropdown"]
        container = self.view_as_colorCoding_controlVar_container(num)
        ele = container.find_elements_by_css_selector(".ant-col")
        return ele[3].find_element_by_css_selector(dropdownCss)

    def view_as_colorCoding_controlVar_conditionDropdownOptions(self, num):
        dropdown = self.view_as_colorCoding_controlVar_conditionDropdown(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_colorCoding_controlVar_varDropdown(self, num):
        dropdownCss = self._pageobj["view_as_dropdown"]
        container = self.view_as_colorCoding_controlVar_container(num)
        ele = container.find_elements_by_css_selector(".ant-col")
        return ele[4].find_element_by_css_selector(dropdownCss)

    def view_as_colorCoding_controlVar_varDropdownOptions(self, num):
        dropdown = self.view_as_colorCoding_controlVar_varDropdown(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_colorCoding_controlVar_aggDropdown(self, num):
        dropdownCss = self._pageobj["view_as_dropdown"]
        container = self.view_as_colorCoding_controlVar_container(num)
        ele = container.find_elements_by_css_selector(".ant-col")
        return ele[4].find_element_by_css_selector(dropdownCss)

    def view_as_colorCoding_controlVar_aggDropdownOptions(self, num):
        dropdown = self.view_as_colorCoding_controlVar_aggDropdown(num)
        options = self.common.get_dropdown_options(dropdown)
        return options

    def view_as_gradientcolor_customize_toggle(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Customize")).find_element_by_css_selector("button")
        return ele

    def view_as_gradientcolor_customize_fontcolor(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Font Color")).find_element_by_css_selector("div")
        return ele

    def view_as_gradientcolor_customize_color_from_gradient(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Color From Gradient")).find_element_by_css_selector("div")
        return ele

    def view_as_gradientcolor_customize_color_to_gradient(self):
        all_ele = self.values_all()
        ele = self.nextele(self._contains(all_ele, "Color To Gradient")).find_element_by_css_selector("div")
        return ele

    def view_as_gradientcolor_theme_dropdown(self):
        dropdown_css = self._pageobj["view_as_dropdown"]
        all_ele = self.values_all()
        ele = self.nextele(self.parentnode(self._contains(all_ele, "Theme"))).find_element_by_css_selector(dropdown_css)
        return ele

    def view_as_gradientcolor_theme_options(self):
        # need return []
        dropdown = self.view_as_gradientcolor_theme_dropdown()
        options = self.common.get_dropdown_options(dropdown)
        return options

    def column_border(self):
        """
        col_border should be simple one, will do optimization in future
        :return:
        """
        try:
            all_ele = self.values_all()
            mid_ele = self._contains(all_ele, "Column Border")
            ele = self.nextele(mid_ele)
            return ele
        except Exception as e:
            raise e and self._log.logger_error(e)

    def column_border_options(self):
        """
        usage: column_border_options()["options"]
        :return: dict
        """
        option_eles = []
        options = []
        target_dict = {}
        try:
            css_eles = self._pageobj["column_border_options"]
            eles = self._findeles(css_eles)
            for i in eles:
                option_eles.append(i)
                options.append(i.text)
            self._log.logger_debug(f"column_border options: {options}")
            for i in range(0, len(options)):
                target_dict[options[i]] = option_eles[i]
            return target_dict
        except Exception as err:
            raise err and self._log.logger_error(err)

    def column_border_setting(self):
        border_ele = self.column_border()
        set_container = self.nextele(self.nextele(border_ele))
        border_set = self.childele(set_container, 2)
        return border_set

    def column_border_setting_options(self):
        """
        left_border, right_border
        usage: column_border_set_options()["options"]
        :return:
        """
        options = {}
        left_border = self._findeles(self._pageobj["column_border_set_options"])[0]
        right_border = self._findeles(self._pageobj["column_border_set_options"])[1]
        options["left_border"] = left_border
        options["right_border"] = right_border
        return options


    def get_ariacontrols_id(self, aria):
        """
        find the drop-down options value
        :param aria: aria-controls id
        :return: css
        """
        css = ''
        try:
            if aria[0].isalpha():
                css = "#" + aria + " li"
            elif aria[0].isnumeric():
                css = "#\\3" + aria[0] + ' ' + aria[1:] + " li"
            return css
        except Exception as e:
            raise e and self._log.logger_error(e)


    def unit_conversion(self):
        pass


    def view_as_value_format_suffix(self):
        try:
            eles = self.values_all()
            ele = self.nextele(self._contains(eles, "Suffix"))
            return ele
        except Exception as err:
            raise err and self._log.logger_error(err)
