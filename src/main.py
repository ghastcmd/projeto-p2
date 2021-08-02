from payroll import PayrollSystem as PS

# calendar.isleap is to see if a year is leap, basically it runs a year % 4
# using the module datetime to use the datetime.date data type
# to add a day to datetime.date format is to add the datetime.timedelta(day=1)
# using the calendar.monthcalendar function to get array of days per month
#     [0,1,2,3,4,5,6], [7, ...] ...

def get_date_format(date):
    return date.year, date.month, date.day

if __name__ == '__main__':
    payroll = PS()

    payroll.add_employee('simple', 'via st. 11', 'salaried', 1230)
    payroll.add_employee('alelo', 'maritona st. 19', 'hourly', 12)
    payroll.add_employee('another', 'via st. 12', 'salaried', 1240)

    payroll.print_vals()

    payroll.del_employee(2)

    payroll.print_vals()

    payroll.launch_timecard(1, 9)
    payroll.launch_sell_result(1, 1200, date_offset=1)
    payroll.update_day()
    payroll.launch_timecard(1, 8)
    payroll.launch_service_charge(1, 100)
    payroll.print_calendar()

    payroll.change_employee_data(3, name='simple_name', syndicate=True, type='salaried', payment_method='weekly')
    payroll.print_vals()

    payroll.employees[0].generate_payment(payroll.current_date, payroll.calendar)
    # payroll.employees[1].generate_payment(payroll.current_date, payroll.calendar)