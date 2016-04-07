# -*- coding: utf-8 -*-
#################################################################################
# Weclapp API example
# API documentation: https://www.weclapp.com/api/
#
# You must have a valid weclapp account to use their api.
#
# You also need to generate a api key inside weclapp before you can
# use their api.
#################################################################################

from weclapp4py import Weclapp

tenant = None
api_key = None

print("Weclapp API Example script")
print("**************************\n")
if tenant is None or api_key is None:
    print("You can set tenant and api key inside example.py to avoid the following questions.\n")
    tenant = input("Enter company/tenant name: ")
    api_key = input("Enter api_key: ")

weclapp = Weclapp(tenant, api_key)

print("\nCounting...")
print("contacts %s" % weclapp.contact.count())
print("customers %s" % weclapp.customer.count())

print("\nGet everything....")
customers = weclapp.customer.read()
print(customers)

contacts = weclapp.contact.read()
for contact in contacts:
    print("%s: %s %s" % (contact["id"], contact["firstName"], contact["lastName"]))

print("\nCreate, Update and Delete")
contact = weclapp.contact.create("Bar", "Foo", email="foo@bar.com")
contact = weclapp.contact.read(res_id=contact["id"])
print("%s: %s %s" % (contact["id"], contact["firstName"], contact["lastName"]))

contact = weclapp.contact.update(contact["id"], "BarBar", "FooFoo", email="foofoo@barbar.com")
contact = weclapp.contact.read(res_id=contact["id"])
print("%s: %s %s" % (contact["id"], contact["firstName"], contact["lastName"]))

weclapp.contact.delete(contact["id"])
try:
    max_new = weclapp.contact.read(res_id=contact["id"])
except Exception:
    print("Contact not found")

