from selenium import webdriver
import pytest


def test_a():
    chrome_driver = './Drivers/chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver)
    driver.get('http://www.baidu.com')
    title = driver.title
    assert title == "百度一下，你就知道"


if __name__ == '__main__':
    pytest.main("-s test_1.py")
