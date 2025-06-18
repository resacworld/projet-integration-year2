# ! AI help on the creation of this file !

from database.models.robot import RobotRepository, Robot
from database.models.mission import MissionRepository, Mission
from database.models.block import BlockRepository, Block
from typing import List

def getFullMission(mission: Mission, blocks: List[Block]):
    """!
    Function to get the full mission with its blocks
    @param mission: Mission object
    @param blocks: List of Block objects associated with the mission
    @return Dictionary representation of the mission with its blocks
    """

    json_mission = mission.to_json()
    json_mission["blocks"] = [block.to_json() for block in blocks]

    return json_mission

def getAllMissions(robot_id: str):
    """!
    Function to get all missions of a robot
    @param robot_id: ID of the robot
    @return List of mission dictionaries with their blocks
    """

    db_mission = MissionRepository()
    db_block = BlockRepository()
    db_robot = RobotRepository()

    missions = db_mission.find_all_by_robot_id(robot_id)

    return [getFullMission(mission, db_block.find_many_by_mission_id(mission.id)) for mission in missions]

def getGraphicalMissions(missions: List):
    """!
    Function to get the HTML representation of all missions
    @param missions: List of mission dictionaries
    @return HTML string of all missions
    """

    allGMissions = ""

    for mission in missions:  
        allGMissions += f"""           
        <div class="card">
            <h3 htmlFor="name"><span class="span">{mission["name"]}</span></h3>
            
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


def getGraphicalRobotSelectOptions(robots: List[Robot], selectedRobotId: str = None):
    """!
    Function to get the HTML options for the robot select dropdown
    @param robots: List of Robot objects
    @param selectedRobotId: ID of the selected robot
    @return HTML string of options for the select dropdown
    """

    options = ""
    for robot in robots:
        options += f'<option value="{robot.id}" {"selected" if selectedRobotId == str(robot.id) else ""}>{robot.name}</option>'
    return options


def getFullHomePage(status: bool = None, selected_id: str = None):
    """!
    Function to get the full home page (in HTML) with robots and missions
    @param status: Status of the last operation (True for success, False for error)
    @param selected_id: ID of the selected robot
    @return HTML string of the home page
    """

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
                                {getGraphicalRobotSelectOptions(robots=robots, selectedRobotId=selectedRobotId)}
                            </select>
                            <button type="submit" class="shortsubmit">update</button>
                        </div>
                    </form>
                    
                    <div class="missions-list">
                        {("No missions" if (missions == None or len(missions) == 0) else getGraphicalMissions(missions=missions))}
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
"""
