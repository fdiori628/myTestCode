from Common.web_config_until import WebConfig
from Components.Component.VisibilityLayer.Dashboard.ChartEdit import ChartEdit
from time import sleep
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


class Sort(Common):

    def __init__(self, _driver):
        Common.__init__(self, _driver)
        self._webconfig = WebConfig('Properties_common/sort')
        self._pageobj = self._webconfig.domelements

    def sort_as_sortinginbackend_toggle(self):
        all_ele = self.all_element()
        toggle = self.next_ele(self.contains(all_ele, "Sort in Backend")) \
            .find_element_by_css_selector("button")
        sleep(1)
        self.scroll_to(toggle)
        return toggle

    def sorting_field(self, name, sort_name='', sign=False):
        """
        sort_field 业务有两种情况 一种是打开上面的开关 一种是不打开上面的开关
        :param name: 下拉框需要选择的值
        :param sort_name:
        :param sign: 如果是False 排序方式默认，如果是True 可以传sort_name 选择排序方式
        :return:
        """

        all = self.all_element()
        toggle = self.next_ele(self.contains(all, "Pivot Sorting")) \
            .find_element_by_css_selector("button").get_attribute("aria-checked")
        # print(toggle)
        if toggle == "true":
            sort_field = self.contains(all, 'Sorting Field')
            s = self._pageobj["sorting_field"]
            drop = self.next_ele(sort_field).find_element_by_css_selector(s)
            drop.click()
            sleep(1)
            self.get_dropdown_options(drop)[name].click()
        else:
            sort_field = self.contains(all, 'Sort Field')
            s = self._pageobj["sorting_column"]
            drop = self.next_ele(sort_field).find_element_by_css_selector(s)
            drop.click()
            sleep(1)
            self.get_dropdown_options(drop)[name].click()
            drop.click()
            if sign:
                xpth = '//span[contains(text(), "' + sort_name + '")]/preceding-sibling::span'
                self.driver.find_element_by_xpath(xpth).click()
        return toggle

    def sort_by(self, name, name1, sign=True):
        all = self.all_element()
        sort_field = self.contains(all, 'Sort By')
        s = self._pageobj["sort_by"]
        drop = self.next_ele(sort_field).find_element_by_css_selector(s)
        drop.click()
        sleep(1)
        self.get_dropdown_options(drop)[name].click()
        if sign:
            s = self._pageobj["Sort_by"]
            drop = self.next_ele(self.parentnode(sort_field)).find_element_by_css_selector(s)
            drop.click()
            sleep(1)
            self.get_dropdown_options(drop)[name1].click()

    def ascend_or_descend(self, sort_name):
        xpth = '//span[contains(text(), "' + sort_name + '")]/preceding-sibling::span'
        self.driver.find_element_by_xpath(xpth).click()

    def sorting_column(self, list_name):
        all = self.all_element()
        sort_field = self.contains(all, 'Sorting Column')
        s = self._pageobj["sorting_column"]
        drop = self.next_ele(sort_field).find_element_by_css_selector(s)
        drop.click()
        sleep(1)
        for i in list_name:
            self.get_dropdown_options(drop)[i].click()
        drop.click()
