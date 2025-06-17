import { useEffect, useState } from "react";
import { getMissions, getRobots } from "../services/RESTService";

/**
 * Missions section, to get all missions of the current selected robot
 */
export default ({}) => {
    const [ missions, setMissions ] = useState([])
    const [ robots, setRobots ] = useState([])

    const [ selectedRobotId, setSelectedRobotId ] = useState()

    useEffect(()=>{
        /**
         * Get and set in hooks all the robots get from the web server
         */
        async function request(){
            var allrobots = await getRobots()
            setRobots(allrobots)
        }
        request()
    }, [])

    useEffect(()=>{
        /**
         * Set the first robot as selected (only when the list of robot is available)
         */
        async function request(){
            if(robots[0] !== undefined){
                await setSelectedRobotId(robots[0].id)
            }
        }
        request()
    }, [robots])

    useEffect(()=>{
        /**
         * Get all the missions of the selected robot, called each time a robot is selected
         */
        async function request() {
            console.log("hello")
            setMissions(await getMissions(selectedRobotId))
            console.log(await missions)
        }
        if(selectedRobotId != undefined){
            request()
        }
    }, [selectedRobotId])

    return <div className="p-3 pr-0 bg-slate-300 min-h-screen w-2/3">
        <h2 className="block mb-2 text-xl font-semibold text-gray-900 dark:text-white">Missions</h2>
        <div>
            <form className="max-w-md mx-auto w-80">
                <label htmlFor="countries" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a robot</label>
                <select 
                    id="countries" 
                    onChange={(e)=>setSelectedRobotId(e.target.value)} 
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    {robots && robots.length!=0 && robots.map((robot, index) => {
                        return <option value={robot.id} key={robot.id}>{robot.name}</option>
                    })}
                </select>
            </form>
            
            <div className="flex flex-row flex-wrap justify-center mt-2">
                {missions && missions.map((mission, index) => {
                    return <div className="mr-6 bg-slate-400 p-2 m-1 rounded-md" key={mission.id}>
                        <h3 htmlFor="name" className="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Mission : <span className="text-gray-500">{mission.name}</span></h3>
                        
                        {mission.executing?
                        <h3 className="px-3 py-1 text-sm text-gray-900 font-medium inline-block bg-yellow-300 rounded-md">Running</h3>:(mission.finished?
                        <h3 className="px-3 py-1 text-sm text-gray-900 font-medium inline-block bg-orange-300 rounded-md">Finished</h3>:
                        <h3 className="px-3 py-1 text-sm text-gray-900 font-medium inline-block bg-green-300 rounded-md">New</h3>
                        )}

                        <div className="flex flex-row">
                            {mission.blocks.map((block, index) => {
                                return <div key={block.id + index}>
                                    <h3 htmlFor="name" className="block m-1 mt-2 py-3 px-6 text-sm font-xl content-center bg-gray-200 rounded-md text-gray-900">{block.block_nb}</h3>
                                </div>
                            })}
                        </div>
                    </div>
                })}
                {(missions == undefined || missions.length==0)?"Aucune mission enregistrée":null}
            </div>
        </div>
    </div>
}