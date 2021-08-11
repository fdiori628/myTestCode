from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DomUntil:

    @staticmethod
    def findelement(d, csselector, timeout, timeseq):
        try:
            WebDriverWait(d, timeout, timeseq).until(EC.presence_of_element_located((By.CSS_SELECTOR, csselector)))
            element = d.find_element_by_css_selector(csselector)
        except TimeoutError as err:
            raise err
        except Exception as e:
            raise (type(e), e)
        return element
