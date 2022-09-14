import time

from Common.web_config_until import WebConfig
from time import sleep
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


class ColumnHeader(Common):

    def __init__(self, _driver):
        Common.__init__(self, _driver)
        self._webconfig = WebConfig('Properties_common/column_header')
        self._pageobj = self._webconfig.domelements

    def bottom_border_width_0(self):
        bottom_border_width_0 = self._pageobj["bottom_border_width_0"]
        strong = self.parentnode(self.findele(bottom_border_width_0))
        strong.click()

    def bottom_border_width_2(self):
        bottom_border_width_0 = self._pageobj["bottom_border_width_2"]
        strong = self.parentnode(self.findele(bottom_border_width_0))
        strong.click()

    def bottom_border_width_3(self):
        bottom_border_width_0 = self._pageobj["bottom_border_width_3"]
        strong = self.parentnode(self.findele(bottom_border_width_0))
        strong.click()

    def bottom_border_width_5(self):
        bottom_border_width_0 = self._pageobj["bottom_border_width_5"]
        strong = self.parentnode(self.findele(bottom_border_width_0))
        strong.click()

    def background_color(self, ele_name, color):
        all_ele = self.all_element()
        bottom_border_color_css = self._pageobj["background_color"]
        bottom_border_color_box = self.next_ele(
            self.parentnode(self.contains(all_ele, ele_name))).find_element_by_css_selector(
            bottom_border_color_css)
        bottom_border_color_box.click()
        bottom_border_color_css = self.sketch_picker(color)
        time.sleep(2)
        bottom_border_color_css.click()
        bottom_border_color_box.click()

    def bottom_border_color(self, ele_name, color):
        all_ele = self.all_element()
        bottom_border_color_css = self._pageobj["bottom_border_color"]
        bottom_border_color_box = self.parentnode(self.contains(all_ele, ele_name)).find_element_by_css_selector(
            bottom_border_color_css)
        bottom_border_color_box.click()
        bottom_border_color_css = self.sketch_picker(color)
        time.sleep(2)
        bottom_border_color_css.click()
        bottom_border_color_box.click()
