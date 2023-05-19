#include <Ethernet.h>


//Client Sends Data
byte mac[]={0xDE, 0xAD, 0xBE, 0xEF, 0x12, 0x34};
char server[] = "testdomain.edu";
EthernetClient client;
void setup() {
  Ethernet.begin(mac);
  if(client.connect(server, 80)) {
    client.println("GET index.html HTTP/1.1");
    client.stop();
  }
  //send a GET request to a web server
  //Port 80 used for the web
}


//Client Receives Data
void loop() {
  if(client.available())
    Serial.print(client.read());
  //Recieves a response from the web server
  //Sends data to serial monitor
}
