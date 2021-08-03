from payroll import PayrollSystem

class queue_system:
    def __init__(self):
        return

if __name__ == '__main__':
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

    payroll.launch_sell_result(4, 2000)
    payroll.launch_sell_result(4, 1200)
    payroll.launch_sell_result(4, 1200, date_offset=3)

    payroll.print_calendar()

    from employee import hash_date

    for _ in range(30):
        payroll.update_day()
        payroll.run_today_payroll()
        print('current_day:', hash_date(payroll.current_date))
        payroll.print_calendar()
