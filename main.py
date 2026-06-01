from habit import Habit
from file_connector import FileConnector


def main():
    print("Hello from habit-tracker!")
    file_connector = FileConnector('test.json')
    habits = file_connector.load_habits()


if __name__ == "__main__":
    main()
