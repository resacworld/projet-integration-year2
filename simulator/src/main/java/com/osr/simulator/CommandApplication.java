package com.osr.simulator;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.concurrent.TimeUnit;

public class CommandApplication extends Application {
    private static CommandController commandController;

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("command-control.fxml")); // Assuming your FXML is SimulatorView.fxml
        Parent root = loader.load();

        // Get the controller instance created by the FXMLLoader
        commandController = loader.getController();
        System.out.println(commandController);
        Scene scene = new Scene(root, 896, 504);
        stage.setTitle("Command Control");
        stage.setScene(scene);
        stage.show();
        Robot.getInstance();
        stage.setOnCloseRequest(t -> {
            Platform.exit();
            System.exit(0);
        });
    }

    /**
     * Command Controller getter
     * @return  CommandController
     */
    public static CommandController getCommandController() {
        return commandController;
    }

    /**
     * Main method
     * @param args
     */
    public static void main(String[] args){
        Thread t1 = new Thread(() -> {
            try {
                TimeUnit.SECONDS.sleep(1);
                while(true){
                    Robot.getInstance().execute();
                    TimeUnit.SECONDS.sleep(3);
                }
            } catch (IOException | InterruptedException | URISyntaxException e) {
                throw new RuntimeException(e);
            }
        });
        t1.start();
        launch();

    }
}