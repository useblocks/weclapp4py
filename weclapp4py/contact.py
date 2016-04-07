# -*- coding: utf-8 -*-
from .util import Action


class Contact(Action):
    def __init__(self, tenant, token):
        super().__init__(tenant, token)

    def read(self, res_id=None):
        try:
            contacts = self._get("contact", res_id=res_id)
        except Exception as e:
            raise Exception("Could not get contact. Reason: %s" % e)

        return contacts

    def create(self, lastName=None, firstName=None, **kwargs):
        data = {"lastName": lastName,
                "firstName": firstName}
        data.update(kwargs)
        try:
            contact = self._post("contact", data)
        except Exception as e:
            raise Exception("Could not create contact. Reason: %s" % e)
        return contact

    def update(self, res_id, lastName=None, firstName=None, **kwargs):
        if res_id is None:
            raise Exception("res_id must be set")

        data = {"lastName": lastName,
                "firstName": firstName}
        data.update(kwargs)

        try:
            contact = self._put("contact", res_id, data)
        except Exception as e:
            raise Exception("Could not update contact. Reason: %s" % e)
        return contact

    def delete(self, res_id):
        if res_id is None:
            raise Exception("res_id must be set")
        try:
            contact = self._delete("contact", res_id)
        except Exception as e:
            raise Exception("Could not delete contact. Reason: %s" % e)
        return contact

    def count(self):
        try:
            contact_count = self._get("contact/count")
        except Exception as e:
            raise Exception("Could count contacts. Reason: %s" % e)
        return contact_count

