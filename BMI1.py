from tkinter import *
from tkinter import ttk
import os
from datetime import datetime
import matplotlib.pyplot as plt

co0 = "#444466"
co1 = "#feffff"
co2 = "#6856FF"

history_file = "bmi_history.txt"

if os.path.exists(history_file):
    with open(history_file, "r") as file:
        bmi_history = file.read().splitlines()
else:
    bmi_history = []

window = Tk()
window.title('')
window.geometry('295x380')
window.resizable(height=FALSE, width=FALSE)
window.configure(bg=co1)

top_frame = Frame(window, width=295, height=50, bg=co1, pady=0, padx=0)
top_frame.grid(row=0, column=0)

down_frame = Frame(window, width=295, height=330, bg=co1, pady=0, padx=0)
down_frame.grid(row=1, column=0)

app_name = Label(top_frame, text="BMI Calculator", width=23, height=1, padx=0, anchor="center", font=("Ivy 16 bold"), bg=co1, fg=co0)
app_name.place(x=0, y=2)

app_line = Label(top_frame, text="", width=400, height=1, padx=0, anchor="center", font=("Arial 1"), bg=co2, fg=co0)
app_line.place(x=0, y=35)

def calculate():
    try:
        weight = float(e_weight.get())
        height = float(e_height.get()) ** 2
        result = weight / height

        if result < 18.4:
            category = "Underweight"
        elif result >= 18.5 and result < 24.9:
            category = "Normal"
        elif result >= 25 and result < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"