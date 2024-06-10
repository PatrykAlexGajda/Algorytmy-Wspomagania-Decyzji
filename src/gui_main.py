import tkinter as tk
from tkinter import messagebox
from user_preferences import UserPreferences
import algorithm
import weekly_schedule
import user_preferences
import os

time_results = ""
chosen_day = 0

def open_week_schedule(entry, current_frame, next_frame):
    input_text = entry.get()
    if input_text:
        current_frame.pack_forget()
        next_frame.pack(expand=True)
        create_schedule_page(next_frame)

def next_page(current_frame, next_frame):
    current_frame.pack_forget()
    if next_frame is None:
        root.destroy()
    else:
        next_frame.pack(expand=True)

def create_schedule_page(schedule_frame, week_schedule):
    schedule_frame.pack(expand=True, fill="both")
    schedule_frame.pack_propagate(0)

    weekdays = ["Day 0", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6"]

    for i, weekday in enumerate(weekdays):
        label = tk.Label(schedule_frame, text=weekday, bg="white", font=("Arial", 14, "bold"))
        label.grid(row=0, column=i+1, padx=0, pady=0, sticky="nsew")

    for hour in range(6, 24):
        label = tk.Label(schedule_frame, text=f"{hour}:00", bg="white", font=("Arial", 12))
        label.grid(row=hour-5, column=0, padx=0, pady=0, sticky="nsew")

    for i, row in enumerate(week_schedule[6:]):
        for j, category in enumerate(row):
            color = "#FFFFFF"
            if category == 3: # ACTIVITY
                color = "#FF0000"  # Red
            elif category == 2: # SLEEP
                color = "#0000FF"  # Blue
            elif category == 1: # WORK
                color = "#FFFF00"  # Yellow
            elif category == 0: # FREE
                color = "#00FF00"  # Green

            slot_frame = tk.Frame(schedule_frame, bg=color, borderwidth=1, relief="solid")
            slot_frame.grid(row=i+1, column=j+1, padx=0, pady=0, sticky="nsew")

    for i in range(len(weekdays) + 1):
        schedule_frame.grid_columnconfigure(i, weight=1, uniform="columns")

    for i in range(18):
        schedule_frame.grid_rowconfigure(i, weight=1)

    empty_label = tk.Label(schedule_frame, bg="white")
    empty_label.grid(row=len(range(6, 24)) + 1, column=len(weekdays) + 1, sticky="nsew")

def check_value(attribute, entry, current_frame, next_frame):
    input_text = entry.get()
    if input_text:
        input_text = int(input_text)
        setattr(user_preferences.data, attribute, input_text)
    current_frame.pack_forget()
    if next_frame is None:
        root.destroy()
    else:
        next_frame.pack(expand=True)



def create_input_page(attr, current_frame, next_frame):
    label = tk.Label(current_frame, text=f"Enter your prefered {attr}:")
    label.config(font=("Arial", 20), background="white", fg="#444444")
    label.pack()

    entry = tk.Entry(current_frame, width=30, font=("Arial", 32), fg="#444444", 
                    bg="white", bd=0, relief="solid", highlightbackground="gray", 
                    cursor="arrow", justify="center")
    entry.pack()

    canvas = tk.Canvas(current_frame, width=400, height=10, 
                       bg=root["bg"], highlightthickness=0)
    canvas.pack()
    canvas.create_line(0, 5, 400, 5, fill="black")

    button = tk.Button(current_frame, text="NEXT PAGE", 
        command = lambda : check_value(attr, entry, current_frame, next_frame), 
        bg="#888888", fg="white", font=("Arial", 14), relief="flat")
    button.pack(pady=10)









def toggle_day_night(current_frame, next_frame):
    def set_preference():
        preference = "Day" if day_night_var.get() == 1 else "Night"
        user_preferences.data.is_day = (preference == "Day")
        current_frame.pack_forget()

        global time_results 
        time_results = algorithm.gui_write_to_calendar_separate()
        choose_day(frame_choose, frame_week)

        if next_frame is not None:
            next_frame.pack(expand=True)

    label = tk.Label(current_frame, text="Do you prefer day or night?")
    label.config(font=("Arial", 20), background="white", fg="#444444")
    label.pack()

    day_night_var = tk.IntVar()
    day_button = tk.Radiobutton(current_frame, text="Day", variable=day_night_var, value=1, bg="white", font=("Arial", 14), fg="#444444")
    night_button = tk.Radiobutton(current_frame, text="Night", variable=day_night_var, value=0, bg="white", font=("Arial", 14), fg="#444444")
    day_button.pack()
    night_button.pack()

    button = tk.Button(current_frame, text="NEXT PAGE", 
                       command=set_preference, 
                       bg="#888888", fg="white", font=("Arial", 14), relief="flat")
    button.pack(pady=10)

def choose_day(current_frame, next_frame):
    label = tk.Label(current_frame, text="CHOOSE THE DAY THAT\nWORKS BEST FOR YOU", font=("Arial", 24), bg="white", fg="#444444")
    label.pack(anchor="n")

    canvas = tk.Canvas(current_frame, width=400, height=10, bg=root["bg"], highlightthickness=0)
    canvas.pack()
    canvas.create_line(0, 5, 400, 5, fill="black")

    label_2 = tk.Label(current_frame, text="\n", font=("Arial", 24), bg="white")
    label_2.pack(anchor="n")

    global time_results
    label_3 = tk.Label(current_frame, text=time_results, font=("Arial", 20), bg="white", fg="#444444")
    label_3.pack(anchor="w")

    def set_chosen_day(day):
        global chosen_day
        chosen_day = day
        algorithm.gui_get_final_week(chosen_day)

        new_week_schedule = []
        for day in range(7):
            day_schedule = [weekly_schedule.data[day][hour].value for hour in range(24)]
            new_week_schedule.append(day_schedule)

        print(new_week_schedule)
        new_week_schedule = list(zip(*new_week_schedule))

        create_schedule_page(frame_week, new_week_schedule)
        next_page(current_frame, frame_week)

    def set_day(day):
        return lambda: set_chosen_day(day)

    canvas = tk.Canvas(current_frame, width=400, height=10, bg=root["bg"], highlightthickness=0)
    canvas.pack()
    canvas.create_line(0, 5, 400, 5, fill="black")

    for i in range(7):
        button = tk.Button(current_frame, text=f"Day {i}", command=set_day(i), bg="#888888", fg="white", font=("Arial", 14), relief="flat")
        button.pack(side="left", padx=10, pady=10)

root = tk.Tk()
root.configure(bg="white")
root.title("Week scheduling app")
root.geometry("800x600")

frame_1 = tk.Frame(root, bg="white")
frame_1.pack(expand=True)
frame_2 = tk.Frame(root, bg="white")
frame_3 = tk.Frame(root, bg="white")
frame_4 = tk.Frame(root, bg="white")
frame_5 = tk.Frame(root, bg="white")
frame_6 = tk.Frame(root, bg="white")
frame_7 = tk.Frame(root, bg="white")
frame_day = tk.Frame(root, bg="white")
frame_choose = tk.Frame(root, bg="white")
frame_week = tk.Frame(root, bg="white")

create_input_page("hour", frame_1, frame_2)
create_input_page("temperature", frame_2, frame_3)
create_input_page("humidity", frame_3, frame_4)
create_input_page("cloud_cover", frame_4, frame_5)
create_input_page("visibility", frame_5, frame_6)
create_input_page("wind_speed", frame_6, frame_7)
create_input_page("uv_index", frame_7, frame_day)
toggle_day_night(frame_day, frame_choose)

root.mainloop()