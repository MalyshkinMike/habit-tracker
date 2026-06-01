from habit import Habit
import json

class FileConnector:

    def __init__(self, path: str):
        self.__path = path

    def save_habits(self, habits: list[Habit]):
        file = open(self.__path, 'w')
        json.dump([habit.__dict__ for habit in habits], file)
    
    def habit_decoder(self, dct):
        return Habit(dct['name'], dct['base_xp'], dct['habit_days'], dct['xp_growth_coef'])

    def load_habits(self) -> list[Habit]:
        file = open(self.__path, 'r')
        habits = json.load(file, object_hook=self.habit_decoder)
        return habits


