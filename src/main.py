from payroll import PayrollSystem

# calendar.isleap is to see if a year is leap, basically it runs a year % 4
# using the module datetime to use the datetime.date data type
# to add a day to datetime.date format is to add the datetime.timedelta(day=1)
# using the calendar.monthcalendar function to get array of days per month
#     [0,1,2,3,4,5,6], [7, ...] ...

def get_date_format(date):
    return date.year, date.month, date.day

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
        print('current_day:', hash_date(payroll.current_date))
        payroll.print_calendar()
