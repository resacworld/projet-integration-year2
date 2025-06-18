"""
AI helped in writing the comments
"""

import tkinter as tk
from tkinter import ttk
import requests
from pydantic import BaseModel
from telemetry import telemetryPage
from addmission import addMissionPage

class Robot (BaseModel):
    id: str
    name: str

# We get the robots from the server
robots_json = requests.get("http://10.7.5.182:8000/api/robots").json()["robots"]
robots = [Robot(id=robot["id"], name=robot["name"]) for robot in robots_json]

# Check if there is at least one robot
if len(robots) == 0:
     raise Exception("Server need to store at least one robot to be working !")

# Initialize the main window
root = tk.Tk()

root.title("Basic Tkinter GUI")
root.geometry("500x600")

top_frame = ttk.Frame(root)

# Robot selection
title = tk.Label(top_frame, text="Select a robot :", padx=10)
robot_number = ttk.Combobox(top_frame, values=[robot.name for robot in robots], width=20)
robot_number.current(0)

title.grid(row=0, column=1)
robot_number.grid(row=0, column=2)

top_frame.pack(fill="x", expand=True, pady=10, side="top")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Create two frames for the notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# Add the titles for the frames
notebook.add(frame1, text='Add mission')
notebook.add(frame2, text='Telemetry')

# Add the pages to the frames
addMissionPage(frame1, lambda: robots[robot_number.current()].id)
telemetryPage(frame2, lambda: robots[robot_number.current()].id)

# Run the application
root.mainloop()