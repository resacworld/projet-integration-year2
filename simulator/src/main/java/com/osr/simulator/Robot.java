package com.osr.simulator;

import java.util.Vector;

public class Robot {
    private static Robot instance = null;
    private Float[] position = new Float[2];

    private Robot() {
    }

    public static Robot getInstance() {
        if ( instance == null ) {
            instance = new Robot();
        }
        return instance;
    }
}
