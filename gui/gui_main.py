import tkinter as tk
from tkinter import messagebox

def check_value(entry, frame_old, frame_new):
    input_text = entry.get()
    if input_text:

        frame_old.pack_forget()
        frame_new.pack(expand=True)

def open_week_schedule(entry, current_frame, next_frame):
    input_text = entry.get()
    if input_text:
        current_frame.pack_forget()
        next_frame.pack(expand=True)
        create_schedule_page(next_frame)

def create_schedule_page(root):
    schedule_frame = tk.Frame(root, bg="white")
    schedule_frame.pack(expand=True, fill="both")
    schedule_frame.pack_propagate(0)  # Prevent automatic resizing of the frame

    # Weekday labels
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i, weekday in enumerate(weekdays):
        label = tk.Label(schedule_frame, text=weekday, bg="white", font=("Arial", 14, "bold"))
        label.grid(row=0, column=i+1, padx=0, pady=0, sticky="nsew")

    # Time labels
    for hour in range(6, 24):
        label = tk.Label(schedule_frame, text=f"{hour}:00", bg="white", font=("Arial", 12))
        label.grid(row=hour-5, column=0, padx=0, pady=0, sticky="nsew")

    # Slots for each hour
    for hour in range(6, 24):
        for day in range(len(weekdays)):
            slot_frame = tk.Frame(schedule_frame, bg="white", borderwidth=1, relief="solid")
            slot_frame.grid(row=hour-5, column=day+1, padx=0, pady=0, sticky="nsew")

    # Configure uniform column weight to make all columns have the same width
    for i in range(len(weekdays) + 1):
        schedule_frame.grid_columnconfigure(i, weight=1, uniform="columns")

    # Configure row weights to make the grid cells expand vertically to fill the window
    for i in range(18):
        schedule_frame.grid_rowconfigure(i, weight=1)

    # Add empty label at the bottom-right corner to fill space
    empty_label = tk.Label(schedule_frame, bg="white")
    empty_label.grid(row=len(range(6, 24)), column=len(weekdays) + 1, sticky="nsew")



root = tk.Tk()
root.configure(bg="white")
root.title("Week scheduling app")
root.geometry("800x600")



# FRAMES
frame_1 = tk.Frame(root, bg="white")
frame_1.pack(expand=True)
frame_2 = tk.Frame(root, bg="white")
frame_3 = tk.Frame(root, bg="white")
frame_4 = tk.Frame(root, bg="white")
frame_5 = tk.Frame(root, bg="white")
frame_6 = tk.Frame(root, bg="white")
frame_week = tk.Frame(root, bg="white")



# LABEL
label = tk.Label(frame_1, text="Enter your prefered hour:")
label.config(font=("Arial", 20), background="white", fg="#444444")
label.pack()
# ENTRY
entry = tk.Entry(frame_1, width=30, font=("Arial", 32), fg="#444444", bg="white", 
                 bd=0, relief="solid", highlightbackground="gray", cursor="arrow", justify="center")
entry.pack()
# UNDERLINE FOR ENTRY
canvas = tk.Canvas(frame_1, width=400, height=10, bg=root["bg"], highlightthickness=0)
canvas.pack()
canvas.create_line(0, 5, 400, 5, fill="black")
# BUTTON
button = tk.Button(frame_1, text="NEXT PAGE", 
                   command=lambda arg1=entry, arg2=frame_1, arg3=frame_2: check_value(arg1, arg2, arg3), 
                   bg="#888888", fg="white", font=("Arial", 14), relief="flat")
button.pack(pady=10)



label_2 = tk.Label(frame_2, text="Enter your prefered temperature:")
label_2.config(font=("Arial", 20), background="white", fg="#444444")
label_2.pack()

entry_2 = tk.Entry(frame_2, width=30, font=("Arial", 32), fg="#444444", bg="white", 
                 bd=0, relief="solid", highlightbackground="gray", cursor="arrow", justify="center")
entry_2.pack()

canvas_2 = tk.Canvas(frame_2, width=400, height=10, bg=root["bg"], highlightthickness=0)
canvas_2.pack()
canvas_2.create_line(0, 5, 400, 5, fill="black")

button_2 = tk.Button(frame_2, text="NEXT PAGE", 
                    command=lambda arg1=entry_2, arg2=frame_2, arg3=frame_3: check_value(arg1, arg2, arg3), 
                     bg="#888888", fg="white", font=("Arial", 14), relief="flat")
button_2.pack(pady=10)



label_3 = tk.Label(frame_3, text="Enter your prefered humidity:")
label_3.config(font=("Arial", 20), background="white", fg="#444444")
label_3.pack()

entry_3 = tk.Entry(frame_3, width=30, font=("Arial", 32), fg="#444444", bg="white", 
                 bd=0, relief="solid", highlightbackground="gray", cursor="arrow", justify="center")
entry_3.pack()

canvas_3 = tk.Canvas(frame_3, width=400, height=10, bg=root["bg"], highlightthickness=0)
canvas_3.pack()
canvas_3.create_line(0, 5, 400, 5, fill="black")

button_3 = tk.Button(frame_3, text="NEXT PAGE", 
                     command=lambda arg1=entry_3, arg2=frame_3, arg3=frame_4: check_value(arg1, arg2, arg3), 
                     bg="#888888", fg="white", font=("Arial", 14), relief="flat")
button_3.pack(pady=10)



label_4 = tk.Label(frame_4, text="Enter your prefered cloud cover:")
label_4.config(font=("Arial", 20), background="white", fg="#444444")
label_4.pack()

entry_4 = tk.Entry(frame_4, width=30, font=("Arial", 32), fg="#444444", bg="white", 
                 bd=0, relief="solid", highlightbackground="gray", cursor="arrow", justify="center")
entry_4.pack()

canvas_4 = tk.Canvas(frame_4, width=400, height=10, bg=root["bg"], highlightthickness=0)
canvas_4.pack()
canvas_4.create_line(0, 5, 400, 5, fill="black")

button_4 = tk.Button(frame_4, text="NEXT PAGE", 
                     command=lambda arg1=entry_4, arg2=frame_4, arg3=frame_5: check_value(arg1, arg2, arg3), 
                     bg="#888888", fg="white", font=("Arial", 14), relief="flat")
button_4.pack(pady=10)



label_5 = tk.Label(frame_5, text="Enter your prefered wind speed:")
label_5.config(font=("Arial", 20), background="white", fg="#444444")
label_5.pack()

entry_5 = tk.Entry(frame_5, width=30, font=("Arial", 32), fg="#444444", bg="white", 
                 bd=0, relief="solid", highlightbackground="gray", cursor="arrow", justify="center")
entry_5.pack()

canvas_5 = tk.Canvas(frame_5, width=400, height=10, bg=root["bg"], highlightthickness=0)
canvas_5.pack()
canvas_5.create_line(0, 5, 400, 5, fill="black")

button_5 = tk.Button(frame_5, text="NEXT PAGE", 
                     command=lambda arg1=entry_5, arg2=frame_5, arg3=frame_6: check_value(arg1, arg2, arg3), 
                     bg="#888888", fg="white", font=("Arial", 14), relief="flat")
button_5.pack(pady=10)



label_6 = tk.Label(frame_6, text="Is day or a night better:")
label_6.config(font=("Arial", 20), background="white", fg="#444444")
label_6.pack()

entry_6 = tk.Entry(frame_6, width=30, font=("Arial", 32), fg="#444444", bg="white", 
                 bd=0, relief="solid", highlightbackground="gray", cursor="arrow", justify="center")
entry_6.pack()

canvas_6 = tk.Canvas(frame_6, width=400, height=10, bg=root["bg"], highlightthickness=0)
canvas_6.pack()
canvas_6.create_line(0, 5, 400, 5, fill="black")

button_6 = tk.Button(frame_6, text="NEXT PAGE", 
                     command=lambda: open_week_schedule(entry_6, frame_6, frame_week), 
                     bg="#888888", fg="white", font=("Arial", 14), relief="flat")
button_6.pack(pady=10)


root.mainloop()