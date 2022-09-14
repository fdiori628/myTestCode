import email
import email.message
import email.parser
import email.policy
import poplib
import smtplib
import time
import re
from datetime import datetime, timedelta, timezone


class Email:

    def __init__(self, smtp, pop3, emailaddr, pwd):
        smtplib.SMTP().set_debuglevel(1)
        self._SMTP = smtp
        self._POP3 = pop3
        # 465 for ssl
        self._conn = smtplib.SMTP(smtp, 25)
        self._emailaddr = emailaddr
        self._conn.login(emailaddr, pwd)
        # 995 for ssl
        self._conn_pop = poplib.POP3(pop3, 110)
        self._conn_pop.user(emailaddr)
        self._conn_pop.pass_(pwd)

    def send_email(self, subject, _from, _to, content, attachment=None):
        # attachment = {
        #   'maintype' = '',
        #   'subtype' = '',
        #   'filename' = '',
        #   'filepath' = ''
        # }
        try:
            msg = email.message.EmailMessage()
            msg['subject'] = subject
            msg['from'] = _from
            msg['to'] = _to
            msg.set_content(content)
            if attachment == None:
                self._conn.sendmail(from_addr=self._emailaddr,
                                    to_addrs=_to, msg=msg.as_string())
            else:
                with open(attachment['filepath'], 'rb') as f:
                    msg.add_attachment(f.read(
                    ), maintype=attachment['maintype'], subtype=attachment['subtype'], filename=attachment['filename'])
                    self._conn.sendmail(
                        from_addr=self._emailaddr, to_addrs=_to, msg=msg.as_string())
            self._conn.quit()
        except Exception as e:
            raise e

    def recv_email(self, n):
        mails = []
        try:
            nums, total = self._conn_pop.stat()
            for num in range(nums - n + 1, nums + 1):
                mail = {}
                mail_data = self._conn_pop.retr(num)[1]
                mail_data = b'\r\n'.join(mail_data).decode("utf-8")
                msg = email.parser.Parser().parsestr(mail_data)
                mail['subject'] = msg['subject']
                mail['from'] = msg['Sender']
                mail['to'] = msg['to']
                mail['date'] = msg['date']
                for i in msg.walk():
                    if i.get_content_maintype() == 'multipart':
                        continue
                    elif i.get_content_maintype() == 'text':
                        mail['content'] = i.get_payload(decode=True)
                    else:
                        attachment_name = i.get_filename()
                        with open(attachment_name, 'wb') as f:
                            f.write(i.get_payload(decode=True))
                mails.append(mail)
            return mails
        except Exception as e:
            raise e


# if __name__ == '__main__':
#     smtp = 'smtp.163.com'
#     pop = 'pop.163.com'
#     emailaddr = 'essex_automation@163.com'
#     token = 'RNRIYKBJMEPZGTQK'
#     # domain_217 = "http://217.20.4.217:3002"
#     e = Email(smtp=smtp, emailaddr=emailaddr, pwd=token, pop3=pop)
#     subject = 'test hello19'
#     _from = 'Karl'
#     _to = ['xingyang.han@essexlg.com', '5168008@qq.com']
#     msg_content = 'test_report_2'
#     attachment = {
#         'maintype': 'html',
#         'subtype': 'html',
#         'filename': 'test_report.html',
#         'filepath': './report.html'
#     }
#     e.send_email(subject=subject, _from=_from, _to=_to, content=msg_content, attachment=attachment)

    # date = 'Sun, 21 Nov 2021 22:33:40 -0500 (EST)'
    # mail_date = date[:25]
    # utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    # dt = utc_dt.astimezone(timezone(timedelta(hours=-5)))
    # sending_date = str(dt)[:19]
    # print(sending_date)
    # print(time.mktime(time.strptime(mail_date, "%a, %d %b %Y %H:%M:%S")))
    # print(sending_date)
    # print(time.mktime(time.strptime(sending_date, "%Y-%m-%d %H:%M:%S")))

    # print(a)
    # print(time.asctime(time.localtime()))

    # subject = 'test hello18'
    # _from = 'Karl'
    # _to = ['fdiori@163.com']
    # msg_content = 'test_karl18'
    # attachment = {
    #     'maintype' : 'html',
    #     'subtype' : 'html',
    #     'filename' : 'test_report.html',
    #     'filepath' : '../test.html'
    # }
    # e.send_email(subject=subject, _from=_from, _to=_to, content=msg_content, attachment=attachment)
    # emails = e.recv_email(2)
    # for my_email in emails:
    #     print(my_email)
    #     print(my_email["date"])
