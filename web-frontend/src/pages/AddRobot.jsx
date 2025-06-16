import React, { useState } from "react";
import { registerRobot } from "../services/RESTService"

/** 
 * Page to add a robot in the web server
*/
export default ({}) => {
    const [ status, setStatus ] = useState(false)
    const [ message, setMessage ] = useState(false)

    const [ name, setName ] = useState("");

    return (
        <div className="p-3 w-1/3 bg-slate-400">
            <h2 className="block mb-2 text-md text-xl font-semibold text-gray-900 dark:text-white">Add a robot</h2>
            <div className="home px-5 pb-5">
                <div className="bg-red grid gap-6 mb-2">
                    <div>
                        <label htmlFor="name" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Robot name</label>
                        <input type="text" id="name" value={name} onChange={(e)=>setName(e.target.value)} className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="robot 1" required />
                    </div>
                </div>
                <button onClick={() => {
                    // Ask the web server to register a new robot
                    var response = registerRobot(name)
                    if(response){
                        // Set success message
                        setStatus(true)
                        setMessage("Robot ajouté avec succès")
                    }
                    else {
                        // Set error message
                        setStatus(false)
                        setMessage("Erreur lors de l'ajout")
                    }
                }} className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 mt-3 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
                <p className={`mt-6 font-semibold size-2 w-full ${status?"text-green-300":"text-red-300"}`}>{message}</p>
            </div>
        </div>
    );
}