module com.osr.simulator {
    requires javafx.controls;
    requires javafx.fxml;

    requires com.almasb.fxgl.all;
    requires com.fasterxml.jackson.databind;

    opens com.osr.simulator to javafx.fxml;
    exports com.osr.simulator;
}