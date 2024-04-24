from enum import Enum

# Define an enum for the three values
class Activity(Enum):
    FREE = 0
    WORK = 1
    SLEEP = 2
    ACTIVITY = 3

# Define the week data dictionary with enum values
data = {
    0: {hour: Activity.FREE for hour in range(24)},
    1: {hour: Activity.FREE for hour in range(24)},
    2: {hour: Activity.FREE for hour in range(24)},
    3: {hour: Activity.FREE for hour in range(24)},
    4: {hour: Activity.FREE for hour in range(24)},
    5: {hour: Activity.FREE for hour in range(24)},
    6: {hour: Activity.FREE for hour in range(24)}
}

# Function to reset all values to a specified status
def reset_week_data(week_data):
    for day in week_data:
        for hour in week_data[day]:
            week_data[day][hour] = Activity.FREE


def print_week_data(week_data):
    for day, hours in week_data.items():
        print(f'Day {day} from today:')
        for hour, activity in hours.items():
            print(f'    Hour {hour}:00: {activity.name}')

def print_week_activity(week_data):
    for day, hours in week_data.items():
            for hour, activity in hours.items():
                if activity.name == "ACTIVITY":
                    print(f'Day {day} from today:')
                    print(f'    Hour {hour}:00: {activity.name}')

def change_status(week_data, day, hour, new_status):
    if day in week_data and hour in week_data[day]:
        if isinstance(new_status, int):
            try:
                new_status = Activity(new_status)
            except ValueError:
                print('Invalid status value')
                return
        if isinstance(new_status, Activity):
            week_data[day][hour] = new_status
            print(f'Status changed to {new_status.name} for {day} from today, hour {hour}:00')
        else:
            print('Invalid status type')
    else:
        print(f'Invalid day or hour: {day}, {hour}')
