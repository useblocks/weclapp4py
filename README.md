# weclapp4py
Abstracts the weclapp api as python lib

## Prerequirements
You need a weclapp account (https://weclapp.com) and a valid weclapp api key/token.

## Initialization
~~~~
from weclapp4py import Weclapp
myWeclapp = Weclapp("MyCompany", "MyApiKey")
~~~~

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

## Example and test run
There is an **example.py** file, which can be executed by:
~~~~
python3 example.py
~~~~
It will ask for your company and apikey. After that it will perform some API actions and shows you the results.

## Further documentation
Official weclapp API documentation: https://www.weclapp.com/api/
