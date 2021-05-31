from datetime import timedelta

class Shift:
    def __init__(self, time_from, time_to, date_from, date_to, week_days):
        self.time_from = time_from
        self.time_to = time_to
        self.date_from = date_from
        self.date_to = date_to
        self.week_days = week_days

    @staticmethod
    def clarify_date_to(shift):  # type(shift) == class Shift
        start, end = shift.time_from.hour, shift.time_to.hour
        if start >= end:
            shift.date_to += timedelta(1)

    @staticmethod
    def clarify_week_days(shift):  # type(shift) == class Shift
        start, end = shift.time_from.hour, shift.time_to.hour
        clarified_dow = shift.week_days
        if start >= end:
            for day in shift.week_days:
                clarified_dow.add(day + 1 if day != 7 else 1)


    def is_intersect(self, shift_2):  # type(shift_2) == class Shift
        early_shift = self if self.date_from < shift_2.date_from else shift_2
        late_shift = self if self.date_from >= shift_2.date_from else shift_2

        Shift.clarify_date_to(early_shift)
        Shift.clarify_date_to(late_shift)
        # start, end = early_shift.time_from.hour, early_shift.time_to.hour
        # if start >= end:
        #     early_shift.date_to += timedelta(1)
        #
        # start, end = late_shift.time_from.hour, late_shift.time_to.hour
        # if start >= end:
        #     late_shift.date_to += timedelta(1)

        is_date_intersect = early_shift.date_from <= late_shift.date_from <= early_shift.date_to
        if not is_date_intersect:
            return False

        # self_dow = set(self.week_days)
        # start, end = self.time_from.hour, self.time_to.hour
        # if start >= end:
        #     for day in self.week_days:
        #         self_dow.add(day + 1 if day != 7 else 1)
        #
        # shift_2_dow = set(shift_2.week_days)
        # start, end = shift_2.time_from.hour, shift_2.time_to.hour
        # if start >= end:
        #     for day in shift_2.week_days:
        #         shift_2_dow.add(day + 1 if day != 7 else 1)

        is_dow_intersect = not self_dow.isdisjoint(shift_2_dow)
        if not is_dow_intersect:
            return False

        hours = list(range(24))
        start, end = self.time_from.hour, self.time_to.hour
        if start >= end:
            self_hours = set(hours[start:] + hours[:end])
        else:
            self_hours = set(hours[start:end])

        start, end = shift_2.time_from.hour, shift_2.time_to.hour
        if start >= end:
            shift_2_hours = set(hours[start:] + hours[:end])
        else:
            shift_2_hours = set(hours[start:end])

        is_time_intersect = not self_hours.isdisjoint(shift_2_hours)
        return is_time_intersect
