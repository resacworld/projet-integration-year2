import axios from 'axios';

export const registerRobot = async (name) =>{
    return (await axios.post('http://10.7.5.182:8000/api/addrobot', {
        name: name
    }, {
        headers: {
            "Content-Type": "application/json"
        }
    })).data.status
}

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

export const getRobots = async () => {
    return (await axios.get("http://10.7.5.182:8000/api/robots")).data.robots
}