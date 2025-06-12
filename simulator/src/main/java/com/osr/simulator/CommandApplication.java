package com.osr.simulator;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class CommandApplication extends Application {
    private static CommandController commandController;

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("command-control.fxml")); // Assuming your FXML is SimulatorView.fxml
        Parent root = loader.load();

        // Get the controller instance created by the FXMLLoader
        commandController = loader.getController();
        Scene scene = new Scene(root, 896, 504);
        stage.setTitle("Command Control");
        stage.setScene(scene);
        stage.show();
        Robot.setInstance(commandController);
    }

    public static CommandController getCommandController() {
        return commandController;
    }

    public static void main(String[] args) throws IOException {
        Thread t1 = new Thread(() -> {
            try {
                Robot.getInstance().execute();
            } catch (IOException | InterruptedException e) {
                throw new RuntimeException(e);
            }
        });
        t1.start();
        launch();

    }
}