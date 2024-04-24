import algorithm
import user_preferenes
import weekly_schedule

def main():
    print("Hello - console app scheduler")
    
    hour_t = int(input("Enter your prefered hour: "))
    temperature_t = int(input("Enter your prefered temperature: "))
    humidity_t = int(input("Enter your prefered humidity: "))
    percipitation_probability_t = int(input("Enter your prefered rain: "))
    cloud_cover_t = int(input("Enter your prefered cloud cover: "))
    visibility_t = int(input("Enter your prefered visibility: "))
    wind_speed_t = int(input("Enter your prefered wind speed: "))
    uv_index_t = int(input("Enter your prefered uv index: "))
    is_day_t = int(input("Is day ora night better: "))

    while(True):
        if input("You have some addictional acivity (y/n): ") != "y":
            break
        day_a = int(input("Which day: "))
        hour_a = int(input("Which hour: "))

        weekly_schedule.change_status(weekly_schedule.data, day_a, hour_a, 1)
    
    user_preferenes.data.update_values(hour_t, temperature_t, humidity_t, percipitation_probability_t, cloud_cover_t, visibility_t, wind_speed_t, uv_index_t, is_day_t)

    algorithm.write_to_calendar()

    weekly_schedule.print_week_activity(weekly_schedule.data)

if __name__ == "__main__":
    main()



    