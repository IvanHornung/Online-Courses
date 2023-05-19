#define ADDR 1;

void setup() {
  Wire.begin();
  Wire.beginTransmission(ADDR);
  Wire.write(2);
  Wire.write(3);
  Wire.endTransmission(stop);
}

//send two bytes
//stop condition sent at the end
