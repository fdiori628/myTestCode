from Common.web_config_until import WebConfig
from time import sleep
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


class RowHeaders(Common):

    def __init__(self, _driver):
        Common.__init__(self, _driver)
        self._webconfig = WebConfig('Properties_common/row_headers')
        self._pageobj = self._webconfig.domelements

    def rotation_horizontal(self):
        hor = self._pageobj["rotation_horizontal"]
        self.parentnode(self.findele(hor)).click()

    def rotation_up(self):
        hor = self._pageobj["rotation_up"]
        self.parentnode(self.findele(hor)).click()

    def rotation_down(self):
        hor = self._pageobj["rotation_down"]
        self.parentnode(self.findele(hor)).click()

    def rotation_right_down(self):
        hor = self._pageobj["rotation_right-down"]
        self.parentnode(self.findele(hor)).click()

    def rotation_right_up(self):
        hor = self._pageobj["rotation_right-up"]
        self.parentnode(self.findele(hor)).click()
