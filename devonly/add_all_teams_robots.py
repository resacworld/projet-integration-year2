"""
This script adds each robot of each team to the database.
"""

import requests

all_robots = [
    {
        "robot_id": "53d67923-704f-4b97-b6d4-64a0a04ca5de",
        "name": "MR. KRABS"
    },
    {
        "robot_id": "72a1834d-98ef-4b46-87f5-5e4c4e82e39a",
        "name": "MAXENCE LA FOURMIS"
    },
    {
        "robot_id": "24dcc3a8-3de8-0000-0000-000000000000",
        "name": "GHOST EYES"
    },
    {
        "robot_id": "255f30bc-46f7-41d4-ba1d-db76a0afd7f7",
        "name": "PATH FINDER"
    },
    {
        "robot_id": "efe16b56-45fa-47a3-8f05-04200828eea9",
        "name": "ROBOT OSR (NOUS)"
    },
    {
        "robot_id": "7f377006-cba5-5d50f-a058d-45c5ce970f10",
        "name": "PASTA BOT"
    },
]

url = "http://10.7.5.182:8000/api/addrobot"

for robot in all_robots:
    payload = {
        "robot_id": robot["robot_id"],
        "name": robot["name"]
    }

    response = requests.get(url, params=payload)