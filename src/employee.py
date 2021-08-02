import datetime
import calendar

SALARIED_PAYMENT = 0
HOURLY_PAYMENT = 1
COMMISSIONED_PAYMENT = 2

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

calendar.setfirstweekday(calendar.SUNDAY)

class Employee:
    def __init__(self, name: str, address: str, id: int = 0):
        self.name = name
        self.address = address

        self.syndicate = False
        self.syndicate_id = 0
        self.syndicate_charge = 0
        self.id = id

        self.owing_qnt = 0

    def __str__(self):
        return f'{self.id}, {self.name}, {self.address}'

    def owing(self, owing: int):
        self.owing_qnt += owing

    def generate_payment(self, previous_date):
        raise NotImplementedError()

# * Specialized classes * #

def next_month(date):
    maxmonth = calendar.monthrange(date.year, date.month)[1]
    next_maxmonth = calendar.monthrange(date.year, date.month + 1)[1]
    next_days = maxmonth
    if next_maxmonth < maxmonth:
        next_days -= maxmonth - next_maxmonth
    another_month = date + datetime.timedelta(days=next_days)
    return another_month

def get_day_of_month(date, date_to_get):
    day = date_to_get
    if day == -1:
        day = calendar.monthrange(date.year, date.month)[1]
    
    another_date = datetime.date(date.year, date.month, day)

    if another_date <= date:
        another_date = next_month(another_date)
    return another_date

def get_day_of_week(date, quantity, weekday):
    this_month = calendar.monthcalendar(date.year, date.month)

    val = next(i for i, x in enumerate(this_month) if x == date.day)
    print(val)

class Salaried(Employee):
    def __init__(self, name, address, monthly_wage, id = 0):
        super().__init__(name, address, id)

        self.payment_method = 'monthly'

        self.monthly_wage = monthly_wage

    def generate_payment(self, current_date, current_calendar):
        if self.payment_method == 'monthly':
            payment_date = get_day_of_month(current_date, -1)
        current_calendar[hash_date(payment_date)]['update'].append((SALARIED_PAYMENT, self.id))
        cal = calendar.monthrange(current_date.year, current_date.month)

        if self.payment_method == 'weekly':
            print('this is the weekly')

        print(cal)

        print('Generated assalaried payment of:', self.monthly_wage)

class Commissioned(Employee):
    def __init__(self, name, address, commission, id = 0):
        super().__init__(name, address, id)

        self.payment_method = 'bi-weekly'

    def generate_payment(self, current_date, current_calendar):
        print('Generated commissioned of:', self.paramaters)

class Hourly(Employee):
    def __init__(self, name, address, hour_wage, id = 0):
        super().__init__(name, address, id)

        self.payment_method = 'weekly'
        self.hour_wage = hour_wage

    def generate_payment(self, current_date, current_calendar):
        print('Generated hourly of:', self.hour_wage)