#define ADDR 1;

//receive two bytes from the slave, compute sum
//Wire.available() is used to check how much data is received.
void setup() {
  int sum = 0;
  Wire.requestFrom(ADDR, 2);
  while(Wire.available()) {
    sum += (int)(Wire.read());
  }
}
