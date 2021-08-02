from employee import *

# * Starting payroll system * #

class PayrollSystem:
    TIMECARD = 0
    SELL_RESULT = 1
    SERVICE_TAX = 2

    current_date = datetime.date.today()

    def __init__(self):
        self.count = 1
        self.employees = []
        self.calendar = {}
        for i in range(366):
            self.calendar[i] = {'update': [], 'schedule': []}

        self.current_day = self.calendar[hash_date(self.current_date)]

    def update_day(self, add_days = 1):
        self.current_date += datetime.timedelta(days=add_days)
        self.current_day = self.calendar[hash_date(self.current_date)]

    def print_vals(self):
        print('------------ list of employees -------------')
        for employee in self.employees:
            print(employee.__str__())

    def add_employee(self, name: str, address: str, type: str, attr: int):
        types = ['salaried', 'commissioned', 'hourly']
        assert type in types

        if type == 'salaried':
            self.employees.append(Salaried(name, address, attr, self.count))
        elif type == 'commissioned':
            self.employees.append(Commissioned(name, address, attr, self.count))
        elif type == 'hourly':
            self.employees.append(Hourly(name, address, attr, self.count))
        
        self.count += 1

    def search_employee(self, id: int):
        return next(x for x in self.employees if x.id == id)

    def del_employee(self, id: int):
        index = next(i for i, x in enumerate(self.employees) if x.id == id)
        del self.employees[index]

    def launch_timecard(self, id: int, hours: int):
        employee = self.search_employee(id)
        self.current_day['schedule'].append((self.TIMECARD, employee.id, hours))

    def launch_sell_result(self, id: int, price: int, date: datetime.date = current_date, date_offset: int = 0):
        employee = self.search_employee(id)
        self.calendar[hash_date(date + datetime.timedelta(days=date_offset))]['schedule'].append((self.SELL_RESULT, employee.id, price))

    # charge must be a whole value, not a percentage of wage
    def launch_service_charge(self, id: int, charge: int):
        employee = self.search_employee(id)
        employee.owing(charge)

    def print_calendar(self):
        print('---------------- calendar ------------------')
        for key in self.calendar:
            if self.calendar[key] != {'schedule':[], 'update':[]}:
                print(str(key) + ':', self.calendar[key])

    def change_employee_data(self, id: int, name: str = 0, address: str = 0, type: str = 0, payment_method: str = 0, syndicate: bool = 0, syndicate_id: int = 0, syndicate_charge: int = 0):
        employee = self.search_employee(id)
        if name:
            employee.name = name
        if address:
            employee.address = address
        if type:
            employee.type = type
        if payment_method:
            employee.payment_method = payment_method
        
        employee.syndicate = syndicate

        if syndicate_id:
            employee.syndicate_id = syndicate_id
        if syndicate_charge:
            employee.syndicate_charge = syndicate_charge