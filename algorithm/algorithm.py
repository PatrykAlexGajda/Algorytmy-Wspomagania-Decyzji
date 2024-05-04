import math
import sys
import os
import get_api
import user_preferenes
import weekly_schedule

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..', 'api'))

week_points = {
    0: {points: 0 for points in range(24)},
    1: {points: 0 for points in range(24)},
    2: {points: 0 for points in range(24)},
    3: {points: 0 for points in range(24)},
    4: {points: 0 for points in range(24)},
    5: {points: 0 for points in range(24)},
    6: {points: 0 for points in range(24)}
}


def print_week_points(week_points):
    for day, points_dict in week_points.items():
        print(f'Day {day}:')
        for hour, points in points_dict.items():
            print(f'    Hour {hour}: Points = {points}')


def reset_week_points(week_points):
    for day in week_points:
        for hour in week_points[day]:
            week_points[day][hour] = 0


def calculate_points(value, perfect_value, std_dev):
    # Calculate the difference between the value and the perfect value
    diff = abs(value - perfect_value)
    
    # Calculate the z-score using the difference and the standard deviation
    z_score = diff / std_dev
    
    # Calculate the probability using the cumulative distribution function (CDF)
    probability = (1 + math.erf(z_score / math.sqrt(2))) / 2
    
    # Map the probability to a range of points (adjust the scale as needed)
    points = 10 - int(probability * 10)
    
    return points


def find_max_points(week_points):
    max_points = 0
    max_day = None
    max_hour = None
    
    for day, points_dict in week_points.items():
        for hour, points in points_dict.items():
            if weekly_schedule.data[day][hour] == weekly_schedule.Activity.FREE:
                if points > max_points:
                    max_points = points
                    max_day = day
                    max_hour = hour
                
    return max_day, max_hour


def calculate_best():
    # iterate thorug weeks 
    weather_info = get_api.get_weather_info()

    for day_hour in weather_info:

        hour_points = calculate_points(day_hour.hour, user_preferenes.data.hour, 10)
        temperature_points = calculate_points(day_hour.temperature, user_preferenes.data.temperature, 10)
        humidity_points = calculate_points(day_hour.humidity, user_preferenes.data.humidity, 10)
        precipitation_probability_points = calculate_points(day_hour.precipitation_probability, user_preferenes.data.precipitation_probability, 10)
        cloud_cover_points = calculate_points(day_hour.cloud_cover, user_preferenes.data.cloud_cover, 10)
        visibility_points = calculate_points(day_hour.visibility, user_preferenes.data.visibility, 10)
        wind_speed_points = calculate_points(day_hour.wind_speed, user_preferenes.data.wind_speed, 10)
        uv_index_points = calculate_points(day_hour.uv_index, user_preferenes.data.uv_index, 10)
        is_day_points = calculate_points(day_hour.is_day, user_preferenes.data.is_day, 10)

        sum_points = hour_points + temperature_points + humidity_points + precipitation_probability_points 
        + cloud_cover_points + visibility_points + wind_speed_points + uv_index_points + is_day_points

        week_points[day_hour.date.weekday()][day_hour.date.hour] = sum_points

    return find_max_points(week_points)


def write_to_calendar():
    chosen_day, chosen_hour = calculate_best()

    weekly_schedule.change_status(weekly_schedule.data, chosen_day, chosen_hour, 3)



# write_to_calendar()

# weekly_schedule.print_week_data(weekly_schedule.data)