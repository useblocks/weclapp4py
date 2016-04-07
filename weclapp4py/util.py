# -*- coding: utf-8 -*-
import requests


class Action():
    def __init__(self, tenant, token, api_version="v1"):
        self.tenant = tenant
        self.token = token
        self.api_version = api_version
        self.base_url = "https://%s.weclapp.com/webapp/api/%s/" % (tenant, api_version)
        self.headers = {
            "AuthenticationToken": token,
            "Content-type": "application/json"
        }

    def _get(self, resource, res_id=None):
        url = "".join([self.base_url, resource])

        if res_id is None:
            answer = self.__get_all(url)
        elif isinstance(res_id, str) or isinstance(res_id, int):
            answer = self.__get_single(url, str(res_id))
        else:
            raise Exception("res_id set, but type is not string.")

        self.__check_answer(answer)

        if res_id is None:
            return answer.json()["result"]
        else:
            return answer.json()

    def _post(self, resource, data):
        url = "".join([self.base_url, resource])
        answer = requests.post(url, headers=self.headers, json=data)
        self.__check_answer(answer)
        return answer.json()

    def _put(self, resource, res_id, data):
        url = "".join([self.base_url, resource, "/id/", res_id])
        answer = requests.put(url, headers=self.headers, json=data)
        self.__check_answer(answer)
        return answer.json()

    def _delete(self, resource, res_id):
        url = "".join([self.base_url, resource, "/id/", res_id])
        answer = requests.delete(url, headers=self.headers)
        self.__check_answer(answer)
        return None

    def __get_all(self, url):
        return requests.get(url, headers=self.headers)

    def __get_single(self, url, res_id):
        url = "".join([url, "/id/", res_id])
        return requests.get(url, headers=self.headers)

    @staticmethod
    def __check_answer(answer):
        if answer.status_code == 404:
            raise Exception("Server responded 404 for url %s" % answer.request.url)
        if answer.status_code < 200 or answer.status_code >= 300:
            raise Exception(answer.json()["error"])
