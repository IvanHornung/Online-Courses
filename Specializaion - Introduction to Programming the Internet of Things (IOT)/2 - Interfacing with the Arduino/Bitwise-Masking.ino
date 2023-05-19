#include EEPROM.h

//Writing an int to EEPROM

int bigData;
byte littleDate;

void setup() {
  littleData = bigData & 0xFF; //hexadecimal for eight 1s
  EEPROM.write(0, littleData);
  littleData = (bigData >> 8);
  EEPROM.write(1, littleData);
  //Little Endian ordering
}
