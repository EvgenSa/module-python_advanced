import requests
from bs4 import BeautifulSoup
import re
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
            return (requests.get(Page.PAGE_URL, headers=Page.HEADERS).text)

        except requests.exceptions.HTTPError as err:
            print('Response is: {content}'.format(content=err.response.content))
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
        except requests.exceptions.ConnectTimeout:
            print('Connection timeout')
        except(ConnectionError, Exception) as e:
            print("Exception is :", e)



class Vacancies(Page):

    def __init__(self, vacancies_link=[]):
        self.vacancies_link = vacancies_link

    def searh_num_pages(self):
        pages = []
        self.soup = BeautifulSoup(self.create_page(), 'lxml')
        for i in self.soup.findAll(class_='bloko-button HH-Pager-Control', text=True):
            pages.append(i["href"][-1:])
        return (int(pages[-1]) + 1)

    def search_vacancies_link(self):
        for i in range(self.searh_num_pages()):
            link = self.PAGE_URL[:-1] + str(i)
            soup = BeautifulSoup(requests.get(link, headers=Page.HEADERS).text, 'lxml')
            for j in soup.findAll("a", text=True):
                if "Python" in j.text:
                    self.vacancies_link.append(j["href"])

class Calculator(Vacancies):

    def __init__(self, words):
        self.words = words
        self.counter = []
        self.result = []

    def searh_words(self):
        for word in self.words:
            for i in range(self.searh_num_pages()):
                link = self.PAGE_URL[:-1] + str(i)
                soup = BeautifulSoup(requests.get(link, headers=Page.HEADERS).text, 'lxml')
                self.counter.append(re.findall(word, str(soup).lower()))

    def average_number(self):
        for i in self.counter:
            for j in i:
                if j in self.words:
                    self.result.append(j)

        result_all = {i: self.result.count(i) for i in self.result}
        for key, value in result_all.items():
            print(str(key) + " counts " + str(value) + ', average number of occurrence' + ' = ' + str(value / len(self.result)*100) + '%')


if __name__ == '__main__':
    page = Page()
    page.create_page()
    jobs = Vacancies()
    jobs.search_vacancies_link()
    print(*jobs.vacancies_link, sep='\n')
    calc = Calculator(["python", "linux", "flask"])
    calc.searh_words()
    calc.average_number()
