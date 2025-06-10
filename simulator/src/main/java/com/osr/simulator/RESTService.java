package com.osr.simulator;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.UnknownHostException;

public class RESTService {
    static String json = "{\n" + "\"userId\": 101,\r\n" +
            "    \"id\": 101,\r\n" +
            "    \"title\": \"Test Title\",\r\n" +
            "    \"body\": \"Test Body\"" + "\n}";
    static String server = "http://10.7.5.182:8000/api/";
    public static void main(String[] args) throws IOException {
        //MyGETRequest();
        //MyPOSTRequest(json);
    }
    public static void MyPOSTRequest(String Post) throws IOException {
        System.out.println(Post);
        StringBuilder url = new StringBuilder(server);
        url.append("instructions");
        url.append("?robot_id=");
        URL obj = new URL(url.toString());
        if (!testConnection(url.toString())) {return;}
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
            System.out.println("POST FAILED");
        }
    }

    public static String MyGETRequest(String parameter) throws IOException {
        StringBuilder url = new StringBuilder(server);
        url.append("instructions");
        url.append("?robot_id=");
        url.append(parameter);
        URL urlForGetRequest = new URL(url.toString());
        System.out.println(url);
        String readLine = null;
        if (!testConnection(url.toString())) {return ("Connection failed");}
        HttpURLConnection conection = (HttpURLConnection) urlForGetRequest.openConnection();
        conection.setRequestMethod("GET");
        //conection.setRequestProperty("userId", "a1bcdef"); // set userId its a sample here
        int responseCode = conection.getResponseCode();


        if (responseCode == HttpURLConnection.HTTP_OK) {
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(conection.getInputStream()));
            StringBuffer response = new StringBuffer();
            while ((readLine = in.readLine()) != null) {
                response.append(readLine);
            }
            in.close();
            // print result
            return (response.toString());
            //GetAndPost.POSTRequest(response.toString());
        } else {
            return ("GET FAILED");
        }


    }

    //Gemini
    public static boolean testConnection(String url) {
        HttpURLConnection connection = null;
        try {
            // Define the URL to test the connection against.
            // Using the same URL as MyGETRequest for consistency.
            URL urlToTest = new URL(url);

            // Open a connection. This operation itself can throw exceptions
            // if the host is unreachable or the URL is malformed.
            connection = (HttpURLConnection) urlToTest.openConnection();

            // Set a short timeout for connecting to avoid long waits.
            connection.setConnectTimeout(1000); // 5 seconds
            connection.setReadTimeout(1000);    // 5 seconds

            // Attempt to connect. The getResponseCode() call will
            // implicitly connect if not already connected.
            connection.connect();

            // If we reach here, it means a connection was established.
            // We can optionally check the response code, but for just testing
            // connection, simply reaching here is often enough.
            // int responseCode = connection.getResponseCode();
            // return true; // Or return (responseCode >= 200 && responseCode < 400); if you want to check for successful HTTP status

            System.out.println("Connection to " + urlToTest + " successful.");
            return true;

        } catch (UnknownHostException e) {
            // This exception occurs if the host name cannot be resolved,
            // implying no network connection or incorrect host.
            System.err.println("Connection test failed: Unknown host or no network. " + e.getMessage());
            return false;
        } catch (IOException e) {
            // This catches other I/O errors like connection refused, timeouts, etc.
            System.err.println("Connection test failed: I/O error. " + e.getMessage());
            return false;
        } finally {
            // Ensure the connection is disconnected to release resources.
            if (connection != null) {
                connection.disconnect();
            }
        }
    }
}
