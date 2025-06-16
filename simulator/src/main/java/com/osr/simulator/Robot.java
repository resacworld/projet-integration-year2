package com.osr.simulator;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.*;
import java.util.concurrent.TimeUnit;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.osr.simulator.CommandController;

import static java.lang.Math.abs;
import static java.lang.Math.random;


public class Robot {
    private static Robot instance = null;
    private final CommandController commandController;
    private float positionRobot = 1;
    private Cube cube;
    private final String uuid = "efe16b56-45fa-47a3-8f05-04200828eea9";

    /**
     * Constructor of Robot Singleton
     * @param commandController
     */
    private Robot(CommandController commandController) {
        this.commandController = commandController;
    }

    /**
     * Create singleton instance to set a commandController
     * @param commandController
     * @return Robot instance
     */
    public static Robot setInstance(CommandController commandController) {
        if ( instance == null ) {
            instance = new Robot(commandController);
        }
        return instance;
    }

    /**
     * Singleton instance getter
     * @return Robot instance
     */
    public static Robot getInstance() {
        if ( instance == null ) {
            instance = new Robot(null);
        }
        return instance;
    }

    /**
     * Cube getter
     * @return Cube
     */
    public Cube getCube() {
        return cube;
    }

    public String getUuid() {
        return uuid;
    }

    /**
     * Position getter
     * @return float position of the robot
     */
    public float getPositionRobot() {
        return positionRobot;
    }

    public CommandController getCommandController() {
        return commandController;
    }

    /**
     * Execution of a the instruction list given by the server
     * @throws IOException
     * @throws InterruptedException
     */
    public void execute() throws IOException, InterruptedException, URISyntaxException {
        String executeJson = RESTService.MyGETRequest(uuid);
        System.out.println(executeJson);
        //System.out.println(commandController);
        List<Integer> listeInstructions = getListeBlocksFromJson(executeJson);
        //List<Integer> listeInstructions = getListeBlocksFromJson("{\"status\":true,\"liste_blocks\":[2,6,10]}");
        TimeUnit.SECONDS.sleep(3);
        System.out.println(listeInstructions);
        for (Integer i : listeInstructions) {
            System.out.println("Going to cube position : "+ i);
            moveRobot((int) positionRobot,i,findOrientation((int) positionRobot,i));

            this.cube = dictPosition.getPosition(positionRobot).getCube();
            postTelemetry(0,"Ramasse cube"+cube.getColor(),(int) positionRobot);
            System.out.println("Picked up "+cube.getColor()+"cube");
            dictPosition.getPosition(positionRobot).setCube(null);

            Map<Float, Position> storagePositions = dictPosition.getFreeStoragePositions();
            if (storagePositions.isEmpty()){System.out.println("No storage space");break;}
            int closest = findClosest((int) positionRobot,storagePositions);
            System.out.println("Going to storage position : "+ closest);
            //System.out.println(findOrientation((int) positionRobot,closest));
            moveRobot((int) positionRobot,closest,findOrientation((int) positionRobot,closest));

            dictPosition.getPosition(positionRobot).setCube(cube);
            postTelemetry(0,"Dépose cube"+cube.getColor(),(int) positionRobot);
            System.out.println("Dropped "+cube.getColor()+"cube");
            cube = null;
        }
        RESTService.MyPOSTRequest("{\"robot_id\":\""+uuid+"\"}","summary");
    }



    /**
     * Find the closest position in a list of positions
     * @param start
     * @param positions
     * @return int
     */
    private int findClosest(int start,Map<Float, Position> positions) {
        List<Integer> listDistances = new ArrayList<>();
        List<Integer> listDestinations = new ArrayList<>();
        int x=0;
        for (var position : positions.entrySet()) {
            int pos = position.getKey().intValue();
            listDestinations.add(x, pos);
            int distance;
            int nbPositions = (int) (dictPosition.getNumberOfPositions()*0.5);
            if(pos>nbPositions+start){distance = nbPositions-pos+start;}
            else {distance = abs(pos-start);}
            listDistances.add(x,distance);
            x++;
        }
        int closest = listDistances.indexOf(Collections.min(listDistances));
        return listDestinations.get(closest);
    }

    /**
     * Find the best orientation to go to a destination
     * @param start
     * @param end
     * @return boolean
     */
    private boolean findOrientation(int start, int end) {
        boolean startOrientation;
        int nbPositions = dictPosition.getNumberOfPositions();
        if (end<start) {
            if(end<0.25*nbPositions+(start)){startOrientation=false;}else{startOrientation=true;}
        }else {
            if(end>0.25*nbPositions+(start)){startOrientation=false;}else{startOrientation=true;}
        }

        System.out.println("start Orientation : "+startOrientation);
        return startOrientation;
    }

    /**
     * Move the position of the robot to simulate motion
     * @param start int start position
     * @param end   int end position
     * @param startOrientation  boolean way to go
     * @throws InterruptedException
     */
    private void moveRobot(int start, int end, boolean startOrientation) throws InterruptedException, IOException, URISyntaxException {
        int nbPositions = dictPosition.getNumberOfPositions();
        float e = start;
        System.out.println("Going to : "+end);
        while (e != end) {
            if (e==1&&!startOrientation){e= (float) (nbPositions/2+0.5);}
            else if(e==nbPositions/2+0.5&&startOrientation) {e=1;}
            else if(startOrientation){e+= 0.5F;}
            else {e-= 0.5F;}
            this.positionRobot = e;
            System.out.println("Futur Position : "+e);
            CommandController.updatePositionColor();
            postTelemetry(randomFloat(20,60),"Se déplace vers "+end,(int) e);
            TimeUnit.SECONDS.sleep(3);
        }
    }

    private float randomFloat(int min, int max) {
        Random random = new Random();
        min *= 100;
        max *= 100;
        float randomNumber = min + random.nextInt(max - min + 1);
        randomNumber/=100;
        return randomNumber;
    }

    /**
     * Get list from our json standard for command
     * @param jsonString string json to find list in
     * @return List<Integer> list of position to go to
     */
    //gemini
    public List<Integer> getListeBlocksFromJson(String jsonString) {
        List<Integer> listeBlocks = new ArrayList<>();
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            JsonNode rootNode = objectMapper.readTree(jsonString);
            if (rootNode.has("error")){RESTService.MyPOSTRequest("{\"robot_id\":\""+uuid+"\"}","summary");}

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
        } catch (IOException | URISyntaxException e) {
            throw new RuntimeException(e);
        }
        return listeBlocks;
    }

    public String convertMapToJson(Map<String, Object> dataMap) {
        // ObjectMapper is thread-safe and can be reused, but for simplicity in this example,
        // we'll create a new instance each time. In a larger application, consider
        // making it a singleton or a class member.
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            // writeValueAsString converts the Java object (your Map) into a JSON string.
            return objectMapper.writeValueAsString(dataMap);
        } catch (JsonProcessingException e) {
            System.err.println("Error converting map to JSON: " + e.getMessage());
            return null; // Return null or throw a custom exception based on your error handling strategy
        }
    }

    private void postTelemetry(float vitesse,String statut_deplacement,int ligne) throws IOException, URISyntaxException {
        float distance_ultrasons;
        if(cube==null){distance_ultrasons=randomFloat(19,21);}else{distance_ultrasons=randomFloat(14,18);}
        Map<String,Object> jsonTelemetry = new HashMap<String,Object>(){{
            put("vitesse",vitesse);
            put("distance_ultrasons",distance_ultrasons);
            put("statut_deplacement",statut_deplacement);
            put("ligne",ligne);
            put("status_pince", cube==null);
            put("robot_id",uuid);
        }};

        RESTService.MyPOSTRequest(convertMapToJson(jsonTelemetry),"telemetry");
    }
}
