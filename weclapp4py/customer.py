# -*- coding: utf-8 -*-
from .util import Action


class Customer(Action):
    def __init__(self, tenant, token):
        super().__init__(tenant, token)

    def read(self, res_id=None):
        try:
            customers = self._get("customer", res_id=res_id)
        except Exception as e:
            raise Exception("Could not get customers. Reason: %s" %e)

        return customers

    def create(self, partyType="PERSON", lastName=None, firstName=None, **kwargs):
        data = {"partyType": partyType,
                "lastName": lastName,
                "firstName": firstName}
        data.update(kwargs)
        try:
            contact = self._post("customer", data)
        except Exception as e:
            raise Exception("Could not create customer. Reason: %s" % e)
        return contact

    def update(self, res_id, lastName=None, firstName=None, **kwargs):
        if res_id is None:
            raise Exception("res_id must be set")

        data = {"lastName": lastName,
                "firstName": firstName}
        data.update(kwargs)

        try:
            contact = self._put("customer", res_id, data)
        except Exception as e:
            raise Exception("Could not update customer. Reason: %s" % e)
        return contact

    def delete(self, res_id):
        if res_id is None:
            raise Exception("res_id must be set")
        try:
            contact = self._delete("customer", res_id)
        except Exception as e:
            raise Exception("Could not delete customer. Reason: %s" % e)
        return contact

    def count(self):
        try:
            customer_count = self._get("customer/count")
        except Exception as e:
            raise Exception("Could count customers. Reason: %s" % e)
        return customer_count