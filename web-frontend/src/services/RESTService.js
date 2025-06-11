import axios from 'axios';

export const registerRobot = async (name, mac) =>{
    response = await axios.post('http://10.7.5.182:8000/api/addrobot', {
        name: name,
        mac: mac
    }, {
        headers: {
            "Content-Type": "application/json"
        }
    })

    return response.data.status;
} 