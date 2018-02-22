
# coding: utf-8

# # Chapter 8

# In[1]:

a = "hello"
b = 'world'
c = '''a multiple
line string'''
d = """More
multiple"""
e = ("Three " "Strings "
"Together")


# In[2]:

print(e)
print(type(e))


# In[4]:

dir(e)


# In[11]:

"The Launch Of The Pad".istitle()


# In[12]:

u = '45\u06602'


# In[13]:

u.isdecimal()


# In[14]:

u.isdigit()


# In[15]:

u.isnumeric()


# In[16]:

u = '45.2'


# In[17]:

u.isdecimal()


# In[20]:

u = "127.0.0.1"


# In[21]:

u.isdecimal()


# In[22]:

u.isdigit()


# In[23]:

u.isnumeric()


# In[25]:

s = "Hello world"
s.count('l')
s.find('l')


# In[26]:

s.find('l',2)


# In[27]:

s.rindex('l')


# In[29]:

s.rindex('m')


# In[32]:

s = "hola que tal estás, todo bien, verdad?, LOL"


# In[33]:

s.capitalize()


# In[34]:

s.title()


# In[35]:

countries = 'US, ES, LOL, PT, IT, DE'


# In[38]:

country_list_start_from_left = countries.split(',',3)
print(country_list_start_from_left)
print(len(country_list_start_from_left))


# In[39]:

country_list_start_from_right = countries.rsplit(',',3) # RSPLIT
print(country_list_start_from_right)
print(len(country_list_start_from_right))


# In[40]:

'|'.join(country_list_start_from_right)


# # Formating

# In[41]:

template = "Hello {0}, you are {1}. Your name is {0}."
print(template.format('Dusty', 'writing'))


# In[43]:

template = "Scaping brackets, showing the variable {} between two {{}}"
print(template.format("var1"))


# In[45]:

template = """
From: <{from_email}>
To: <{to_email}>
Subject: {subject}
Message: 
{full_message}"""
print(template.format(
from_email = "andertor.gmail.com", to_email = "asdf.company.net",
subject = "Asunto importante",
full_message = "Hola, esto es un asunto importante."))


# In[47]:

#mixed labels with positional arguments
print(" {} {label} {}".format("x","y",label = "z"))


# In[8]:

#Accessing to tuples and keys in dicts
emails = ("a@example.com", "b@example.com")
message = {
'subject': "You Have Mail!",
'message': "Here's some mail for you!"
}
template = "{message[message]}"
print(template.format(emails, message=message))


# In[9]:

#Using objects and accesing atributes in the format function call.
class Email:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

email = Email("a@example.com","b@example.com", "You have Email!", "Here's some email for you!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}

{0.message}"""
print(template.format(email))


# In[11]:

#encoding
import sys
sys.getdefaultencoding()


# # Regular expressions

# In[12]:

import re


# In[17]:

search_string = "hello world"
pattern = "hello world"

match = re.match(pattern, search_string)
if match:
    print("regex matches")



# In[18]:

search_string = "5n"
pattern = "\s\d\w"

match = re.match(pattern, search_string)
if match:
    print("regex matches")



# # JSON

# In[9]:

import json

class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def full_name(self):
        return("{} {}".format(self.first, self.last))
    


# In[10]:

c = Contact("John", "Smith")
json.dumps(c.__dict__)


# In[11]:

class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {'is_contact': True,
                    'first': obj.first,
                   'last': obj.last,
                   'full': obj.full_name}
        return super().defualt(obj)


# In[12]:

c = Contact("John", "Smith")
json.dumps(c, cls=ContactEncoder)


# In[14]:

# for decoding
def decode_contact(dic):
    if dic.get('is_contact'):
        return Contact(dic['first'], dic['last'])
    else:
        return dic


# In[17]:

data = ('{"is_contact": true, "last": "smith", "full": "Sir john J smith", "first": "john"}')
c = json.loads(data, object_hook=decode_contact)
c


# In[18]:

c.full_name


# # Case Study

# In[ ]:



