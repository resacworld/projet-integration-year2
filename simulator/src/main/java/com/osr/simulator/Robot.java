package com.osr.simulator;

import java.io.IOException;
import java.util.*;
import java.util.concurrent.TimeUnit;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.osr.simulator.CommandController;

import static java.lang.Math.abs;


public class Robot {
    private static Robot instance = null;
    private final CommandController commandController;
    private String robotId = "001";
    private float positionRobot = 1;
    private Cube cube;

    private Robot(CommandController commandController) {
        this.commandController = commandController;
    }

    public static Robot setInstance(CommandController commandController) {
        if ( instance == null ) {
            instance = new Robot(commandController);
        }
        return instance;
    }

    public static Robot getInstance() {
        if ( instance == null ) {
            instance = new Robot(null);
        }
        return instance;
    }

    public Cube getCube() {
        return cube;
    }

    public float getPositionRobot() {
        return positionRobot;
    }

    public CommandController getCommandController() {
        return commandController;
    }

    public void execute() throws IOException, InterruptedException {
        System.out.println(RESTService.MyGETRequest(robotId));
        //System.out.println(commandController);
        List<Integer> listeInstructions = getListeBlocksFromJson(RESTService.MyGETRequest(robotId));
        TimeUnit.SECONDS.sleep(3);
        System.out.println(listeInstructions);
        for (Integer i : listeInstructions) {
            System.out.println("Going to cube position : "+ i);
            moveRobot((int) positionRobot,i,findOrientation((int) positionRobot,i));
            this.cube = dictPosition.getPosition(positionRobot).getCube();
            System.out.println("Picked up "+cube.getColor()+"cube");
            dictPosition.getPosition(positionRobot).setCube(null);
            Map<Float, Position> storagePositions = dictPosition.getFreeStoragePositions();
            int closest = findClosest((int) positionRobot,storagePositions);
            System.out.println("Going to storage position : "+ closest);
            moveRobot((int) positionRobot,closest,findOrientation((int) positionRobot,closest));
            dictPosition.getPosition(positionRobot).setCube(cube);
            System.out.println("Dropped "+cube.getColor()+"cube");
            cube = null;
//            List<Integer> distances = new ArrayList<>();
//            List<Integer> destinations = new ArrayList<>();
//            int x=0;
//            for (var storagePosition : storagePositions.entrySet()) {
//                int pos = Integer.parseInt(storagePosition.getKey());
//                destinations.set(x, pos);
//                int distance;
//                int nbPositions = dictPosition.getNumberOfPositions();
//                if(pos>0.5*nbPositions+(int)(positionRobot)){distance = nbPositions-pos+(int)(positionRobot); startOrientation=false;}
//                else {distance = abs(pos)-(int) positionRobot;startOrientation=true;}
//                distances.set(x,distance);
//                x++;
//            }
//            int destination = destinations.indexOf(Collections.min(distances));
        }
    }
    private int findClosest(int start,Map<Float, Position> positions) {
        List<Integer> listDistances = new ArrayList<>();
        List<Integer> listDestinations = new ArrayList<>();
        int x=0;
        for (var position : positions.entrySet()) {
            int pos = position.getKey().intValue();
            listDestinations.add(x, pos);
            int distance;
            int nbPositions = dictPosition.getNumberOfPositions();
            if(pos>0.5*nbPositions+start){distance = nbPositions-pos+start;}
            else {distance = abs(pos)-start;}
            listDistances.add(x,distance);
            x++;
        }
        int closest = listDistances.indexOf(Collections.min(listDistances));
        return listDestinations.get(closest);
    }
    private boolean findOrientation(int start, int end) {
        boolean startOrientation = true;
        int nbPositions = dictPosition.getNumberOfPositions();
        if(end>0.5*nbPositions+(start)){startOrientation=false;}
        return startOrientation;
    }
    private void moveRobot(int start, int end, boolean startOrientation) throws InterruptedException {
        int nbPositions = dictPosition.getNumberOfPositions();
        float e = start;
        System.out.println("Going to : "+end);
        while (e != end) {
            if (e==1&&!startOrientation){e=nbPositions;}
            else if(e==nbPositions/2+0.5&&startOrientation) {e=1;}
            else if(startOrientation){e+= 0.5F;}
            else {e-= 0.5F;}
            this.positionRobot = e;
            System.out.println("Futur Position : "+e);
            CommandController.updatePositionColor();
            TimeUnit.SECONDS.sleep(3);
        }

        //AJOUTER AFFICHAGE
    }
    //gemini
    public List<Integer> getListeBlocksFromJson(String jsonString) {
        List<Integer> listeBlocks = new ArrayList<>();
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            JsonNode rootNode = objectMapper.readTree(jsonString);

            // Check if "liste_blocks" node exists and is an array
            if (rootNode.has("liste_blocks") && rootNode.get("liste_blocks").isArray()) {
                for (JsonNode blockNode : rootNode.get("liste_blocks")) {
                    if (blockNode.isInt()) {
                        listeBlocks.add(blockNode.asInt());
                    } else {
                        System.err.println("Warning: Non-integer value found in liste_blocks: " + blockNode.asText());
                    }
                }
            } else {
                System.out.println("No 'liste_blocks' array found or it's not an array in the JSON.");
            }
        } catch (com.fasterxml.jackson.core.JsonProcessingException e) {
            System.err.println("Error parsing JSON string: " + e.getMessage());
        }
        return listeBlocks;
    }
}
