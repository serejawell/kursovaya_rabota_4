from src.parser import HhAPI
from src.get_json import JSONSaver


def parse_salary_range(salary_range):
    """Парсинг диапазона зарплат из строки"""
    try:
        min_salary, max_salary = map(int, salary_range.split('-'))
        return min_salary, max_salary
    except ValueError:
        print("Некорректный формат диапазона зарплат. Введите в формате 'мин - макс'.")
        return None, None


def user_interaction():
    print('Данная программа поможет подобрать интересные вакансии на сайте hh.ru.\n')
    search_query = input('Введите желаемую для поиска профессию: ')
    top_n = int(input('Введите количество вакансий для вывода: '))
    salary_range = input("Введите диапазон зарплат в формате 'мин - макс': ")

    min_salary, max_salary = parse_salary_range(salary_range)
    if min_salary is None or max_salary is None:
        return

    hh = HhAPI()
    data = hh.get_vacancies(search_query, 100)

    saver = JSONSaver()
    saver.save_data(data)

    vacancies = saver.load_vacancies()

    filtered_vacancies = [
        vacancy for vacancy in vacancies
        if vacancy.salary_from >= min_salary and (vacancy.salary_to <= max_salary and vacancy.salary_to != 0)
    ]


    filtered_vacancies.sort(key=lambda vacancy: vacancy.salary_from, reverse=True)


    for i in range(min(top_n, len(filtered_vacancies))):
        print(f'{filtered_vacancies[i]}\n')



