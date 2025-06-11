import React from "react";
import AddRobot from "./AddRobot";
import Missions from "./Missions";

export default ({}) => {
    return <div className="flex flex-row overflow-y-auto">
        <AddRobot />
        <Missions />
    </div>
}