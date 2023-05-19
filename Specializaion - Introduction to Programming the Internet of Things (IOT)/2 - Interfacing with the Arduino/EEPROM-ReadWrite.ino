#include EEPROM.h

void setup() {
  int addr, data=1;
  Serial.begin(9600);
  for(addr = 0; add<1024; addr++) {
    EEPROM.write(addr, data);
  }
  for(addr = 0; addr<1024; addr++) {
    Serial.print(EEPROM.read(addr), DEC);
  }
}
