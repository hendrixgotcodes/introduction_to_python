# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#core modules
import datetime
from datetime import date
from time import time

#pip modules
from camelcase import CamelCase

#custom modules
import validator


today = datetime.date.today()

print(today)
print(date.today())

print(time())

c = CamelCase()

print(c.hump("hello there world"))

email = "someone@xitroo.com"

if validator.validate_email(email):
    print("Valid email")
else:
    print("Bad email")
