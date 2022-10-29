from application.salary import *
from application.people import *
from datetime import datetime as dt

if __name__ == '__main__':
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S'))
    calculate_salary()
    get_employees()
