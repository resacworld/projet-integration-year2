import React, { useActionState, useEffect, useState } from "react";
import { getMissions, getRobots } from "../services/RESTService";

export default ({}) => {
    const [ missions, setMissions ] = useState([])
    const [ robots, setRobots ] = useState([])

    const [ selectedRobotMac, setSelectedRobotMac ] = useState()

    useEffect(()=>{
        async function request(){
            var allrobots = await getRobots()
            setRobots(allrobots)
        }
        request()
    }, [])

    useEffect(()=>{
        async function request(){
            if(robots[0] !== undefined){
                await setSelectedRobotMac(robots[0].id)
            }
        }
        request()
    }, [robots])

    useEffect(()=>{
        async function request() {
            setMissions(await getMissions(selectedRobotMac))
        }
        if(selectedRobotMac != undefined){
            request()
        }
    }, [selectedRobotMac])

    return <div className="p-3 pr-0 bg-slate-300 min-h-screen w-2/3">
        <label htmlFor="name" className="block mb-2 text-md font-medium text-gray-900 dark:text-white">Missions</label>
        <div>
            <form className="max-w-md mx-auto w-80">
                <label htmlFor="countries" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a robot</label>
                <select 
                    id="countries" 
                    onChange={(e)=>setSelectedRobotMac(e.target.value)} 
                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    {robots && robots.length!=0 && robots.map((robot, index) => {
                        return <option value={robot.id} key={robot.id}>{robot.name}</option>
                    })}
                </select>
            </form>
            
            <div className="flex flex-row flex-wrap justify-center">
                {missions.map((mission, index) => {
                    return <div className="mr-6 bg-slate-400 p-2 m-1 rounded-md" key={mission.id}>
                        <h3 htmlFor="name" className="block mb-1 text-sm font-medium text-gray-900 dark:text-white">Mission : <span className="text-gray-500">{mission.name}</span></h3>
                        
                        <div className="flex flex-row">
                            {mission.blocks.map((block, index) => {
                                return <div key={block.id + index}>
                                    <h3 htmlFor="name" className="block m-1 py-3 px-6 text-sm font-xl content-center bg-gray-200 rounded-md text-gray-900">{block.block_nb}</h3>
                                </div>
                            })}
                        </div>
                    </div>
                })}
            </div>
        </div>
    </div>
}