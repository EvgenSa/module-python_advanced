from Autotest.test.business_layer.calculator import Calculator
from Autotest.test.business_layer.vacancies import Vacancies
import requests
from bs4 import BeautifulSoup


class TestCalculator():

    def setup(self):
        self.crucial_word = "shotgun"
        self.url = str('https://rabota.by/search/vacancy?area=16&fromSearchLine=true&st=searchVacancy&text=' + self.crucial_word)
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.response = BeautifulSoup(requests.get(self.url, headers=self.headers).text, 'lxml').find('h1', class_="bloko-header-1").text

    def test_vacancies_shotgun(self):
        assert self.response == "По запросу «shotgun» ничего не найдено", "there is such a vacancy"
        # print(self.response)


class TestCalc():

    def setup(self):
        vac = Vacancies()
        vac.search_vacancies_link()
        self.len_list_link = len(vac.vacancies_link)
        calc = Calculator(["python", "linux", "flask"])
        calc.searh_words()
        self.count = calc.counter
        self.result = []
        for i in self.count:
            for j in i:
                if j in ["python", "linux", "flask"]:
                    self.result.append(j)
        self.result_all = {i: self.result.count(i) for i in self.result}

    def test_avg(self):
        for key, value in self.result_all.items():
            # print(str(key) + ', avg' + ' = ' + str(value / self.len_list_link))
            assert -1 < value / self.len_list_link < 1, f" {key} {value} {'- avg too big'}"


# calc = TestCalculator()
#
# calc.setup()
# calc.test_vacancies_shotgun()
#
# testcalc = TestCalc()
# testcalc.setup()
# testcalc.test_avg()