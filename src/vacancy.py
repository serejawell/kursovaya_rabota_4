class Vacancy:

    def __init__(self, name, url, employer, salary):
        '''Инициализация класса с нужными атрибутами'''
        self.name = name
        self.url = url
        self.employer = employer
        self.check_salary(salary)

    def check_salary(self, salary):
        """Проверка корректности зарплаты"""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary.get("from", 0) or 0
            self.salary_to = salary.get("to", 0) or 0



    def __str__(self):
        return (f'Название: {self.name}\nЗарплата от {self.salary_from} до {self.salary_to}\nСсылка: {self.url}\n'
                f'Название компании: {self.employer}')

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from > other.salary_from
        return False