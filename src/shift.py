class Shift:
    def __init__(self, shift_info):
        self.time_from = shift_info['time_from']
        self.time_to = shift_info['time_to']
        self.date_from = shift_info['date_from']
        self.date_to = shift_info['date_to']
        self.week_days = shift_info['week_days']

    def is_intersect(self, shift_2):

        early_shift = self if self.date_from < shift_2.date_from else shift_2
        late_shift = self if self.date_from >= shift_2.date_from else shift_2

        is_date_intersect = early_shift.date_from <= late_shift.date_from <= early_shift.date_to
        if not is_date_intersect:
            return False

        is_dow_intersect = not set(self.week_days).isdisjoint(set(shift_2.week_days))
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
