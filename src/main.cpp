#include <Arduino.h>

int x;
int ledPin = 2;
boolean ledOn = false;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(ledPin, OUTPUT);
}

void  loop() {
  while (!Serial.available()){
    if(ledOn == true){
        digitalWrite(ledPin, HIGH);
    } else if (ledOn == false){
      digitalWrite(ledPin, LOW);
    }
  }
  x = Serial.readString().toInt();
  Serial.print(x);
  if(x == 23){
    ledOn = true;
  }else{
    ledOn = false;
  }
  
  Serial.print(x + 1);
  Serial.print(ledOn);
    
  
  
}

/*const byte numChars = 32;
char receivedChars[numChars]; // an array to store the received data

boolean newData = false;

void recvWithEndMarker() {
 static byte ndx = 0;
 char endMarker = '\n';
 char rc;
 
 // if (Serial.available() > 0) {
           while (Serial.available() > 0 && newData == false) {
 rc = Serial.read();

 if (rc != endMarker) {
 receivedChars[ndx] = rc;
 ndx++;
 if (ndx >= numChars) {
 ndx = numChars - 1;
 }
 }
 else {
 receivedChars[ndx] = '\0'; // terminate the string
 ndx = 0;
 newData = true;
 }
 }
}

void showNewData() {
 if (newData == true) {
 Serial.print("This just in ... ");
 Serial.println(receivedChars);
 newData = false;
 }
}

void setup() {
 Serial.begin(9600);
 Serial.println("<Arduino is ready>");
}

void loop() {
 recvWithEndMarker();
 showNewData();
}

*/