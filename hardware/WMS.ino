/**
 * @file WMS.ino
 * @author precio 
 * @brief 
 * @version 0.1
 * @date 2023-03-05
 * 
 * @copyright Copyright (c) 2023
 * 
 */

/*================================================================
Pinouts:

1. Dallas: GPIO 2
2. BH1750:I2C
3. MS5611:I2C
4. SHT25: I2C
5. Voltage: 32
6. Rain sensor: 34,35
7. 
==================================================================*/

/*=========================================================================================================

Check lists of each programs and sensors:
1. Dallas                                                                * Done
2. SHT25                                                                 * Done
3. ML8511                                                                *
4. VEML7700                                                              *
5. VEML6500                                                              *
6. MS5611                                                                * Done
7. BH1750                                                                * Done
8. Rain sensor                                                           * Done
9. Bluetooth connect for communication and trouble shoot                 *
10. OTA                                                                  *
11. SIM800                                                               *
12. Voltage monitoring                                                   * Done
13. Time series weather prediction                                       *
14. php script                                                           * CANCELLED
15. PIR intrusion detection                                              * CANCELLED
16. Deep sleep with battery power down sequence                          *
17. NRF24 communication-receiver and transmitter with code update        *
18. Webpage                                                              * Done
19. Time function with standard time turn on feature                     *
20. Interupt pin                                                         *
21. GPIO control                                                         *
22. SD card backup data                                                  *
23. Notification and troubleshoot section                                *
==========================================================================================================*/


#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <BH1750.h>
#include <SHT25.h>
#include <MS5611.h>



// Replace with your network credentials
const char* ssid     = "xxxxxxxxxxx";
const char* password = "***********";

// REPLACE with your api key and URL path or IP address with path
const char* serverName = "http://127.0.0.1:8000/api/update/{api_token}";

// Keep this API Key value to be compatible with the PHP code provided in the project page. 
// If you change the apiKeyValue value, the PHP file /post-esp-data.php also needs to have the same key 
String apiKeyValue = "tPmAT5Ab3j7F9";

String sensorName = "AWS_v04";
String sensorLocation = "Home";

// Input values for MySQL
float Humidity_S, Pressure, UV, Intensity;
float Temperature_S,Temperature_M,Temperature_D,Temperature_A;
String Notification,Nrf;
int RainSensorD,RainSensorA,Adc,Volt;


// Dallas temperature sensor
const int oneWireBus = 0;
float Dtemp;  
OneWire oneWire(oneWireBus);
DallasTemperature DallasProbe(&oneWire);

//BH1750
float lux;
BH1750 lightMeter;

//SHT25
SHT25 SHT;
float SHTtemp,SHThumi;

//ML8511

//MS5611
MS5611 MS5611(0x77);
float MS5611pres, MS5611temp;

//Rain Sensor
const int rainAnalog = 35;
const int rainDigital=34;
int rainAnalogVal;
int rainDigitalVal;

//Voltage Sensor
const int Analog_pin= 32;
int ADC_VALUE = 0;
int Voltage_value = 0; 

void Dallas(){
  DallasProbe.requestTemperatures(); 
  Dtemp = DallasProbe.getTempCByIndex(0);
}

void RainSensor(){
  rainAnalogVal = analogRead(rainAnalog);
  rainDigitalVal = digitalRead(rainDigital);
}

void SHT_SENS(){
  SHTtemp=SHT.getTemperature();
  SHThumi=SHT.getHumidity();
}

void Lux(){
  lux = lightMeter.readLightLevel(true);
  if (lux > 40000.0) {
      lightMeter.setMTreg(32);
    }
  else if (lux > 10.0) {
      lightMeter.setMTreg(69);
    }
  else if (lux <= 10.0) {
      lightMeter.setMTreg(138);
    }
}  

void Voltage(){
ADC_VALUE = analogRead(Analog_pin);
Voltage_value = (ADC_VALUE * 3.3 ) / (4095);
}

void MS5611_P(){
  MS5611.setOversampling(OSR_ULTRA_HIGH);
  MS5611.read();
  MS5611temp = MS5611.getTemperature();
  MS5611pres = MS5611.getPressure();  
}


void Sensor_data_read(){
  Voltage();
  delay(1000);
  Lux();
  delay(1000);
  SHT_SENS();
  delay(1000);
  Dallas();
  delay(1000);
  RainSensor();
  delay(1000);
  MS5611_P();
  delay(1000);
  Serial.println("ADC Value: ");
  Serial.println(ADC_VALUE);
  Serial.println("Voltage Value: ");
  Serial.println(Voltage_value);
  Serial.println("Light Intensity: ");
  Serial.println(lux);
  Serial.println("Temperature Value -");
  Serial.println("SHT Temperature: ");
  Serial.println(SHTtemp);
  Serial.println("DallasProbe Temperature: ");
  Serial.println(Dtemp);
  Serial.println("MS5611 Temperature: ");
  Serial.println(MS5611temp);
  Serial.println("Humidity: ");
  Serial.println(SHThumi);
  Serial.println("Pressure: ");
  Serial.println(MS5611pres);
  Serial.println("Rain analogue: ");
  Serial.println(rainAnalogVal);
  Serial.println("Rain digital: ");
  Serial.println(rainDigitalVal);  
  Serial.println("\n");

 Temperature_S= SHTtemp;
 Temperature_A=0;
 Temperature_M=MS5611temp;
 Temperature_D=Dtemp;
 Humidity_S=SHThumi;
 Pressure=MS5611pres;
 UV=0;
 Intensity=(int)lux;
 RainSensorD=rainDigitalVal;
 RainSensorA=rainAnalogVal;
 Adc=ADC_VALUE;
 Volt=Voltage_value;
 Notification="Weather station working fine";
 Nrf="Inactive";

}

void mySQL_dataUpdate() {
  
  if(WiFi.status()== WL_CONNECTED){
    WiFiClient client;
    HTTPClient http;
    
    http.begin(client, serverName);    
    http.setTimeout(30000);
    http.addHeader("Content-Type", "application/json");

    StaticJsonDocument<500> doc;   
    doc["apiKeyValue"]=apiKeyValue;
    doc["deviceName"]=sensorName;
    doc["location"]=sensorLocation;
    doc["temperature_s"]=Temperature_S;
    doc["temperature_d"]=Temperature_D;
    doc["temperature_a"]=Temperature_A;
    doc["temperature_m"]=Temperature_M;
    doc["nrf"]=Nrf;
    doc["notifc"]=Notification;
    doc["adc"]=Adc;
    doc["voltage"]=Volt;
    doc["humidity"]=Humidity_S;
    doc["pressure"]=Pressure;
    doc["uv_index"]=UV;
    doc["light_lux"]=Intensity;
    doc["rainAnalog"]=RainSensorA;
    doc["rainDigital"]=RainSensorD;

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
  Wire.begin();
  DallasProbe.begin();
  SHT.begin();
  MS5611.begin();
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(rainAnalog,INPUT);
  pinMode(rainDigital,INPUT);
  lightMeter.begin(BH1750::ONE_TIME_HIGH_RES_MODE);
}
void loop(){
  digitalWrite(LED_BUILTIN, HIGH);
  Sensor_data_read();
  delay(500); 
  mySQL_dataUpdate();
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000*60*15);
}