package com.osr.simulator;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import static javafx.scene.paint.Color.*;

public class dictPosition {
    private static final Map<Float,Position> positions = new HashMap<Float,Position>(){{
        put(1F, new Position("p_1","Start",null,false));
        put(2F, new Position("p_2","Yellow",new Cube(YELLOW),false));
        put(3F, new Position("p_3","Red",new Cube(RED),false));
        put(4F, new Position("p_4","Stockage1",null,true));
        put(5F, new Position("p_5","Stockage1",null,true));
        put(6F, new Position("p_6","Pink",new Cube(PINK),false));
        put(7F, new Position("p_7","Blue",new Cube(BLUE),false));
        put(8F, new Position("p_8","Stockage2",null,true));
        put(9F, new Position("p_9","Stockage2",null,true));
        put(10F, new Position("p_10","Green",new Cube(GREEN),false));
        put(1.5F, new Position("p_1_2","Start_Yellow",null,false));
        put(2.5F, new Position("p_2_3","Yellow_Red",null,false));
        put(3.5F, new Position("p_3_4","Red_Stockage1",null,false));
        put(4.5F, new Position("p_4_5","Stockage1_Stockage1",null,false));
        put(5.5F, new Position("p_5_6","Stockage1_Pink",null,false));
        put(6.5F, new Position("p_6_7","Pink_Blue",null,false));
        put(7.5F, new Position("p_7_8","Blue_Stockage2",null,false));
        put(8.5F, new Position("p_8_9","Stockage2_Stockage2",null,false));
        put(9.5F, new Position("p_9_10","Stockage2_Green",null,false));
        put(10.5F, new Position("p_10_1","Green_Start",null,false));
    }} ;

    /**
     * getPosition
     * @param id
     * @return Position instance of the float id
     */
    public static Position getPosition(Float id) {
        return positions.get(id);
    }

    /**
     * get number of positions
     * @return Integer total number of positions
     */
    public static Integer getNumberOfPositions() {
        return positions.size();
    }

    //Generate

    /**
     * get all positions
     * @return Map<Float, Position> map of the positions dictionnary
     */
    public static Map<Float, Position> getAllPositions() {
        return Collections.unmodifiableMap(positions);
    }

    /**
     * get free storage positions
     * @return Map<Float, Position> map of all the positions with available storage
     */
    public static Map<Float, Position> getFreeStoragePositions() {
        Map<Float, Position> storagePositions = new HashMap<>();
        for (var entry : positions.entrySet()) {
            if(entry.getValue().isStorage()&&entry.getValue().getCube()==null){
                storagePositions.put(entry.getKey(), entry.getValue());
            }
            //System.out.println(entry.getKey() + "/" + entry.getValue());
        }
//        System.out.println("Free Storage Positions: "+storagePositions);
        return storagePositions;
    }
}
