package com.osr.simulator;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class RESTService {
    static String json = "{\n" + "\"userId\": 101,\r\n" +
            "    \"id\": 101,\r\n" +
            "    \"title\": \"Test Title\",\r\n" +
            "    \"body\": \"Test Body\"" + "\n}";
    public static void main(String[] args) throws IOException {
        MyGETRequest();
        MyPOSTRequest(json);
    }
    public static void MyPOSTRequest(String Post) throws IOException {
        System.out.println(Post);
        URL obj = new URL("http://10.7.5.185:8000/api/telemetry");
        HttpURLConnection postConnection = (HttpURLConnection) obj.openConnection();
        postConnection.setRequestMethod("POST");
        //postConnection.setRequestProperty("userId", "a1bcdefgh");
        postConnection.setRequestProperty("Content-Type", "application/json");

        postConnection.setDoOutput(true);
        OutputStream os = postConnection.getOutputStream();
        os.write(Post.getBytes());
        os.flush();
        os.close();

        int responseCode = postConnection.getResponseCode();
        System.out.println("POST Response Code :  " + responseCode);
        System.out.println("POST Response Message : " + postConnection.getResponseMessage());

        if (responseCode == HttpURLConnection.HTTP_OK) { //success
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    postConnection.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in .readLine()) != null) {
                response.append(inputLine);
            } in .close();

            // print result
            System.out.println(response.toString());
        } else {
            System.out.println("POST NOT WORKED");
        }
    }

    public static void MyGETRequest() throws IOException {
        URL urlForGetRequest = new URL("http://10.7.5.185:8000/api/instructions");
        String readLine = null;
        HttpURLConnection conection = (HttpURLConnection) urlForGetRequest.openConnection();
        conection.setRequestMethod("GET");
        //conection.setRequestProperty("userId", "a1bcdef"); // set userId its a sample here
        int responseCode = conection.getResponseCode();


        if (responseCode == HttpURLConnection.HTTP_OK) {
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(conection.getInputStream()));
            StringBuffer response = new StringBuffer();
            while ((readLine = in .readLine()) != null) {
                response.append(readLine);
            } in .close();
            // print result
            System.out.println("JSON String Result " + response.toString());
            //GetAndPost.POSTRequest(response.toString());
        } else {
            System.out.println("GET NOT WORKED");
        }
    }
}
