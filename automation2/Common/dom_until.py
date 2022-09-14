from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from time import sleep


class DomUntil:

    def __init__(self, driver):
        self.driver = driver

    def findelement(self, csselector, timeout=40, timeseq=1):
        try:
            WebDriverWait(self.driver, timeout, timeseq).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, csselector)))
            element = self.driver.find_element_by_css_selector(csselector)
            return element
        except TimeoutError as err:
            raise err
        except Exception as e:
            raise (type(e), e)

    def findelements(self, csselector, timeout=40, timeseq=1):
        try:
            WebDriverWait(self.driver, timeout, timeseq).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, csselector)))
            elements = self.driver.find_elements_by_css_selector(csselector)
            return elements
            # elements = self.driver.execute_script(
            #     """
            #         eles = document.querySelectorAll(arguments[0]);
            #         return eles;
            #
            #     """
            #     , csselector)
            # return elements

        except TimeoutError as err:
            raise err
        except Exception as e:
            raise (type(e), e)

    def wait_url(self, url_keyword, timeout=40, timeseq=1):
        try:
            result = WebDriverWait(self.driver, timeout, timeseq).until(EC.url_contains(url_keyword))
            return result
        except TimeoutError as err:
            raise err
        except Exception as e:
            raise (type(e), e)

    def contains(self, ele, name):
        # needs add timewait to ele or load the func findelements
        # ele should be arr eles / []
        try:
            targetele = self.driver.execute_script("""
                for(let i = 0; i < arguments[0].length; i++)
                {
                    if(arguments[0][i].innerHTML.trim() === arguments[1])
                    {
                        return arguments[0][i];
                    }
                }
            """, ele, name)
            return targetele
        except Exception as err:
            raise err

    def containsAll(self, ele, name):
        # needs add timewait to ele or load the func findelements
        # ele should be arr eles / []
        try:
            targeteles = self.driver.execute_script("""
                let eles = [];
                for(let i = 0; i < arguments[0].length; i++)
                {
                    if(arguments[0][i].innerHTML.trim() === arguments[1])
                    {
                        eles.push(arguments[0][i]);
                    }
                }
                return eles
            """, ele, name)
            return targeteles
        except Exception as err:
            raise err

    def next_ele(self, ele):
        try:
            next_ele = self.driver.execute_script("""
            return arguments[0].nextElementSibling
            """, ele)
            return next_ele
        except Exception as err:
            raise err

    def previous_ele(self, ele):
        try:
            previous_ele = self.driver.execute_script("""
            return arguments[0].previousElementSibling
            """, ele)
            return previous_ele
        except Exception as err:
            raise err

    def child_ele(self, ele, num):
        try:
            child_ele = self.driver.execute_script("""
                return arguments[0].children
            """, ele)
            return child_ele[num - 1]
        except Exception as err:
            raise err

    def child_ele_all(self, ele):
        try:
            child_ele = self.driver.execute_script("""
                return arguments[0].children
            """, ele)
            return child_ele
        except Exception as err:
            raise err

    def dely_input(self, ele, input_data, timeseq=1):
        """

        :param ele:
        :param input_data: String
        :param timeseq:
        :return:
        """
        input_data = str(input_data)
        try:
            input_data = list(input_data)
            for i in input_data:
                sleep(timeseq)
                ele.send_keys(i)
        except Exception as e:
            raise e

    def scroll_to(self, ele):
        try:
            self.driver.execute_script("""
                return arguments[0].scrollIntoView();
            """, ele)
        except Exception as err:
            raise err

    def parentnode(self, ele):
        try:
            parentnode = self.driver.execute_script("""
                return arguments[0].parentNode;
            """, ele)
            return parentnode
        except Exception as err:
            raise err

    def clear_input(self, ele):
        try:
            self.driver.execute_script("""
                arguments[0].value = '';
            """, ele)
        except Exception as e:
            raise e

    def get_style(self, ele, css_indicator):
        """

        :param ele: dom element
        :param css_indicator: css name, eg:width.
        :return: css_text
        note: the css prop should be existed
        """
        script = "return arguments[0].style" + "." + css_indicator
        try:
            target = self.driver.execute_script(script, ele)
            return target
        except Exception as e:
            raise e
