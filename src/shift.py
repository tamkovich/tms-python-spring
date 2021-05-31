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
            return shift.date_to + timedelta(1)
        return shift.date_to

    @staticmethod
    def clarify_week_days(shift):  # type(shift) == class Shift
        start, end = shift.time_from.hour, shift.time_to.hour
        clarified_dow = set(shift.week_days[:])
        if start >= end:
            for day in shift.week_days:
                clarified_dow.add(day + 1 if day != 7 else 1)
        return clarified_dow

    @staticmethod
    def get_hours_set(shift):  # type(shift) == class Shift
        HOURS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

        start, end = shift.time_from.hour, shift.time_to.hour
        if start >= end:
            return set(HOURS[start:] + HOURS[:end])
        return set(HOURS[start:end])

    def is_intersect(self, shift_2):  # type(shift_2) == class Shift
        early_shift = self if self.date_from < shift_2.date_from else shift_2
        late_shift = self if self.date_from >= shift_2.date_from else shift_2

        early_date_from = early_shift.date_from
        early_date_to = Shift.clarify_date_to(early_shift)
        late_date_from = late_shift.date_from

        # start, end = early_shift.time_from.hour, early_shift.time_to.hour
        # if start >= end:
        #     early_shift.date_to += timedelta(1)
        #
        # start, end = late_shift.time_from.hour, late_shift.time_to.hour
        # if start >= end:
        #     late_shift.date_to += timedelta(1)

        is_date_intersect = early_date_from <= late_date_from <= early_date_to
        if not is_date_intersect:
            return False

        self_dow = Shift.clarify_week_days(self)
        shift_2_dow = Shift.clarify_week_days(shift_2)
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

        self_hours = Shift.get_hours_set(self)
        shift_2_hours = Shift.get_hours_set(shift_2)

        # HOURS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        #
        # start, end = self.time_from.hour, self.time_to.hour
        # if start >= end:
        #     self_hours = set(HOURS[start:] + HOURS[:end])
        # else:
        #     self_hours = set(HOURS[start:end])
        #
        # start, end = shift_2.time_from.hour, shift_2.time_to.hour
        # if start >= end:
        #     shift_2_hours = set(HOURS[start:] + HOURS[:end])
        # else:
        #     shift_2_hours = set(HOURS[start:end])

        is_time_intersect = not self_hours.isdisjoint(shift_2_hours)
        return is_time_intersect
