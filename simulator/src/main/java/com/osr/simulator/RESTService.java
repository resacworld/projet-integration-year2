package com.osr.simulator;

import java.io.*;
import java.net.*;

public class RESTService {
    static String serverStart = "http://";
    static String serverEnd = ":8000/";
    //static String server = "http://10.7.5.42:8000/";

    /**
     * POST request method
     * @param Post  String : message to post (usually json)
     * @param route String : route to reach
     * @throws IOException
     * @throws URISyntaxException
     */
    public static void MyPOSTRequest(String Post,String route) throws IOException, URISyntaxException {
        System.out.println(Post);
        StringBuilder url = new StringBuilder(serverStart+CommandApplication.getCommandController().getIPTextField()+serverEnd);
        url.append(route);
        //url.append("?robot_id=");
        //url.append(uuid);
        URL obj = new URI(url.toString()).toURL();
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
            StringBuilder response = new StringBuilder();

            while ((inputLine = in .readLine()) != null) {
                response.append(inputLine);
            } in .close();

            // print result
            System.out.println(response);
        } else {
            System.out.println("POST FAILED");
        }
    }

    /**
     * GET request method
     * @param uuid  String : uuid of the robot
     * @return  String : json of the instructions
     * @throws IOException
     * @throws URISyntaxException
     */
    public static String MyGETRequest(String uuid) throws IOException, URISyntaxException {
        StringBuilder url = new StringBuilder(serverStart+CommandApplication.getCommandController().getIPTextField()+serverEnd);
        url.append("instructions");
        url.append("?robot_id=");
        url.append(uuid);
        URL urlForGetRequest = new URI(url.toString()).toURL();
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
            StringBuilder response = new StringBuilder();
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
    /**
     * Test the server connection
     * @param url   String : URL of the server
     * @return  boolean : true if connection exist
     */
    public static boolean testConnection(String url) {
        HttpURLConnection connection = null;
        System.out.println(url);
        try {
            // Define the URL to test the connection against.
            // Using the same URL as MyGETRequest for consistency.
            URL urlToTest = new URI(url).toURL();

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
        } catch (URISyntaxException e) {
            throw new RuntimeException(e);
        } finally {
            // Ensure the connection is disconnected to release resources.
            if (connection != null) {
                connection.disconnect();
            }
        }
    }
}
