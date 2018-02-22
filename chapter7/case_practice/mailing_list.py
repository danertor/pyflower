import smtplib
import json
from email.mime.text import MIMEText
from collections import defaultdict

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

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
    def __init__(self, filename="data1.json"):
        self.email_map = defaultdict(set)
        self.data_file = filename

    def add_to_group(self, email, group):
        try:
            self.email_map[email].add(group)
        except KeyError:
            newset = set()
            newset.add(group)
            self.email_map[email] = newset

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

    def save(self):
        data = json.dumps(dict(self.email_map), cls=SetEncoder)
        data = json.loads(data)
        with open(self.data_file, 'w') as outfile:
            json.dump(data, outfile)

    def load(self):
        self.email_map = defaultdict(set)
        try:
            with open(self.data_file, 'r') as file:
                self.email_map = dict(json.loads(file.read()))
            for k, v in self.email_map.items():
                self.email_map[k] = set(v) if v else set()
        except IOError:
            print("Error on {}".format(self.data_file))

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()

    def __str__(self):
        output = ''
        newline = '\n'
        for k, v in self.email_map.items():
            output += 'K' + ' ' + str(k.__class__) + ' ' + str(k) + ' ' + 'v' + ' ' + str(v.__class__) + ' ' + str(v) + newline
        return output

with MailingList('addresses.json') as m:
    print(m)
    m.add_to_group('friend2@example.com', 'friends')
    m.add_to_group('friend2@example.com', 'family2')
    print(m)
    m.send_mailing("What's up", "hey friends, how's it going", 'me@example.com', 'friends')


#send_email("A model subject", "The message contents","from@example.com", "to1@example.com", "to2@example.com")