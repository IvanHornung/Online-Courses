int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 9;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  float voltage = sensorValue*(5.0 / 1023.0);
  // turn the ledPin on
  if(voltage < 1){
    digitalWrite(ledPin, LOW);
  } else {
    // turn the ledPin off:
    digitalWrite(ledPin, HIGH);
  }
  Serial.println(voltage);
  // stop the program for for <sensorValue> milliseconds:
  delay(sensorValue);
}
