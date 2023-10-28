import datetime


class KaizerChiefsDays:
    last_day = datetime.datetime(2015, 5, 9)
    current_day = datetime.datetime.now()

    def execute(self):
        number_of_days = self.current_day - self.last_day
        return f"it's been {number_of_days.days // 365} years or {number_of_days.days} days since Kaizer Chiefs last won a title"
