import tkinter as tk
from tkinter import ttk
import requests
from typing import List
from pydantic import BaseModel

comboBoxes:List[ttk.Combobox] = []

class Robot (BaseModel):
    id: str
    mac: str
    name: str

robots_json = requests.get("http://10.7.5.182:8000/api/robots").json()["robots"]

robots = [Robot(id=robot["id"], mac=robot["mac"], name=robot["name"]) for robot in robots_json]

if len(robots) == 0:
     raise Exception("Server need to store at least one robot to be working !")

root = tk.Tk()
blocks_frame = tk.Frame(root)

def add_mission():
    blocks_to_send = []

    for block in comboBoxes:
         blocks_to_send.append([2, 3, 6, 7, 10][block.current()])

    url = "http://10.7.5.182:8000/api/addmission"
    payload = {
        "robot_id": robots[robot_number.current()].id,
        "blocks": blocks_to_send,
        "name": mission_entry.get(),
        "status": True
    }

    print(payload)

    response = requests.post(url, json=payload)

    print(response.status_code)
    print(response.json())

def add_block():
        block_frame = tk.Frame(blocks_frame, bd=2, relief=tk.GROOVE, padx=10, pady=5)
        block_frame.pack(fill=tk.X, pady=5, padx=10)

        # Numéro de bloc
        tk.Label(block_frame, text="N° bloc :", padx=10).grid(row=0, column=0, sticky="w")
        block_number = ttk.Combobox(block_frame, values=["2 - Jaune", "3 - Rouge", "6 - Rose", "7 - Bleu", "10 - Vert"], width=20, )
        block_number.grid(row=0, column=1)
        block_number.current(0)  # valeur par défaut

        # Sauvegarde de la référence
        comboBoxes.append(block_number)

root.title("Basic Tkinter GUI")
root.geometry("500x350")

title_label = tk.Label(root, text="Ajouter une mission", font=("Arial", 16))
title_label.pack(pady=10, padx=30)

name_frame = tk.Frame(root, bd=0, relief=tk.GROOVE, padx=10, pady=5,)
name_frame.pack()

tk.Label(name_frame, text="Selectionnez robot :")
robot_number = ttk.Combobox(name_frame, values=[robot.name for robot in robots], width=20)
robot_number.grid(row=0, column=0, padx=10, pady=5)
# robot_number.grid(row=0, column=1)
robot_number.current(0)

mission_label = tk.Label(name_frame, text="Nom de la mission:", padx=10)
# mission_label.pack(pady=10)
mission_label.grid(row=1, column=0)

mission_entry = tk.Entry(name_frame)
# mission_entry.pack(pady=5, padx=30)
mission_entry.grid(row=1, column=1)

blocks_frame.pack(pady=10, fill=tk.BOTH, expand=True)

add_block_button = tk.Button(text="Ajouter un bloc", command=add_block)
add_block_button.pack(pady=10)


# Add a start button
button = tk.Button(root, text="Envoyer mission", command=add_mission)
button.pack(pady=10, padx=30)

# Run the application
root.mainloop()