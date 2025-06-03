package com.osr.simulator;

import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class HelloController {
    @FXML
    private Label consoleTest;

    @FXML
    //protected void onHelloButtonClick() {welcomeText.setText("Welcome to JavaFX Application!");}
    protected void pressedTestButton() {
        consoleTest.setText("Welcome to JavaFX Application!");}
}