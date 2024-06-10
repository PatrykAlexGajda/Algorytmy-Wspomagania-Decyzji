import algorithm
import user_preferences
import weekly_schedule

def input_process(param, string_temp):
    if string_temp == '':
        return
    param = int(string_temp)

def main():
    print("Hello - console app scheduler")
    
    hour_t, temperature_t, humidity_t, percipitation_probability_t, cloud_cover_t, visibility_t, wind_speed_t, uv_index_t, is_day_t = user_preferences.data.bind_attributes()

    input_process(hour_t, input("Enter your prefered hour: "))
    input_process(temperature_t, input("Enter your prefered temperature: "))
    input_process(humidity_t, input("Enter your prefered humidity: "))
    input_process(percipitation_probability_t, input("Enter your prefered rain: "))
    input_process(cloud_cover_t, input("Enter your prefered cloud cover: "))
    input_process(visibility_t, input("Enter your prefered visibility: "))
    input_process(wind_speed_t, input("Enter your prefered wind speed: "))
    input_process(uv_index_t, input("Enter your prefered uv index: "))
    input_process(is_day_t, input("Is day ora night better: "))

    while(True):
        if input("You have some addictional acivity (y/n): ") != "y":
            break
        day_a = int(input("Which day: "))
        hour_a = int(input("Which hour: "))

        weekly_schedule.change_status(weekly_schedule.data, day_a, hour_a, 1)
    
    user_preferences.data.update_values(hour_t, temperature_t, humidity_t, percipitation_probability_t, cloud_cover_t, visibility_t, wind_speed_t, uv_index_t, is_day_t)

    # algorithm.write_to_calendar()
    algorithm.write_to_calendar_separate()

    print("\n\n")
    algorithm.rich_print_week_points(algorithm.week_points)
    print("\n\n")
    weekly_schedule.print_week_activity(weekly_schedule.data)
    print("\n\n")

if __name__ == "__main__":
    main()
