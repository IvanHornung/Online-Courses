#include <Ethernet.h>


//Server Receives Data
EthernetServer server = EthernetServer(80); //port 80
void setup() {
  Ethernet.begin(mac, ip, gateway, subnet); //specify IP address, dont rely on DHCP
  server.begin(); //start the listening
}

void loop() {
  EthernetClient client = server.available();
  //you should check for availability first before we call client.read
  if(client) {
    Serial.print(client.read());
  }
}
//receives data on port 80 and just prints it.
