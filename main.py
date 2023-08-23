from aplications.salary import calculate_salary
from aplications.db.people import get_employees
from datetime import datetime
import yandex
if __name__ == '__main__':
    print(datetime.date(datetime.today()))
    get_employees()
    calculate_salary()

