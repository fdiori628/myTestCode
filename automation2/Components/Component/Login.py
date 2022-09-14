from Common.web_config_until import WebConfig
from Common.dom_until import DomUntil
from Common.logger_until import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.email_until import Email
import time
from datetime import datetime, timedelta, timezone


class Login:

    def __init__(self, _driver):
        self._log = Logger()
        self._webconfig = WebConfig('Login')
        self._pageobj = self._webconfig.domelements
        self._driver = _driver
        self._findele = DomUntil(_driver).findelement
        self._waiturl = DomUntil(_driver).wait_url
        self.title = _driver.title
        self.dom = DomUntil(_driver)

    def username(self):
        css = self._pageobj['username']
        ele = self._findele(css, 5, 0.5)
        return ele

    def username_input(self, username):
        ele = Login(self._driver).username()
        ele.send_keys(username)

    def password(self):
        css = self._pageobj['password']
        ele = self._findele(css, 5, 0.5)
        return ele

    def password_input(self, pwd):
        ele = Login(self._driver).password()
        ele.send_keys(pwd)

    def privacy_checkbox(self):
        checked = False
        css = self._pageobj['privacy_checkbox']
        ele = self._findele(css, 5, 0.5)
        ele_p = DomUntil(self._driver).parentnode(ele)
        checked_class = "ant-checkbox-checked"
        if checked_class in ele_p.get_attribute("class"):
            checked = True
        return ele, checked

    def privacy_check_click(self):
        ele = Login(self._driver).privacy_checkbox()
        ele[0].click()

    def submitbtn(self):
        css = self._pageobj['submitBtn']
        ele = self._findele(css, 5, 0.5)
        return ele

    def submit(self):
        ele = Login(self._driver).submitbtn()
        ele.click()

    def error_message(self):
        err_msg = "Username/password incorrect. Please try again."
        WebDriverWait(self._driver, 20, 1).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".form"), err_msg))
        form = self.dom.findelements(".form div")
        ele = self.dom.contains(form, err_msg)
        return ele.text

    def forget_password(self):
        _text = "Forgot Password"
        all_ele = self.dom.findelements(".form a")
        target_ele = self.dom.contains(all_ele, _text)
        return target_ele

    def forget_pwd_email(self):
        css = self._pageobj["forget_pwd_email"]
        ele = self.dom.findelement(css)
        return ele

    def forget_pwd_send_btn(self):
        css = self._pageobj["forget_pwd_send_btn"]
        ele = self.dom.findelement(css)
        return ele

    def retrieve_email_forgetpwd(self):
        """
            # current func support for forget password
            # for user active, will script in other function
            # content = first_email["content"].decode()
            # content_a = content.split(">")
            # # href is num 20 in the [], link is started with 9 end with 166 in the str
            # link = content_a[20][9:166]
            # # delete amp;
            # new_link = re.sub('amp;', "", link)
            # staging = "https://eysight-staging.essexlg.com:3000"
            # target_link = re.sub(staging, domain, new_link)
            domain is for active_mail
        """
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt = utc_dt.astimezone(timezone(timedelta(hours=-5)))
        sending_time_format = str(dt)[:19]
        sending_time = int(time.mktime(time.strptime(sending_time_format, "%Y-%m-%d %H:%M:%S")))
        email_config = self._webconfig.testdata["email_config"]
        smtp = email_config["smtp"]
        pop = email_config["pop"]
        emailaddr = email_config["emailaddr"]
        token = email_config["token"]
        mail_date = 0
        retry_id = 0
        first_email = {}
        while sending_time >= mail_date and retry_id <= 18:
            time.sleep(10)
            e = Email(smtp=smtp, emailaddr=emailaddr, pwd=token, pop3=pop)
            emails = e.recv_email(1)
            first_email = emails[0]
            mail_date_org = first_email["date"]
            mail_date_format = mail_date_org[:25]
            mail_date = int(time.mktime(time.strptime(mail_date_format, "%a, %d %b %Y %H:%M:%S")))
            retry_id += 1
            self._log.logger(f"retry_id: {retry_id}")
            self._log.logger(f"mailing_date: {mail_date_format}")
            self._log.logger(f"sending_date: {sending_time_format}")
        if retry_id >= 19:
            self._log.logger(f"no mail receive in 3 mins")
            return False
        else:
            content = first_email["content"].decode()
            content = content.split(">")
            link = content[10][9:-1]
            self._log.logger(f"reset link: {link}")
            return link

    def login(self, username, pwd):
        try:
            l = Login(self._driver)
            l.username_input(username)
            l.password_input(pwd)
            l.privacy_check_click()
            l.submit()
            result = self._waiturl("projects", 20, 1)
            if result:
                self._log.logger(f'login ESB with {username}')
        except TimeoutError as e:
            raise e and self._log.logger_error(e)


# if __name__ == '__main__':
#     r = WebConfig('driver').get_appinfo()['Driver']
#     driver = webdriver.Chrome(r)
#     print(Login(driver).retrieve_email("010101"))
#     driver.get('http://172.20.4.217:3002/login')
#     l = Login(driver)
#     l.login('xingyang.han@essexlg.com', '1qaz@WSX3edc')
#     WebDriverWait(driver, 10, 1).until(EC.url_contains('projects'))
#     current_url = driver.current_url
#     assert current_url == 'http://172.20.4.217:3002/projects'
#     driver.quit()
