package com.osr.simulator;

import javafx.scene.paint.Color;

public class Cube {
    private Color color;

    public Cube(Color color) {
        this.color = color;
    }

    public Color getColor() {
        if(color==null){return Color.BLACK;}
        return color;
    }
}


