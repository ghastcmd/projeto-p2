import datetime
import calendar

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

class Salaried(Employee):
    def __init__(self, name, address, monthly_wage, id = 0):
        super().__init__(name, address, id)

        self.payment_method = 'monthly'

    def generate_payment(self, previous_date):
        print('Generated assalaried payment of:', self.parameter)

class Commissioned(Employee):
    def __init__(self, name, address, commission, id = 0):
        super().__init__(name, address, id)

        self.payment_method = 'bi-weekly'

    def generate_payment(self, previous_date):
        print('Generated commissioned of:', self.paramaters)

class Hourly(Employee):
    def __init__(self, name, address, hour_wage, id = 0):
        super().__init__(name, address, id)

        self.payment_method = 'weekly'

    def generate_payment(self, previous_date):
        print('Generated hourly of:', self.parameters)