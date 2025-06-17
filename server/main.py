from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.index import MasterRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database.models.robot import RobotRepository, Robot, RobotId
from database.models.mission import MissionRepository, Mission
from database.models.block import BlockRepository, Block
from typing import List

# Initialize the FastAPI application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # seulement si tu envoies des cookies ou auth headers
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# link the router to the fastapi instance
app.include_router(MasterRouter)

def getFullMission(mission: Mission, blocks: List[Block]):
    json_mission = mission.to_json()
    json_mission["blocks"] = [block.to_json() for block in blocks]

    return json_mission

def getAllMissions(robot_id: str):
    db_mission = MissionRepository()
    db_block = BlockRepository()
    db_robot = RobotRepository()

    missions = db_mission.find_all_by_robot_id(robot_id)

    return [getFullMission(mission, db_block.find_many_by_mission_id(mission.id)) for mission in missions]

# Define the default route
# @app.get("/", response_class=HTMLResponse)
# async def root():
#     with open('static/index.html', 'r') as file:
#         return file.read()


def getAllGraphicalMissions(missions: List):
    allGMissions = ""

    for mission in missions:  
        allGMissions += f"""           
        <div class="card">
            <h3 htmlFor="name">Mission : <span class="span">{mission["name"]}</span></h3>
            
            {(
                "<h3 class=\"tag yellow\">Running</h3>" if mission["executing"] else (
                "<h3 class=\"tag orange\">Finished</h3>" if mission["finished"] else (
                "<h3 class=\"tag green\">New</h3>"
            )))}

            <div class="flex">
                {''.join([f"""<div>
                    <h3 htmlFor="name" class="microcard">{block["block_nb"]}</h3>
                </div>""" for block in mission["blocks"]])}
            </div>
        </div>
        """

    return allGMissions


def getRobotSelectOptions(robots: List[Robot], selectedRobotId: str = None):
    options = ""
    for robot in robots:
        options += f'<option value="{robot.id}" {"selected" if selectedRobotId == str(robot.id) else ""}>{robot.name}</option>'
    return options

@app.get("/", response_class=HTMLResponse)
async def root(status: bool = None, selected_id: str = None):
    db_robot = RobotRepository()
    robots = db_robot.find_all()

    if selected_id is not None:
        # If a robot is selected, we keep it
        selectedRobotId = selected_id
    else:
        # Else, we take the first robot's id
        selectedRobotId  = str(robots[0].id)

    missions  = getAllMissions(selectedRobotId)

    return f"""
    <!DOCTYPE html>
    <html lang="en"> 
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The beautiful ihm</title>
        <link href="/static/index.css" rel="stylesheet"> 
    </head>
    <body>
        <div class="root">
            <div class="addrobotsection">
                <form action="/api/addrobot" method="get">
                    <h2 class="maintitle">Add a robot</h2>
                    <div class="home">
                        <div class="bg-red grid gap-6 mb-2">
                            <div>
                                <label for="name" class="field">Robot name (required)</label>
                                <input type="text" id="name" name="name" class="inputfield" placeholder="robot name" required />
                            </div>
                            <div>
                                <label for="robot_id" class="field">Robot id (optional)</label>
                                <input type="text" id="robot_id" name="robot_id" class="inputfield" placeholder="uuid" />
                            </div>
                        </div>
                        <button type="submit" class="submitbtn">Submit</button>
                    </div>
                </form>
                <p class="{"text-green" if status else "text-red"}">{"" if status == None else ("Successfully added" if status else "Error")}</p>
            </div>
            <div class="missionssection">
                <h2 class="maintitle">Missions</h2>
                <div>
                    <form class="formselect">
                        <label htmlFor="selected_id" class="field">Select a robot</label>
                        <div class="flex">
                            <select 
                                id="selected_id"
                                name="selected_id"
                                class="inputfield">
                                {getRobotSelectOptions(robots=robots, selectedRobotId=selectedRobotId)}
                            </select>
                            <button type="submit" class="shortsubmit">update</button>
                        </div>
                    </form>
                    
                    <div class="missions-list">
                        {("Aucune mission enregistrée" if (missions == None or len(missions) == 0) else getAllGraphicalMissions(missions=missions))}
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
"""
