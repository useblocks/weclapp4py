# weclapp4py
Abstracts the weclapp api as python lib

# Initialization
from weclapp4py import Weclapp

myWeclapp = Weclapp("MyCompany", "MyApiKey")

## Usage
~~~~
all_contacts = myWeclapp.contact.read()
specific_contacts = myWeclapp.contact.read(res_id="123")

contact_amount = myWeclapp.contact.count()

new_contact = myWeclapp.contact.create(lastName="Bar", firstName="Foo")

updated_contact = myWeclapp.contact.create(res_id="123", lastName="BarBar", firstName="FooFoo")

print("%s: %s %s" % (updated_contact["id"], 
                     updated_contact["firstName"], 
                     updated_contact["lastName"]))

myWeclapp.contact.delete(res_id="123")
~~~~
## Supported resources
Currently only **contact** and **customer** are supported.

## Custom field data
The functions **create** and **update** takes every keyword argument, which is given, and sends it to weclapp.
~~~~
myWeclapp.contact.create(lastName="Bar", ownArguement="my_stuff")
~~~~
