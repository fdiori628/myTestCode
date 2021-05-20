from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def myFindElement(driver, cssSelector, timeout, timeSeq):
    try:
        WebDriverWait(driver, timeout, timeSeq).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
        element = driver.find_element_by_css_selector(cssSelector)
    except BaseException as e:
        raise e
    return element
