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

# calendar.setfirstweekday(calendar.SUNDAY)

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

def next_month(date: datetime.date):
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
    this_day = date.day

    location = (0,0)
    for row, week in enumerate(this_month):
        done = False
        for column, day in enumerate(week):
            if day == this_day:
                location = (row, column)
                done = True
                break
        if done:
            break
    
    other_day = 0
    outofbounds = False
    hasalready = this_day >= this_month[location[0]][weekday]
    haszeros = ~bool(this_month[-1][-1])

    index = location[0] - 1 + hasalready
    for _ in range(quantity):
        index += 1
        try:
            other_day = this_month[index][weekday]
        except:
            outofbounds = True
            index = haszeros
        if other_day == 0:
            index = 0
        if other_day == 0 or outofbounds:
            outofbounds = False
            date = next_month(date)
            this_month = calendar.monthcalendar(date.year, date.month)
            haszeros = ~bool(this_month[-1][-1])
            other_day = this_month[index][weekday]
    
    return datetime.date(date.year, date.month, other_day)

def schedule_paymethod(date: datetime.date, entry: str):
    monthly = 0
    weekly = 1
    func_dict = {
        'monthly': monthly, 'weekly': weekly,
        'mensalmente': monthly, 'semanalmente': weekly,
        'mensal': monthly, 'semanal': weekly
    }

    weekday_dict = {
        'segunda': 0, 'terca': 1, 'quarta': 2, 'quinta': 3,
        'sexta': 4, 'sabado': 5, 'domingo': 6,
        'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
        'friday': 4, 'saturday': 5, 'sunday': 6
    }

    parsed_entry = entry.split(' ')
    if len(parsed_entry) == 1:
        if entry == 'monthly':
            entry = 'monthly $'
        elif entry == 'weekly':
            entry = 'weekly 1 friday'
        elif entry == 'bi-weekly':
            entry = 'weekly 2 friday'
        parsed_entry = entry.split(' ')

    func_selection = func_dict[parsed_entry[0]]

    if parsed_entry[1] != '$':
        entry_first_arg = int(parsed_entry[1])
    else:
        entry_first_arg = -1

    if func_selection == monthly:
        out_date = get_day_of_month(date, entry_first_arg)
    elif func_selection == weekly:
        out_date = get_day_of_week(date, entry_first_arg, weekday_dict[parsed_entry[2]])

    return out_date

class Salaried(Employee):
    def __init__(self, name, address, monthly_wage, id = 0):
        super().__init__(name, address, id)

        self.payment_method = 'monthly'

        self.monthly_wage = monthly_wage

    def generate_payment(self, current_date, current_calendar):
        payment_date = schedule_paymethod(current_date, self.payment_method)

        print('payment_date', payment_date)
        current_calendar[hash_date(payment_date)]['update'].append(self.id)

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