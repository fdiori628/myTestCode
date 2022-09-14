import pytest
import allure
import time
from Components.Component.VisibilityLayer.Dashboard.Properties.sort import Sort
from Components.Component.VisibilityLayer.Dashboard.Properties.common import Common


@pytest.mark.usefixtures("pivtable")
class TestSort:

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    def test_sort_row_sorting(self, pivtable_handle_case):
        com = Common(pivtable_handle_case)
        sort = Sort(pivtable_handle_case)
        try:
            com.tab_click("Sort")
            com.toggle("Row Sorting")
            time.sleep(2)
            com.toggle("Pivot Sorting", sign=True)
            time.sleep(1)
            sort.sorting_field(name='id', sort_name='Desc', sign=True)
            time.sleep(2)
            assert com.assert_text()["id"] == sorted(com.assert_text()["id"], reverse=True), "排序方式不对"
            time.sleep(2)
            com.toggle("Row Sorting")
        except:
            # 后面做异常截图处理
            raise "error"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    def test_sort(self, pivtable_handle_case):
        com = Common(pivtable_handle_case)
        sort = Sort(pivtable_handle_case)
        try:
            com.tab_click("Sort")
            com.toggle("Row Sorting")
            sort.sorting_field(name='id')
            time.sleep(2)
            sort.ascend_or_descend("Descending")
            time.sleep(2)
            assert com.assert_text()["id"] == sorted(com.assert_text()["id"], reverse=True), "排序不对"
            com.toggle("Row Sorting")

        except Exception as e:
            raise e
