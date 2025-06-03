package com.osr.simulator;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.stage.Stage;

import java.io.IOException;

public class CommandController {
    @FXML
    private Label consoleTest;
    private String consoleTestText ;

    public void setConsoleTestText(String consoleTestText) {
        this.consoleTestText = consoleTestText;
    }

    @FXML
    //protected void onHelloButtonClick() {welcomeText.setText("Welcome to JavaFX Application!");}
    protected void pressedTestButton() throws IOException {
        consoleTestText = RESTService.MyGETRequest();
        consoleTest.setText(consoleTestText);}
}