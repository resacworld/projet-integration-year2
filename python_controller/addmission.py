"""
AI helped in writing the comments
"""

import tkinter as tk
from tkinter import ttk
from typing import List
import requests

comboBoxes:List[ttk.Combobox] = []

def add_mission(robot_id, mission_name, return_label: tk.Label):
    """!
    Register a mission in the database
    @param robot_id: ID of the robot to which the mission is associated
    @param mission_name: Name of the mission to register
    @param return_label: Label to display the result of the operation

    """

    blocks_to_send = []

    for block in comboBoxes:
         blocks_to_send.append([2, 3, 6, 7, 10][block.current()])

    url = "http://10.7.5.182:8000/api/addmission"
    payload = {
        "robot_id": robot_id,
        "blocks": blocks_to_send,
        "name": mission_name,
        "status": True
    }

    print(payload)

    response = requests.post(url, json=payload)

    json_res = response.json()

    if json_res["status"]:
        return_label.config(text="Sucessfully added", fg="green")
    else:
        return_label.config(text=f"Error - not added : {json_res["error"]}", fg="red")
    
def del_block(block_frame: tk.Frame, block_number: ttk.Combobox):
    """!
    Delete a block element from the current mission (in creation)
    @param block_frame: Frame to delete
    @param block_number: Combobox to delete on the list of blocks
    """

    if len(comboBoxes) == 0:
        return

    comboBoxes.remove(block_number)
    block_frame.destroy()

def add_block(frame):
    """!
    Add a block element to the current mission (in creation)
    @param frame: Frame in which the block will be added
    """

    if len(comboBoxes) == 5:
        return

    block_frame = tk.Frame(frame, bd=2, relief=tk.GROOVE, padx=10, pady=5)
    block_frame.pack(fill=tk.X, pady=5, padx=10)

    # Numéro de bloc
    tk.Label(block_frame, text="N° bloc :", padx=10).grid(row=0, column=0, sticky="w")
    block_number = ttk.Combobox(block_frame, values=["2 - Jaune", "3 - Rouge", "6 - Rose", "7 - Bleu", "10 - Vert"], width=20, )
    block_number.grid(row=0, column=1)
    block_number.current(0)  # valeur par défaut

    # buoutton pour supprimer le bloc
    delete_button = tk.Button(block_frame, text="Delete", command=lambda: del_block(block_frame, block_number))
    delete_button.grid(row=0, column=2, padx=5)

    # Sauvegarde de la référence
    comboBoxes.append(block_number)

def addMissionPage(frame, robot_id):
    """!
    Create in the frame (given as parameter) the Mission page
    @param frame: Frame in which the mission page will be created
    @param robot_id: Function to get the ID of the robot to which the mission is associated
    """

    blocks_frame = tk.Frame(frame)

    title_label = tk.Label(frame, text="Add a mission", font=("Arial", 16))
    title_label.pack(pady=10, padx=30)

    name_frame = tk.Frame(frame, bd=0, relief=tk.GROOVE, padx=10, pady=5,)
    name_frame.pack()

    mission_label = tk.Label(name_frame, text="Mission's name:", padx=10)
    # mission_label.pack(pady=10)
    mission_label.grid(row=1, column=0)

    mission_entry = tk.Entry(name_frame)
    # mission_entry.pack(pady=5, padx=30)
    mission_entry.grid(row=1, column=1)

    blocks_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    add_block_button = tk.Button(frame, text="Add a block", command=lambda: add_block(frame))
    add_block_button.pack(pady=10)

    # Add a start button
    button = tk.Button(frame, text="Send mission", command=lambda: add_mission(robot_id(), mission_entry.get(), title_label))
    button.pack(pady=10, padx=30)

    title_label = tk.Label(frame, text="Response ---", font=("Arial", 8))
    title_label.pack(pady=10, padx=30)