package com.osr.simulator;

import javafx.fxml.FXML;

public class Position {
    private final String fxId;
    private final String name;
    private Cube cube;

    public Position(String fxId, String name, Cube cube) throws NullPointerException{

        this.fxId = fxId;
        this.name = name;
        this.cube = cube;
    }
    public String getFxId() { // Getter for the FXML ID
        return fxId;
    }
    public String getName() {
        return name;
    }

    public Cube getCube() {
        return cube;
    }

    @FXML
    public void setCube(Cube cube) {
        this.cube = cube;
    }
}

