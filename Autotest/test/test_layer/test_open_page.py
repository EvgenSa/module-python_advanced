from Autotest.test.core_layer.open_page import Page
import pytest
import requests

class TestPage():

    def setup(self):
        page = Page()
        self.myresponse = page.create_page()
        self.status_code = 200

    def test_request(self):

        assert self.myresponse.status_code == self.status_code, f"expected {self.myresponse.status_code}, got {self.status_code}"


    def teardown(self):
        print("ok")

class TestErrors():

    def setup(self):
        page = Page()
        self.error = requests.exceptions.HTTPError()
        self.response = page.create_page()
        self.error = requests.exceptions.HTTPError(response=self.response)
        self.error = requests.exceptions.HTTPError('message', response=self.response)

    def test_http_error(self):

        assert self.error.response == self.response
        assert str(self.error) == 'message'
        assert self.error.response == self.response


    def teardown(self):
        print("ok")

# page = TestPage()
# page.setup()
# page.test_request()
# erorr = TestErrors()
# erorr.setup()
# erorr.test_http_error()