import requests
from requests import ConnectionError

class Parser:
    def __init__(self, name, url, headers):
        self.name = name
        self.url = url
        self.headers = headers


class Page(Parser):

    NAME = "Python"
    PAGE_URL = str('https://rabota.by/search/vacancy?L_is_autosearch=false&area=16&clusters=true&enable_snippets=true&text=' + NAME + '&page=0')
    HEADERS = {'user-agent': 'my-app/0.0.1'}

    def __init__(self):
        super().__init__(Page.NAME, Page.PAGE_URL, Page.HEADERS)

    def create_page(self):

        try:
            return (requests.get(Page.PAGE_URL, headers=Page.HEADERS))
            # return (requests.get(Page.PAGE_URL, headers=Page.HEADERS)).text

        except requests.exceptions.HTTPError as err:
            return ('Response is: {content}'.format(content=err.response.content))
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
        except requests.exceptions.ConnectTimeout:
            print('Connection timeout')
        except(ConnectionError, Exception) as e:
            print("Exception is :", e)