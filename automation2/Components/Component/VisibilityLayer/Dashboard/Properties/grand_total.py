from Common.web_config_until import WebConfig
from time import sleep
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


class GrandTotal(Common):

    def __init__(self, _driver):
        Common.__init__(self, _driver)
        self._webconfig = WebConfig('Properties_common/grand_total')
        self._pageobj = self._webconfig.domelements

    def strong(self, number):
        strong_css = self._pageobj["strong"]
        strong = self.parentnode(self.findeles(strong_css)[number])
        strong.click()

    def italic(self, number):
        italic_css = self._pageobj["italic"]
        italic = self.parentnode(self.findeles(italic_css)[number])
        italic.click()

    def underline(self, number):
        underline_css = self._pageobj["underline"]
        underline = self.parentnode(self.findeles(underline_css)[number])
        underline.click()
