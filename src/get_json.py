import json
import os
from src.vacancy import Vacancy

class JSONSaver:
    def __init__(self, filename='data/vacancies.json'):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_vacancies(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Vacancy(item['name'], item['alternate_url'], item['employer']['name'], item['salary']) for item in data]

    def delete_data(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
