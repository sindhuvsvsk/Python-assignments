from datetime import *
import calendar


class BaseCalendar:

    def __init__(self, year="not specified"):
        self.year = int(year)

    def print_day(self):
        month = 2
        cal = calendar.monthcalendar(self.year, month)
        first_week = cal[0]
        if first_week[calendar.MONDAY]:
            third_week = cal[2]
        else:
            third_week = cal[3]
        return date(self.year, month, third_week[calendar.MONDAY])


class MemorialCal(BaseCalendar):

    def __init__(self, year="not specified"):
        super().__init__(year)

    def print_day(self):
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


class LaborCal(BaseCalendar):
    def __init__(self, year="not specified"):
        super().__init__(year)

    def print_day(self):
        month = 9
        c = calendar.monthcalendar(self.year, month)
        first_week = c[0]
        second_week = c[1]
        if first_week[calendar.MONDAY]:
            first_mon = first_week[calendar.MONDAY]
        else:
            first_mon = second_week[calendar.MONDAY]
        return date(self.year, month, first_mon)


class ThanksgivingCal(BaseCalendar):
    def __init__(self, year="not specified"):
        super().__init__(year)

    def print_day(self):
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


base = BaseCalendar('2020')
print(f"President's Day : {base.print_day()}")

mem = MemorialCal('2020')
print(f"Memorial Day : {mem.print_day()}")

labor = LaborCal('2019')
print(f"Labor Day : {labor.print_day()}")

thanks = ThanksgivingCal('2019')
print(f"Thanksgiving day : {thanks.print_day()}")