class Employee:
    def __init__(self, name, address, type, attributes, id = 0):
        self.name = name
        self.address = address
        self.type = type

        self.parameter = attributes

        self.id = id

    def __str__(self):
        return f'{self.id}, {self.name}, {self.address}, {self.type}, {self.parameter}'

class PayrollSystem:
    employees = []
    count = 0

    def add_employee(self, name, address, type, attributes):
        self.employees.append(Employee(name, address, type, attributes, self.count))
        self.count += 1

    def print_vals(self):
        print('------------ list of employees -------------')
        for employee in self.employees:
            print(employee.__str__())

    def del_employee(self, id):
        index = next(i for i, x in enumerate(self.employees) if x.id == id)
        del self.employees[index]

if __name__ == '__main__':
    payroll = PayrollSystem()

    payroll.add_employee('alelo', 'maritona st. 19', 'salaried', 1000)
    payroll.add_employee('another', 'via st. 11', 'salaried', 1230)
    payroll.add_employee('another', 'via st. 12', 'salaried', 1240)

    payroll.print_vals()

    payroll.del_employee(1)

    print('')

    payroll.print_vals()