import tkinter as tk
from tkinter import ttk
import requests

last_telemetry = {}

def update_last_telemetry(robot_id, telemetry_field: tk.Text):
    last_telemetry = requests.post("http://10.7.5.182:8000/api/lasttelemetry", json={
        "robot_id": robot_id
    }).json()

    if not bool(last_telemetry["status"]):
        last_telemetry = {
            "message": last_telemetry["error"]
        }
    else:
        last_telemetry = last_telemetry["telemetry"]

    telemetry_field.config(state=tk.NORMAL)
    telemetry_field.delete("1.0", tk.END)

    telemetry_field.pack()

    for k in last_telemetry:
        telemetry_field.insert(tk.END, '{} = {}\n'.format(k,last_telemetry[k]))

    telemetry_field.config(state = tk.DISABLED)

def telemetryPage(frame, robot_id):

    title_label = tk.Button(frame, text="Update Telemetry", font=("Arial", 16), command=lambda: update_last_telemetry(robot_id(), telemetry_field))
    title_label.pack(pady=10, padx=30)

    telemetry_field = tk.Text(frame)
    telemetry_field.pack()