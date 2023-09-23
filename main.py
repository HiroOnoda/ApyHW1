
import datetime
from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(datetime.now())
    print(calculate_salary(3,4))
    get_employees()
    pass
