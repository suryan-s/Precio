/**
 * @file PMS.ino
 * @author precio 
 * @brief 
 * @version 0.1
 * @date 2023-03-05
 * 
 * @copyright Copyright (c) 2023
 * 
 */

/*================================================================
Pinouts: ESP8266

1. Capacitative moisture sensor: A0 
==================================================================*/
===================================================================================
*/

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>



// Replace with your network credentials
const char* ssid     = "xxxxxxxxxxxx";
const char* password = "************";


// REPLACE with your api key and URL path or IP address with path
const char* serverName = "http://127.0.0.1:8000/api/update/{api_token}";

// Keep this API Key value to be compatible with the PHP code provided in the project page. 
// If you change the apiKeyValue value, the PHP file /post-esp-data.php also needs to have the same key 
String apiKeyValue = "tPmAT5Ab3j7F10";

String sensorName = "PMS01";
String sensorLocation = "Home";

#define SensorPin A0 

// Input values for server
int MOISTURE_Value;


void Sensor_data_read(){
  MOISTURE_Value=analogRead(SensorPin);
  Serial.println(MOISTURE_Value);
  delay(1000);
}

void mySQL_dataUpdate() {
  
  if(WiFi.status()== WL_CONNECTED){
    WiFiClient client;
    HTTPClient http;
    
    http.begin(client, serverName);    
    http.setTimeout(30000);
    http.addHeader("Content-Type", "application/json");

    StaticJsonDocument<200> doc;   
    doc["apiKeyValue"]=apiKeyValue;
    doc["deviceName"]=sensorName;
    doc["location"]=sensorLocation;
    doc["moisture"]=MOISTURE_Value;

    String httpRequestData;
    serializeJson(doc, httpRequestData);
    Serial.println(httpRequestData);    
    
  
    int httpResponseCode = http.POST(httpRequestData);    
    if (httpResponseCode>0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    }
    else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
    // Free resources
    http.end();
  }
  else {
    Serial.println("WiFi Disconnected");
  }
  
}

void setup(){
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  delay(1000);
  digitalWrite(LED_BUILTIN, HIGH);   
  delay(250);                       
  digitalWrite(LED_BUILTIN, LOW);   
  delay(250);   
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) { 
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}
void loop(){
  digitalWrite(LED_BUILTIN, HIGH);
  Sensor_data_read();
  delay(500); 
  mySQL_dataUpdate();
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000*60*15);
}