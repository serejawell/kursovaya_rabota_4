from abc import ABC, abstractmethod
import requests


class AbstractApi(ABC):

    @abstractmethod
    def get_url(self):
        pass

    def get_response(self):
        pass

    def get_vacancies(self):
        pass


class HH(AbstractApi):

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'

    def get_url(self):
        return self.__url

    def get_response(self):
        """Ожидание ответа от сервера"""
        response = requests.get(self.__url)
        return response

    def get_vacancies(self, per_page: int, text: str = ''):
        """Получает вакансии по нашему API"""
        self.per_page = per_page
        self.text = text
        params = {'text': self.text, 'page': 0, "per_page": self.per_page}
        response = requests.get(self.__url, params)
        return response.json()['items']

a = HH()
print(a.get_response())
print(a.get_vacancies(1,'developer'))