import calendar
import datetime

def unimplemented():
    return

class Employee:
    def __init__(self, name, address, type, attributes, id = 0):
        self.name = name
        self.address = address
        self.type = type

        self.parameter = attributes

        self.id = id

    def __str__(self):
        return f'{self.id}, {self.name}, {self.address}, {self.type}, {self.parameter}'

    def owing(self, owing: int):
        self.owing += owing

def hash_date(date: datetime.date):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for i in range(date.month):
        days += months[i]
    days += date.day
    is_leap = calendar.isleap(date.year)
    if days > 31 + 28:
        days += int(is_leap)
    
    return days

class PayrollSystem:
    TIMECARD = 0
    SELL_RESULT = 1
    SERVICE_TAX = 2

    current_date = datetime.date.today()

    def __init__(self):
        self.count = 0
        self.employees = []
        self.calendar = {}
        for i in range(366):
            self.calendar[i] = []

        self.current_day = self.calendar[hash_date(self.current_date)]

    def update_day(self, add_days = 1):
        self.current_date += datetime.timedelta(days=add_days)
        self.current_day = self.calendar[hash_date(self.current_date)]

    def print_vals(self):
        print('------------ list of employees -------------')
        for employee in self.employees:
            print(employee.__str__())

    def add_employee(self, name: str, address: str, type: str, attributes: int):
        self.employees.append(Employee(name, address, type, attributes, self.count))
        self.count += 1

    def del_employee(self, id: int):
        index = next(i for i, x in enumerate(self.employees) if x.id == id)
        del self.employees[index]

    def search_employee(self, id: int):
        return next(x for x in self.employees if x.id == id)

    def launch_timecard(self, id: int, hours: int):
        employee = self.search_employee(id)
        self.current_day.append((self.TIMECARD, employee.id, hours))

    def launch_sell_result(self, id: int, price: int, date: datetime.date = current_date, date_offset: int = 0):
        employee = self.search_employee(id)
        self.calendar[hash_date(date + datetime.timedelta(days=date_offset))].append((self.SELL_RESULT, employee.id, price))

    # charge must be a whole value, not a percentage of wage
    def launch_service_charge(self, id: int, charge: int):
        employee = self.search_employee(id)
        employee.owing(charge)

    def print_calendar(self):
        for key in self.calendar:
            if self.calendar[key] != []:
                print(str(key) + ':', self.calendar[key])



# calendar.isleap is to see if a year is leap, basically it runs a year % 4
# using the module datetime to use the datetime.date data type
# to add a day to datetime.date format is to add the datetime.timedelta(day=1)
# using the calendar.monthcalendar function to get array of days per month
#     [0,1,2,3,4,5,6], [7, ...] ...

calendar.setfirstweekday(calendar.SUNDAY)


def get_date_format(date):
    return date.year, date.month, date.day

if __name__ == '__main__':
    payroll = PayrollSystem()

    payroll.add_employee('alelo', 'maritona st. 19', 'hourly', 12)
    payroll.add_employee('simple', 'via st. 11', 'salaried', 1230)
    payroll.add_employee('another', 'via st. 12', 'salaried', 1240)

    payroll.print_vals()

    payroll.del_employee(1)

    payroll.print_vals()

    payroll.launch_timecard(0, 9)
    payroll.launch_sell_result(0, 1200, date_offset=1)
    payroll.update_day()
    payroll.launch_timecard(0, 8)
    payroll.launch_service_charge(0, 100)
    payroll.print_calendar()