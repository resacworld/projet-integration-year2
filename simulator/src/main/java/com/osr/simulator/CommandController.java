package com.osr.simulator;

import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import static javafx.scene.paint.Color.*;

public class CommandController{
    @FXML
    private Pane map_pane;
    private static Map<String, Circle> uiCircles = new HashMap<>();
//    @FXML
//    private Label consoleTest;
//    private String consoleTestText ;

    /**
     * Initialize the circles depending on dictPositionFxId
     */
    @FXML
    public void initialize() {
        // After map_pane is injected, we can now safely lookup circles.
        // Iterate through all the Position data objects from dictPosition
        for (Position pos : dictPosition.getAllPositions().values())
        {
            // Find the corresponding Circle UI element in the FXML
            Node foundNode = map_pane.lookup("#" + pos.getFxId()); // Use pos.getFxId() here!

            if (foundNode instanceof Circle circle) {
                //circle.setFill(pos.getCube().getColor());
                uiCircles.put(pos.getFxId(), circle); // Store the UI reference
                System.out.println("Initialized Circle '" + pos.getFxId()); //+ "' with color " + pos.getCube().getColor());
            } else {
                System.err.println("Error: Circle with fx:id='" + pos.getFxId() + "' not found in FXML or is not a Circle.");
            }
        }
        updatePositionColor();
    }

//    public void updatePositionColor(String positionId, Color newColor) {
//        Position dataPosition = dictPosition.getPosition(positionId);
//        if (dataPosition != null) {
//            dataPosition.setColor(newColor);
//            System.out.println("Data for Position " + dataPosition.getName() + " updated to " + newColor);
//
//            // 2. Update the UI component
//            Circle uiCircle = uiCircles.get(dataPosition.getFxId()); // Get UI circle using its FXML ID
//            if (uiCircle != null) {
//                uiCircle.setFill(newColor);
//                System.out.println("UI for Circle " + dataPosition.getFxId() + " updated to " + newColor);
//            } else {
//                System.err.println("Warning: UI Circle for fx:id '" + dataPosition.getFxId() + "' not found in map.");
//            }
//        } else {
//            System.err.println("Error: Position with ID '" + positionId + "' not found in dictPosition.");
//        }
//    }

    /**
     * Update the circles colors
     */
    public static void updatePositionColor() {
        dictPosition.getAllPositions().values().forEach(pos -> {
            Circle uiCircle = uiCircles.get(pos.getFxId());
            uiCircle.setStroke(BLACK);
            if (pos.getCube()==null&&uiCircle!=null) {
                    uiCircle.setFill(BLACK);
            } else if (uiCircle!=null) {
            uiCircle.setFill(pos.getCube().getColor());
            }
        });

        float robotPose =Robot.getInstance().getPositionRobot();
//        String robotPoseString;
//        if (robotPose%1==0){
//            robotPoseString = (int) robotPose+"";
//        }else{robotPoseString = robotPose+"";}
        System.out.println("robot pose : "+robotPose);
        //System.out.println(uiCircles.values());
        uiCircles.get(dictPosition.getPosition(robotPose).getFxId())
                .setStroke(GRAY);
        if(Robot.getInstance().getCube()!=null){
            uiCircles.get(dictPosition.getPosition(robotPose).getFxId())
                    .setFill(Robot.getInstance().getCube().getColor());
        }

    }

//    public void setConsoleTestText(String consoleTestText) {
//        this.consoleTestText = consoleTestText;
//    }
//
//    @FXML
//    //protected void onHelloButtonClick() {welcomeText.setText("Welcome to JavaFX Application!");}
//    protected void pressedTestButton() throws IOException {
//        //consoleTestText = RESTService.MyGETRequest();
//        //consoleTest.setText(consoleTestText);
//        //updatePositionColor("1",RED);
//    }

}