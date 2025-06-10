package com.osr.simulator;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class CommandApplication extends Application {
    private static CommandController commandController;

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(CommandApplication.class.getResource("command-control.fxml"));
        commandController = fxmlLoader.getController();
        Scene scene = new Scene(fxmlLoader.load(), 896, 504);
        stage.setTitle("Command Control");
        stage.setScene(scene);
        stage.show();
        Robot.setInstance(commandController);
    }

    public static CommandController getCommandController() {
        return commandController;
    }

    public static void main(String[] args) throws IOException {
        launch();
        Robot.getInstance().execute();
    }
}