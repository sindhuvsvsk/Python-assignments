from datetime import *
import calendar


class MySmartCalendar:

    def __init__(self, year="not specified"):
        self.year = int(year)

    def is_leap_year(self):
        return calendar.isleap(self.year)

    def get_memorial_day(self):
        month = 5
        cal = calendar.monthcalendar(self.year, month)
        weeks = len(cal)
        if weeks == 6:
            last_week = cal[5]
            last_before_week = cal[4]
        elif weeks == 5:
            last_week = cal[4]
            last_before_week = cal[3]
        else:
            last_week = cal[3]
            last_before_week = cal[4]
        if last_week[calendar.MONDAY]:
            last_mon = last_week[calendar.MONDAY]
        else:
            last_mon = last_before_week[calendar.MONDAY]
        return date(self.year, month, last_mon)

    def get_labor_day(self):
        month = 9
        c = calendar.monthcalendar(self.year, month)
        first_week = c[0]
        second_week = c[1]
        if first_week[calendar.MONDAY]:
            first_mon = first_week[calendar.MONDAY]
        else:
            first_mon = second_week[calendar.MONDAY]
        return date(self.year, month, first_mon)

    def get_thanksgiving_day(self):
        month = 11
        cal = calendar.monthcalendar(self.year, month)
        first_week = cal[0]
        if first_week[calendar.THURSDAY]:
            fourth_week = cal[3]
        else:
            fourth_week = cal[4]
        return date(self.year, month, fourth_week[calendar.THURSDAY])

    def print_calendar(self):
        cal = calendar.TextCalendar(calendar.SUNDAY)
        return cal.formatyear(self.year)


smart = MySmartCalendar('2020')
print(f"Is a Leap Year ? : {smart.is_leap_year()}")
print(f"Memorial Day : {smart.get_memorial_day()}")
print(f"Labor Day : {smart.get_labor_day()}")
print(f"Thanksgiving day : {smart.get_thanksgiving_day()}")
print(smart.print_calendar())
