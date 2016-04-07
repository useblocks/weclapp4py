# -*- coding: utf-8 -*-
from .customer import Customer
from .contact import Contact


class Weclapp():
    def __init__(self, tenant, token):
        self.tenant = tenant
        self.token = token

        # Init sub apis
        self.customer = Customer(tenant, token)
        self.contact = Contact(tenant, token)









