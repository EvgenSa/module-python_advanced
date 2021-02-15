from Autotest.test.business_layer.vacancies import Vacancies

class TestVacancies():

    def setup(self):

        vacancy = Vacancies()
        vacancy.search_vacancies_link()
        self.vacancies_list = vacancy.vacancies_link
        self.word_to_check = "Python"                   #shotgun
        # print(*self.vacancies_list, sep='\n')

    def test_vacancies_list_empty(self):
        assert len(self.vacancies_list) != 0, "vacancies_list is empty"

    def test_vacancies_list(self):
        for i in self.vacancies_list:

            assert i.find(self.word_to_check) != -1, f"expected {'Python vacancy'}, got {'Other vacancy'}"

    def teardown(self):
        print("ok")


# vac = TestVacancies()
# vac.setup()
# vac.test_vacancies_list_empty()
# vac.test_vacancies_list()
# vac.setup()
# vac.test_vacancies_shotgun()