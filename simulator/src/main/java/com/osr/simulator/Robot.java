package com.osr.simulator;

import java.io.IOException;
import java.util.Vector;


public class Robot {
    private static Robot instance = null;
    private final CommandController commandController;
    private String robotId = "001";

    private Robot(CommandController commandController) {
        this.commandController = commandController;
    }

    public static Robot setInstance(CommandController commandController) {
        if ( instance == null ) {
            instance = new Robot(commandController);
        }
        return instance;
    }

    public static Robot getInstance() {
        if ( instance == null ) {
            instance = new Robot(null);
        }
        return instance;
    }

    public CommandController getCommandController() {
        return commandController;
    }

    public void execute() throws IOException {
        System.out.println(RESTService.MyGETRequest(robotId));


    }
}
