import pytest
import os
import json
from src.get_json import JSONSaver
from src.vacancy import Vacancy

@pytest.fixture
def json_saver():
    return JSONSaver('test_vacancies.json')

@pytest.fixture
def sample_data():
    return [{"name": "Test Vacancy", "alternate_url": "http://test.url",
             "employer": {"name": "Test Employer"}, "salary": {"from": 100000, "to": 200000}}]

def test_save_data(json_saver, sample_data):
    json_saver.save_data(sample_data)
    assert os.path.exists('test_vacancies.json')
    with open('test_vacancies.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert data == sample_data
    os.remove('test_vacancies.json')

def test_load_vacancies(json_saver, sample_data):
    json_saver.save_data(sample_data)
    vacancies = json_saver.load_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].name == "Test Vacancy"
    assert vacancies[0].url == "http://test.url"
    assert vacancies[0].employer == "Test Employer"
    assert vacancies[0].salary_from == 100000
    assert vacancies[0].salary_to == 200000
    os.remove('test_vacancies.json')

def test_delete_data(json_saver, sample_data):
    json_saver.save_data(sample_data)
    json_saver.delete_data()
    assert not os.path.exists('test_vacancies.json')