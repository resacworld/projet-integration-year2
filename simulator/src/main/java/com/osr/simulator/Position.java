package com.osr.simulator;

import javafx.fxml.FXML;

public class Position {
    private final String fxId;
    private final String name;
    private Cube cube;
    private boolean storage =false;

    /**
     * Positions constructor
     * @param fxId  for example, "p_1"
     * @param name  distinct name
     * @param cube  Cube if needed else null
     * @param storage   true if it's a storage position
     * @throws NullPointerException
     */
    public Position(String fxId, String name, Cube cube,Boolean storage) throws NullPointerException{

        this.fxId = fxId;
        this.name = name;
        this.cube = cube;
        this.storage = storage;
    }

    /**
     * FxId getter
     * @return String fxId
     */
    public String getFxId() { // Getter for the FXML ID
        return fxId;
    }

    /**
     * Name getter
     * @return String
     */
    public String getName() {
        return name;
    }

    /**
     * Cube getter
     * @return Cube
     */
    public Cube getCube() {
        return cube;
    }

    /**
     * is Storage
     * @return boolean
     */
    public boolean isStorage() {
        return storage;
    }

    /**
     * Cube setter
     * @param cube
     */
    @FXML
    public void setCube(Cube cube) {
        this.cube = cube;
    }
}

