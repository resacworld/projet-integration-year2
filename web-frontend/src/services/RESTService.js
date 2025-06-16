import axios from 'axios';

/**
 * Register a robot, unique name is required
 * @param {str} name - The name of the robot to register
 * @returns {object} The status of the request
 */
export const registerRobot = async (name) => {
    return (await axios.post('http://10.7.5.182:8000/api/addrobot', {
        name: name
    }, {
        headers: {
            "Content-Type": "application/json"
        }
    })).data.status
}

/**
 * Get all missions of one selected robot (from it's id)
 * @param {str} robot_id - The id (uuid) of the robot's missions to get
 * @returns All the missions of the robot
 */
export const getMissions = async (robot_id) => {
    return (await axios.post("http://10.7.5.182:8000/api/getmissions", { 
        robot_id 
    },
    {
        headers: {
            "Content-Type": "application/json"
        }
    })).data.missions
}

/**
 * Get all the robot from the database
 * @returns All the robots
 */
export const getRobots = async () => {
    return (await axios.get("http://10.7.5.182:8000/api/robots")).data.robots
}