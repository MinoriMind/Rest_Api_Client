import pycurl
import json
from io import BytesIO

class Client:
    
    def __prepare_buffer(self):
        self.result_buffer = BytesIO()
        self.curl.setopt(self.curl.WRITEDATA, self.result_buffer)

    def __init__(self, url: str):
        self.base_url = url

        self.curl = pycurl.Curl()
        self.__prepare_buffer()


    def register_user(self, login: str, password: str):
        data = json.dumps({'login':login, 'password':password})

        self.curl.setopt(self.curl.URL, self.base_url + 'user/')
        self.curl.setopt(self.curl.CUSTOMREQUEST, 'POST')
        self.curl.setopt(self.curl.POSTFIELDS, data)
        self.curl.setopt(self.curl.HTTPHEADER, ['Content-type: application/json'])
        self.curl.perform()

        response = self.result_buffer.getvalue()
        self.__prepare_buffer()

        return response;

    def get_todos(self, login: str, password: str):
        data = json.dumps({'login':login, 'password':password})

        self.curl.setopt(self.curl.URL, self.base_url + 'todo/')
        self.curl.setopt(self.curl.CUSTOMREQUEST, 'GET')
        self.curl.setopt(self.curl.POSTFIELDS, data)
        self.curl.setopt(self.curl.HTTPHEADER, ['Content-type: application/json'])
        self.curl.perform()

        response = self.result_buffer.getvalue()
        self.__prepare_buffer()

        return response

    def add_todo(self, login: str, password: str, name: str, text: str):
        data = json.dumps({'login':login, 'password':password, 'name': name, 'text': text})

        self.curl.setopt(self.curl.URL, self.base_url + 'todo/')
        self.curl.setopt(self.curl.CUSTOMREQUEST, 'POST')
        self.curl.setopt(self.curl.POSTFIELDS, data)
        self.curl.setopt(self.curl.HTTPHEADER, ['Content-type: application/json'])
        self.curl.perform()

        response = self.result_buffer.getvalue()
        self.__prepare_buffer()

        return response

    def delete_todo(self, login: str, password: str, id: int):
        data = json.dumps({'login':login, 'password':password})

        self.curl.setopt(self.curl.URL, self.base_url + 'todo/' + str(id))
        self.curl.setopt(self.curl.CUSTOMREQUEST, 'DELETE')
        self.curl.setopt(self.curl.POSTFIELDS, data)
        self.curl.setopt(self.curl.HTTPHEADER, ['Content-type: application/json'])
        self.curl.perform()

        response = self.result_buffer.getvalue()
        self.__prepare_buffer()

        return response




