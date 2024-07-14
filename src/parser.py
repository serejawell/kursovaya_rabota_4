import requests
from abc import ABC, abstractmethod


class Api(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HhAPI:
    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, text, per_page):
        params = {
            "text": text,
            "per_page": per_page
        }
        response = requests.get(self._url, params=params)
        response.raise_for_status()
        return response.json()["items"]

