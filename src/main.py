from payroll import PayrollSystem
import copy

class QueueSystem:
    ADD_EMPLOYEE = 0
    DEL_EMPLOYEE = 1
    LAUNCH_TIMECARD = 2
    LAUNCH_SELLING = 3
    LAUNCH_SERVICE_CHARGE = 4
    CHANGE_EMPLOYEE_DATA = 5
    CHANGE_EMPLOYEE_TYPE = 6
    RUN_TODAY_PAYROLL = 7
    PAYROLL_STATE = 8
    UPDATE_DAY = 9
    CHANGE_PAYMENT_SCHEDULE = 10

    def __init__(self, payroll: PayrollSystem):
        self.state_save = [(self.PAYROLL_STATE, (payroll))]
        self.states_index = [0]
        self.current_index = 1

    def add_employee(self, name, address, type, parameter):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.ADD_EMPLOYEE, (name, address, type, parameter)))

    def del_employee(self, id):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.DEL_EMPLOYEE, [id]))
    
    def launch_timecard(self, id, hours):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.LAUNCH_TIMECARD, (id, hours)))
    
    def launch_selling(self, id, price, date):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.LAUNCH_SELLING, (id, price, date)))
    
    def launch_service_charge(self, id, charge):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.LAUNCH_SERVICE_CHARGE, (id, charge)))
    
    def change_employee_data(self, id, data: dict):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.CHANGE_EMPLOYEE_DATA, (id, data)))
    
    def change_employee_type(self, id, type):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.CHANGE_EMPLOYEE_TYPE, (id, type)))

    def run_today_payroll(self):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append([self.RUN_TODAY_PAYROLL])

    def update_day(self):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append([self.UPDATE_DAY])

    def change_payment_schedule(self, id, new_schedule):
        self.overwrite_undo()
        self.current_index += 1
        self.state_save.append((self.CHANGE_PAYMENT_SCHEDULE, (id, new_schedule)))

    def print(self):
        print_dict = {
            self.ADD_EMPLOYEE: 'ADD_EMPLOYEE',
            self.DEL_EMPLOYEE: 'DEL_EMPLOYEE',
            self.LAUNCH_TIMECARD: 'LAUNCH_TIMECARD',
            self.LAUNCH_SELLING: 'LAUNCH_SELLING',
            self.LAUNCH_SERVICE_CHARGE: 'LAUNCH_SERVICE_CHARGE',
            self.CHANGE_EMPLOYEE_DATA: 'CHANGE_EMPLOYEE_DATA',
            self.CHANGE_EMPLOYEE_TYPE: 'CHANGE_EMPLOYEE_TYPE',
            self.RUN_TODAY_PAYROLL: 'RUN_TODAY_PAYROLL',
            self.PAYROLL_STATE: 'PAYROLL_STATE',
            self.UPDATE_DAY: 'UPDATE_DAY',
            self.CHANGE_PAYMENT_SCHEDULE: 'CHANGE_PAYMENT_SCHEDULE',
        }

        for x in self.state_save[:self.current_index]:
            print(print_dict[x[0]], x)

    def last_payroll(self):
        return self.state_save[self.states_index[-1]][1]

    def print_payroll(self):
        self.last_payroll().print_vals()

    def print_payroll_calendar(self):
        self.last_payroll().print_calendar()

    def write(self):
        self.overwrite_undo()
        function_dict = {
            self.ADD_EMPLOYEE: PayrollSystem.add_employee,
            self.DEL_EMPLOYEE: PayrollSystem.del_employee,
            self.LAUNCH_TIMECARD: PayrollSystem.launch_timecard,
            self.LAUNCH_SELLING: PayrollSystem.launch_sell_result,
            self.LAUNCH_SERVICE_CHARGE: PayrollSystem.launch_service_charge,
            self.CHANGE_EMPLOYEE_DATA: PayrollSystem.change_employee_data,
            self.CHANGE_EMPLOYEE_TYPE: PayrollSystem.change_employee_type,
            self.RUN_TODAY_PAYROLL: PayrollSystem.run_today_payroll,
            self.UPDATE_DAY: PayrollSystem.update_day,
            self.CHANGE_PAYMENT_SCHEDULE: PayrollSystem.change_payment_schedule,
        }

        index = self.states_index[-1]
        current_payroll = copy.deepcopy(self.state_save[index][1])
        for state in self.state_save[index + 1 : self.current_index]:
            func = function_dict[state[0]]
            if type(state) == list:
                func(current_payroll)
            elif state[0] == self.CHANGE_EMPLOYEE_DATA:
                func(current_payroll, state[1][0], **state[1][1])
            else:
                func(current_payroll, *state[1])

        self.state_save.append((self.PAYROLL_STATE, current_payroll))
        self.states_index.append(self.current_index)
        self.current_index += 1

    def overwrite_undo(self):
        if self.current_index != len(self.state_save):
            inter_arr = [i for i, _ in enumerate(self.state_save[self.current_index:len(self.state_save)])]
            for x in reversed(inter_arr):
                del self.state_save[self.current_index + x]
    
    def undo(self):
        if self.current_index == 1:
            return
        
        if self.state_save[self.current_index-1][0] == self.PAYROLL_STATE:
            del self.states_index[-1]
        
        self.current_index -= 1


    def redo(self):
        if self.current_index == len(self.state_save):
            return
        
        if self.state_save[self.current_index][0] == self.PAYROLL_STATE:
            self.states_index.append(self.current_index)

        self.current_index += 1


if __name__ == '__main__':
    system = QueueSystem(PayrollSystem())

    system.add_employee('simple', 'via st. 11', 'salaried', 1230)
    system.add_employee('alelo', 'maritona st. 19', 'hourly', 12)
    system.add_employee('another', 'via st. 12', 'salaried', 1240)
    system.add_employee('Geredos', 'maritnoa elwoe st. 1', 'commissioned', 13)
    system.add_employee('alelo', 'maritona st. 19', 'hourly', 12)

    system.del_employee(2)
    system.launch_timecard(5, 9)

    system.update_day()

    system.launch_timecard(5, 8)
    system.change_employee_data(1, {'syndicate': True, 'syndicate_charge': 100, 'syndicate_id': 2})
    system.launch_service_charge(1, 100)

    system.launch_selling(4, 2000, 'current')
    system.launch_selling(4, 1200, 'current')
    system.launch_selling(4, 1200, 'current')

    for _ in range(2):
        system.update_day()
        system.run_today_payroll()

    # system.print()
    system.write()

    system.add_employee('zinael', 'via str. 1', 'commissioned', 12)
    system.undo()
    system.undo()
    system.redo()

    system.change_employee_data(3, {'name': 'Ramon', 'syndicate': True, 'syndicate_charge': 100, 'syndicate_id': 1})

    system.write()
    system.print()

    # system.print_payroll()
    # system.print_payroll_calendar()
    system.print_payroll()
    system.change_employee_type(3, 'commissioned')
    system.change_payment_schedule(3, 'weekly 1 friday')
    system.write()
    system.print_payroll()
    # system.last_payroll().employees[]


if __name__ == '__main__ 2':
    payroll = PayrollSystem()

    payroll.add_employee('simple', 'via st. 11', 'salaried', 1230)
    payroll.add_employee('alelo', 'maritona st. 19', 'hourly', 12)
    payroll.add_employee('another', 'via st. 12', 'salaried', 1240)
    payroll.add_employee('Geredos', 'maritnoa elwoe st. 1', 'commissioned', 13)
    payroll.add_employee('alelo', 'maritona st. 19', 'hourly', 12)

    payroll.print_vals()

    payroll.del_employee(2)

    payroll.print_vals()

    payroll.launch_timecard(5, 9)
    # payroll.launch_sell_result(1, 1200, date_offset=1)
    payroll.update_day()
    payroll.launch_timecard(5, 8)
    payroll.launch_service_charge(1, 100)
    payroll.print_calendar()

    # payroll.change_employee_data(3, name='simple_name', syndicate=True, type='Salaried', payment_method='weekly')
    payroll.print_vals()

    payroll.launch_sell_result(4, 2000, 'current')
    payroll.launch_sell_result(4, 1200, 'current')
    payroll.launch_sell_result(4, 1200, 'current')

    payroll.print_calendar()

    from employee import hash_date

    for _ in range(30):
        payroll.update_day()
        payroll.run_today_payroll()
        print('current_day:', hash_date(payroll.current_date))
        payroll.print_calendar()
