package com.osr.simulator;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import static javafx.scene.paint.Color.*;

public class dictPosition {
    private static final Map<String,Position> positions = new HashMap<String,Position>(){{
        put("1", new Position("p_1","Start",null));
        put("2", new Position("p_2","Yellow",new Cube(YELLOW)));
        put("3", new Position("p_3","Red",new Cube(RED)));
        put("4", new Position("p_4","Stockage1",null));
        put("5", new Position("p_5","Stockage1",null));
        put("6", new Position("p_6","Pink",new Cube(PINK)));
        put("7", new Position("p_7","Blue",new Cube(BLUE)));
        put("8", new Position("p_8","Stockage2",null));
        put("9", new Position("p_9","Stockage2",null));
        put("10", new Position("p_10","Green",new Cube(GREEN)));
        put("1.5", new Position("p_1_2","Start_Yellow",null));
        put("2.5", new Position("p_2_3","Yellow_Red",null));
        put("3.5", new Position("p_3_4","Red_Stockage1",null));
        put("4.5", new Position("p_4_5","Stockage1_Stockage1",null));
        put("5.5", new Position("p_5_6","Stockage1_Pink",null));
        put("6.5", new Position("p_6_7","Pink_Blue",null));
        put("7.5", new Position("p_7_8","Blue_Stockage2",null));
        put("8.5", new Position("p_8_9","Stockage2_Stockage2",null));
        put("9.5", new Position("p_9_10","Stockage2_Green",null));
        put("10.5", new Position("p_10_1","Green_Start",null));


    }} ;
    public static Position getPosition(String id) {
        return positions.get(id);
    }

    //Generate
    public static Map<String, Position> getAllPositions() {
        return Collections.unmodifiableMap(positions);
    }
}
