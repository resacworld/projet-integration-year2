package com.osr.simulator;

import javafx.fxml.FXML;

public class Position {
    private final String fxId;
    private final String name;
    private Cube cube;
    private boolean storage =false;

    public Position(String fxId, String name, Cube cube,Boolean storage) throws NullPointerException{

        this.fxId = fxId;
        this.name = name;
        this.cube = cube;
        this.storage = storage;
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

    public boolean isStorage() {
        return storage;
    }
    public void setStorage(boolean storage) {
        this.storage = storage;
    }

    @FXML
    public void setCube(Cube cube) {
        this.cube = cube;
    }
}

