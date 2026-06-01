
class Habit:

    def __init__(self, name, base_xp, habit_days, xp_growth_coef):
        self.name = name
        self.habit_days = habit_days
        self.base_xp = base_xp 
        self.xp_growth_coef = xp_growth_coef
        self.__today_submition = False
        self.__days_streak = 0

    def submit_habit(self, user):
        if (self.__today_submition):
            raise Exception("Already submitted this habit")
        user.gain_xp(self.calculate_xp())
        self.__today_submition = True
        self.__days_streak += 1

    def restart_day(self):
        if not self.__today_submition:
            self__days_streak = 0
        self.__today_submition = False

    def calculate_xp(self) -> int:
        xp = self.base_xp + self.__days_streak * self.xp_growth_coef

    def __str__(self):
        return f'Habit {self.name}\nAquires in {self.habit_days}\nBase xp {self.base_xp}\nXp_coef {self.xp_growth_coef}\nStreak: {self.__days_streak}\nDone today: {self.__today_submition}\n'

    
