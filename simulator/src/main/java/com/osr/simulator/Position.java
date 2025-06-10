package com.osr.simulator;

import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;

public class Position {
    private final String fxId;
    private final String name;
    private Color color;

    public Position(String fxId, String name, Color color) throws NullPointerException{

        this.fxId = fxId;
        this.name = name;
        this.color = color;
    }
    public String getFxId() { // Getter for the FXML ID
        return fxId;
    }
    public String getName() {
        return name;
    }
    public Color getColor() {
        return color;
    }

    @FXML
    public void setColor(Color color) {
        this.color = color;



    }
}

