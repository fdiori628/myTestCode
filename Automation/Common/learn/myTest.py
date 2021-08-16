from Common.root_until import RootUntil
import unittest
from selenium import webdriver


class TestCase(unittest.TestCase):

    def setUp(self):
        self._driverpath = RootUntil().get_driver
        print(self._driverpath)
        self._driver = webdriver.Chrome(self._driverpath)

    def test_01_case(self):
        self._driver.get('http://www.baidu.com')


if __name__ == '__main__':
    print('test')
    unittest.main()

