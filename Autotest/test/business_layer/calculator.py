from Autotest.Pars_final import Vacancies, Page, Parser
from bs4 import BeautifulSoup
import requests
import re


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



# if __name__ == '__main__':
#     page = Page()
#     page.create_page()
#     jobs = Vacancies()
#     jobs.search_vacancies_link()
#     print(*jobs.vacancies_link, sep='\n')
#     calc = Calculator(["python", "linux", "flask"])
#     calc.searh_words()
#     calc.average_number()