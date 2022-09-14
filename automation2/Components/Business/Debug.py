import time

from Login import BusinessLogin
from selenium import webdriver
from Common.root_until import RootUntil
from Common.dom_until import DomUntil
from Components.Business.Project import BusinessProject
from Components.Business.Dashboard import BusinessDashboard
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Components.Component.VisibilityLayer.Dashboard.Dashboard import Dashboard
from selenium.webdriver.common.action_chains import ActionChains
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from Components.Component.VisibilityLayer.Dashboard.Properties.values import Values
from Components.Component.VisibilityLayer.Dashboard.Properties.sort import Sort
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common

from selenium.webdriver.common.keys import Keys
from Components.Business.Properties import Properties

r = RootUntil()
driver_path = r.get_rootpath + '/Drivers/chromedriver'
driver = webdriver.Chrome(driver_path)
d = DomUntil(driver)
ac = ActionChains(driver)
c = ChartEdit(driver)
v = Values(driver)
s = Sort(driver)
y = Common(driver)
url = 'https://eyeguide-designer.essexlg.com/login'
url217 = "http://172.20.4.217:3002/login"
user = 'xingyang.han@essexlg.com'
pwd = '#BZNfdiori9'
pwd217 = "1qaz@WSX3edc"
#
# # BusinessLogin(driver, url, user, pwd).login()
# # project = BusinessProject(driver, url, user, pwd).visit_project("AutomationTest")
# driver.maximize_window()
p = Properties(driver, url217, user, pwd217, "AutomationTest").bussiness_values("Automation_visibilityLayer_pivotTable")

# get_attribute()
# driver.find_element_by_css_selector('').parent

t = 1

# y.toggle("Row Sorting").get_attribute()
y.tab_click("Sort")
y.toggle("Row Sorting")
time.sleep(4)
y.toggle("Pivot Sorting", sign=True)
time.sleep(2)
s.sorting_field(name='id', sort_name='Desc', sign=True)
time.sleep(2)
y.toggle("Row Sorting")
print("执行结束")

# s.sort_as_sortinginbackend_toggle().click()
#
# s.sorting_field('id')
# s.sorting_column(['id', 'name'])
# s.sort_by('Price', 'Sum Total')


# all = y.all_element()
# w = d.contains(all, 'Sorting Field')
# drop = d.next_ele(w).find_element_by_css_selector('.ant-select-selection--single')
# drop.click()
# sleep(1)
# y.get_dropdown_options(drop)['id'].click()
# s.sort_as_rowsorting_toggle().click()
# sleep(2)
# s.sort_as_sortingonios_toggle().click()
# sleep(2)
# s.sort_as_sortinginbackend_toggle().click()

# d.scroll_to(v.column_border())
# sleep(t)
# v.column_border().click()
# sleep(t)
# v.column_border_options()['Price'].click()
# sleep(t)
# v.column_border().click()
# sleep(t)
# v.column_border_set().click()
# sleep(t)
# v.column_border_set_options()["left_border"].click()
# sleep(t)
# v.column_border_set_options()["right_border"].click()
# sleep(t)
# v.occupy_whole_area().click()
# sleep(t)
# # v.hide_value_headers().click()
# # sleep(t)
# v.value_header_border_options()["Price"].click()
# sleep(t)
# v.value_header_border().click()
# sleep(t)
# v.value_header_border_set().click()
# sleep(t)
# v.value_header_border_set_options()["left_border"].click()
# sleep(t)
# v.value_header_border_set_options()["right_border"].click()
# sleep(t)
# v.value_header_border_set().click()
# sleep(t)
# v.value_header_border_delete().click()
# sleep(t)
# v.values().click()
# sleep(t)
# v.values_options()['Price(sum)'].click()
# sleep(t)
# v.empty_cell_value().clear()
# sleep(t)
# d.dely_input(ele=v.empty_cell_value(), input_data="test")
# sleep(t)
# v.show_percent_total().click()
# sleep(t)
# v.values().click()
# sleep(t)
# v.values_options()['Price(sum)'].click()
# sleep(t)
# d.scroll_to(v.view_as())
# sleep(t)
# v.view_as().click()
# sleep(t)


# ====================================================star rate==========
# v.view_as_options()["Star Rate"].click()
# sleep(t)
# v.view_as_starrate_fullstar_input().send_keys(3)
# sleep(t)
# d.dely_input(v.view_as_starrate_fullscore_input(), "50")
# sleep(t)
# v.view_as_starrate_roundness_dropdown().click()
# sleep(t)
# v.view_as_starrate_roundness_dropdown_options()["Round Down"].click()
# sleep(t)
# v.view_as_types_dropdown().click()
# sleep(t)
# v.view_as_types_dropdown_options()["Variables"].click()
# sleep(t)
# v.view_as_allowgroup_toggle()["Allow Group by Row"].click()
# sleep(t)
# v.view_as_allowgroup_toggle()["Allow Group by Col"].click()

# v.view_as_starrate_control_addbtn().click()
# sleep(t)
# v.view_as_starrate_control_colorpicker().click()
# sleep(t)
# v.view_as_starrate_control_condition_dropdown().click()
# sleep(t)
# v.view_as_starrate_control_condition_dropdown().click()
# sleep(t)
# v.view_as_starrate_control_condition_input().send_keys("1")
# sleep(t)
# v.view_as_starrate_control_delete().click()
#
# v.view_as_starrate_size_input().click()
# sleep(t)
# v.view_as_starrate_size_input().send_keys(Keys.DELETE)
# sleep(t)
# v.view_as_starrate_size_input().send_keys(Keys.DELETE)
# sleep(t)
# d.dely_input(v.view_as_starrate_size_input(), "12")
# v.view_as_starrate_overallscore_toggle().click()
# ====================================================color coding==========
# v.view_as_options()["Gradient Color"].click()
# sleep(t)
# v.view_as_colorcoding_type_dropdown().click()
# sleep(t)
# v.view_as_colorcoding_type_dropdown_options()["Variables"].click()
# sleep(t)
# v.view_as_add_btn().click()
# sleep(t)
# v.view_as_colorcoding_control_variables_colorpicker()[1].click()
# sleep(t)
# v.common.sketch_picker("#417505").click()
# sleep(t)
# v.view_as_colorcoding_control_variables_colorpicker()[1].click()
# sleep(t)
# v.common.sketch_picker("#417505")
# sleep(t)
# v.view_as_colorcoding_control_variables_condition_dropdown().click()
# sleep(t)
# v.view_as_colorcoding_control_variables_condition_dropdown_options()[">"].click()
# sleep(t)
# v.view_as_colorcoding_control_variables_condition_measures_dropdown().click()
# sleep(t)
# v.view_as_colorcoding_control_variables_condition_measures_dropdown_options()["date"].click()
# sleep(t)
# v.view_as_colorcoding_control_variables_condition_method_dropdown().click()
# sleep(t)
# v.view_as_colorcoding_control_variables_condition_method_dropdown_options()["Max"].click()
# sleep(t)
# v.view_as_colorcoding_control_delete().click()

# v.view_as_colorcoding_type_dropdown_options()["Values"].click()
# sleep(t)
# v.view_as_addnew_btn().click()
# sleep(t)
# v.view_as_colorcoding_type_dropdown_options()["Gradient Color"].click()
# sleep(t)
# v.view_as_addnew_btn().click()
# sleep(t)
# v.view_as_colorcoding_control_values_colorpicker()[1].click()
# sleep(t)
# v.common.sketch_picker("#417505").click()
# sleep(t)
# v.view_as_colorcoding_control_values_condition_dropdown().click()
# sleep(t)
# v.view_as_colorcoding_control_values_condition_dropdown_options()["<"].click()
# sleep(t)
# v.view_as_colorcoding_control_values_input().clear()
# sleep(t)
# v.view_as_colorcoding_control_values_input().send_keys("1")
# sleep(t)
# v.view_as_colorcoding_control_values_delete().click()

# v.view_as_unitconversion_auto_toggle().click()
# sleep(t)
# v.view_as_unitconversion_auto_toggle().click()
# sleep(t)
# v.view_as_unitconversion_displayunit_toggle().click()
# sleep(t)
# v.view_as_unitconversion_units_toggle().click()
# sleep(t)
# v.view_as_unitconversion_units_toggle().click()
# sleep(t)
# v.view_as_unitconversion_units_dropdown().click()
# sleep(t)
# v.view_as_unitconversion_units_options()["K"].click()
# sleep(t)
# v.view_as_unitconversion_decimal_input().send_keys(1)
# sleep(t)
# v.view_as_unitconversion_decimal_toggle().click()
# sleep(t)
# v.view_as_unitconversion_decimal_dropdown().click()
# sleep(t)
# v.view_as_unitconversion_decimal_options()["inventory"].click()
# ====================================================color coding==========

# ====================================================Gradient==========

# v.view_as_gradientcolor_customize_toggle().click()
# sleep(t)
# v.view_as_gradientcolor_customize_fontcolor().click()
# sleep(t)
# v.view_as_gradientcolor_customize_fontcolor().click()
# sleep(t)
# v.view_as_gradientcolor_customize_color_from_gradient().click()
# sleep(t)
# v.view_as_gradientcolor_customize_color_from_gradient().click()
# sleep(t)
# v.view_as_gradientcolor_customize_color_to_gradient().click()
# sleep(t)
# v.view_as_gradientcolor_theme_dropdown().click()
# sleep(t)
# v.view_as_gradientcolor_theme_options()


# ====================================================Gradient==========
# ==========================indicator======================================
# v.view_as_indicator_style_dropdown().click()
# sleep(t)
# v.view_as_indicator_style_dropdown_options()[3].click()
# sleep(t)
# v.view_as_indicator_size_dropdown().click()
# sleep(t)
# v.view_as_indicator_size_dropdown_options()["16px"].click()
# sleep(t)
# v.view_as_indicator_type_dropdown().click()
# sleep(t)
# v.view_as_indicator_type_dropdown_options()["Variables"].click()
# sleep(t)
# v.view_as_indicator_allowgroup_toggle()["Allow Group by Row"].click()
# sleep(t)
# v.view_as_indicator_allowgroup_toggle()["Allow Group by Col"].click()
# v.view_as_indicator_control_addbtn().click()
# sleep(t)
# d.findelement("i[aria-label='icon: delete']")
# sleep(t)
# v.view_as_indicator_control_styledropdown().click()
# sleep(t)
# v.view_as_indicator_control_colorpicker().click()
# sleep(t)
# v.view_as_indicator_control_condition().click()
# sleep(t)
# v.view_as_indicator_control_input().send_keys("12")
# sleep(t)
# v.view_as_indicator_control_delete().click()
# driver.find_element_by_css_selector()
# v.view_as_indicator_showvalue_toggle()["Show Value Border"].click()
# sleep(t)
# v.view_as_indicator_showvalue_toggle()["Show Value Labels"].click()
# sleep(t)
# v.view_as_indicator_showvalue_border().click()
# sleep(t)
# v.view_as_indicator_showvalue_border().clear()
# sleep(t)
# v.view_as_indicator_showvalue_format_position("left").click()
# sleep(t)
# v.view_as_indicator_showvalue_format_position("top").click()
# sleep(t)
# v.view_as_indicator_showvalue_format_position("right").click()
# sleep(t)
# v.view_as_indicator_showvalue_format_position("bottom").click()
# v.view_as_indicator_showvalue_border().send_keys("11")
# sleep(t)
# v.view_as_indicator_showvalue_format()["format_bold_btn"].click()
# sleep(t)
# v.view_as_indicator_showvalue_format()["format_italic_btn"].click()
# sleep(t)
# v.view_as_indicator_showvalue_format()["format_underline_btn"].click()
# sleep(t)
# v.view_as_indicator_showvalue_format()["format_colorpicker_btn"].click()
# sleep(t)
# v.common.sketch_picker("#417505").click()
# sleep(t)
# v.view_as_indicator_showvalue_format()["format_size"].click()
# sleep(t)
# v.view_as_indicator_showvalue_format_sizeoptions()["17px"].click()
# ==========================indicator============================================

# v.view_as_bar()["bar_color_btn"].click()
# sleep(t)
# v.view_as_sketchpicker("#417505").click()
# sleep(t)
# v.view_as_bar()["bar_color_btn"].click()
# sleep(t)
# v.view_as_bar()["display_mode_toggle"].click()
# sleep(t)
# v.view_as_bar()["min_dropdown"].click()
# sleep(t)
# v.view_as_bar_min_options()[1].click()
# sleep(t)
# v.view_as_bar()["max_dropdown"].click()
# sleep(t)
# v.view_as_bar_max_options()[1].click()
# v.view_as_bar()["types_dropdown"].click()
# sleep(t)
# v.view_as_bar_types_options()[1].click()
# sleep(t)
# v.view_as_bar()["addnew_btn"].click()
# sleep(t)
# v.view_as_bar()["addnew_btn"].click()
# sleep(t)
# v.view_as_bar_controls_component(1)['color_picker'].click()
# sleep(t)
# v.view_as_sketchpicker("#417505").click()
# sleep(t)
# v.view_as_bar_controls_component(1)['condition'].click()
# sleep(t)
# v.view_as_bar_controls_condition_options(1)[0].click()
# sleep(t)
# v.view_as_bar_controls_component(2)['condition'].click()
# sleep(t)
# v.view_as_bar_controls_condition_options(2)[3].click()
# sleep(t)
# v.view_as_bar_controls_component(2)['delete'].click()
# sleep(t)
# v.view_as_bar_displayvalue().click()
# v.view_as_bar_unitconversion()["unit_toggle"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["unit_dropdown"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["format_size"].click()
# sleep(t)
# v.view_as_bar_unitconversion_size_options()[14].click()
# sleep(t)
# v.view_as_bar_unitconversion()["Separator_dropdown"].click()
# sleep(t)
# v.view_as_bar_unitconversion_separator_options()[1].click()
# v.view_as_bar_unitconversion_unit_options()[2].click()
# v.view_as_bar_unitconversion()["format_bold_btn"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["format_italic_btn"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["format_underline_btn"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["format_colorpicker_btn"].click()
# sleep(t)
# v.view_as_sketchpicker("#417505").click()
# sleep(t)
# v.view_as_bar_unitconversion()["format_size"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["format_size"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["Alignment_left"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["Alignment_center"].click()
# sleep(t)
# v.view_as_bar_unitconversion()["Alignment_right"].click()
# v.view_as_bar_unitconversion()["unit_dropdown"].click()
# v.view_as_bar_unitconversion()["Decimal_toggle"].click()
# d.dely_input(v.view_as_bar_unitconversion()["Prefix_inpput"], "test")
# sleep(t)
# d.dely_input(v.view_as_bar_unitconversion()["Suffix_inpput"], "test")
# d.dely_input(ele=v.format_suffix(), input_data="suffix")
# sleep(t)


a = input()
driver.quit()