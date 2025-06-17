package com.osr.simulator;

import javafx.scene.paint.Color;

public class Cube {
    private final Color color;

    /**
     * Cube constructor
     * @param color javafx.scene.paint.Color    color of the cube
     */
    public Cube(Color color) {
        this.color = color;
    }

    /**
     * Color getter
     * @return javafx.scene.paint.Color color of the cube
     */
    public Color getColor() {
        if(color==null){return Color.BLACK;}
        return color;
    }
}


