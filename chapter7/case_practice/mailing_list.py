import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

def send_email(subject, message, from_addr, *to_addrs, host='localhost', port=1025, headers=None):
    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value
    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

class MailingList:
    '''MAnage the mailing lists'''
    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_group(self, *groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            '''is a shortcut for g.intersection(groups); the set class does this by
                implementing the special __and__ method to call intersection.'''
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        emails = self.emails_in_group(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)

send_email("A model subject", "The message contents","from@example.com", "to1@example.com", "to2@example.com")