from datetime import datetime, date

from application.db.people import get_employees
from application.salary import calculate_salary

from babel.numbers import format_currency

if __name__ == '__main__':
    print(f'The current date is {date.today()} and the current time is {datetime.now()}')
    get_employees()
    calculate_salary()

    salary_numbers = [123004.45, 345124.45, 123400.45, 234561.78, 567887.89]

    for salary in salary_numbers:
        print(f'The salary is {format_currency(salary, "RUB", locale="ru_RU")}')








