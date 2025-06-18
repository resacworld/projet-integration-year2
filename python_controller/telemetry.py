"""
AI helped in writing the comments
"""

import tkinter as tk
from tkinter import ttk
import requests

last_telemetry = {}

def update_last_telemetry(robot_id, telemetry_field: tk.Text):
    """!
    Method to get from the web server and update in the tkinter interface the last telemetry
    @param robot_id: ID of the robot to get the telemetry from
    @param telemetry_field: Text field in which the telemetry will be displayed
    """
    
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
    """!
    Create in the frame (given as parameter) the telemetry page
    @param frame: Frame in which the telemetry page will be created
    @param robot_id: Function to get the ID of the robot to which the telemetry is associated
    """

    title_label = tk.Button(frame, text="Update Telemetry", font=("Arial", 16), command=lambda: update_last_telemetry(robot_id(), telemetry_field))
    title_label.pack(pady=10, padx=30)

    telemetry_field = tk.Text(frame)
    telemetry_field.pack()