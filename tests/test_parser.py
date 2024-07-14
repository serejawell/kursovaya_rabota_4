import pytest
from unittest.mock import patch
from src.parser import HhAPI

@patch('src.parser.requests.get')
def test_get_vacancies(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"name": "Test Vacancy", "alternate_url": "http://test.url",
                                                  "employer": {"name": "Test Employer"}, "salary": {"from": 100000, "to": 200000}}]}
    hh = HhAPI()
    vacancies = hh.get_vacancies("test", 1)
    assert len(vacancies) == 1
    assert vacancies[0]['name'] == "Test Vacancy"
    assert vacancies[0]['alternate_url'] == "http://test.url"
    assert vacancies[0]['employer']['name'] == "Test Employer"
    assert vacancies[0]['salary']['from'] == 100000
    assert vacancies[0]['salary']['to'] == 200000

@patch('src.parser.requests.get')
def test_get_vacancies_no_data(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}
    hh = HhAPI()
    vacancies = hh.get_vacancies("test", 1)
    assert len(vacancies) == 0