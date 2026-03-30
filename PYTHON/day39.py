import tkinter as tk
from tkinter import ttk
import time
import calendar
from datetime import datetime

# Create main window
root = tk.Tk()
root.title("Simple Clock & Calendar")
root.geometry("400x400")

# -------- CLOCK --------
clock_label = ttk.Label(root, font=("Arial", 20))
clock_label.pack(pady=20)

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text="Time: " + current_time)
    clock_label.after(1000, update_clock)

# -------- CALENDAR --------
cal_label = ttk.Label(root, font=("Courier", 10), justify="left")
cal_label.pack(pady=20)

def show_calendar():
    now = datetime.now()
    year = now.year
    month = now.month

    cal_text = calendar.month(year, month)
    cal_label.config(text=cal_text)

# Run functions
update_clock()
show_calendar()

# Start GUI loop
root.mainloop()