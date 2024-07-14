import pytest
from src.vacancy import Vacancy

def test_vacancy_initialization():
    vacancy = Vacancy("Test Name", "http://test.url", "Test Employer", {"from": 100000, "to": 200000})
    assert vacancy.name == "Test Name"
    assert vacancy.url == "http://test.url"
    assert vacancy.employer == "Test Employer"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 200000

def test_vacancy_salary_none():
    vacancy = Vacancy("Test Name", "http://test.url", "Test Employer", None)
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0

def test_vacancy_salary_partial():
    vacancy = Vacancy("Test Name", "http://test.url", "Test Employer", {"from": None, "to": 200000})
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 200000

def test_vacancy_str():
    vacancy = Vacancy("Test Name", "http://test.url", "Test Employer", {"from": 100000, "to": 200000})
    expected_str = ("Название: Test Name\nЗарплата от 100000 до 200000\nСсылка: http://test.url\n"
                    "Название компании: Test Employer")
    assert str(vacancy) == expected_str

def test_vacancy_comparison():
    vacancy1 = Vacancy("Test Name 1", "http://test.url", "Test Employer", {"from": 100000, "to": 200000})
    vacancy2 = Vacancy("Test Name 2", "http://test.url", "Test Employer", {"from": 150000, "to": 250000})
    assert vacancy2 > vacancy1