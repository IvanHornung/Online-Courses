#define ADDR 1;

//Typical Slave Receive Code
void receiveFunct(int byteNum) {
  int i, sum = 0;
  for(i=0; i < byteNum; i++) {
    sum += Wire.read();
  }
  Serial.print(sum);
}

Wire.onReceive(receiveFunct);

//Typical Slave Trasmit Code

void transmitFunct(void) {
  Wire.write(SOME_DATA_BYTE);
}

Wire.onRequest(transmitFunct);
