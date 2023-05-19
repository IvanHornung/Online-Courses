/*
  Write a sketch that allows a user to access data in EEPROM using the serial monitor. In the serial monitor the user should be able to type one of two commands: “read” and “write. "Read" takes one argument, an EEPROM address. "Write" takes two arguments, an EEPROM address and a value.

  For example, if the user types “read 3” then the contents of EEPROM address 3 should be printed to the serial monitor. If the user types “write 3 10” then the value 10 should be written into address 3 of the EEPROM.

  In order to grade this assignment, you will perform a simulation on the website www.tinkercad.com. You will need to create an account for free. There are instructional videos on that website that will teach you how to use the simulator.
 */


#include <EEPROM.h>

void setup() {
  Serial.begin(9600);
  Serial.println("--Enter Command--");
  Serial.println("-To read, simply type 'read' followed by the EEPROM address.");
  Serial.println("-To write, simply type 'write' followed by the EEPROM address and the value.");
}

void loop() {
  String input;
  int address, data;
  if(Serial.available()) {
    input = Serial.readString();
    if(input.startsWith("write")) {
       address = input.substring(6,7).toInt();
       data = input.substring(8).toInt();
       EEPROM.write(address, data);
       print_write(address, data);
    } else if(input.startsWith("read")) {
      address = input.substring(5).toInt();
      print_read(address);
      Serial.println(EEPROM.read(address));
    } 
  }
}

void print_write(int address, int data) {
  Serial.print("Data '");
  Serial.print(data);
  Serial.print("' written to address '");
  Serial.print(address);
  Serial.println("'.");
}

void print_read(int address) {
  Serial.print("Data retrieved from addres '");
  Serial.print(address);
  Serial.println("':");
}
