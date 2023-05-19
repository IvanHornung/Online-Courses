/*Write a program that causes the built-in LED connected to pin 13 on the Arduino to blink, alternating between fast blinks and slow blinks.
The LED should blink 5 times quickly and then it should blink 5 more times slowly. When blinking quickly, the LED should have a 1 second
period, so it should be high for 0.5 seconds and low for 0.5 seconds. When blinking slowly, the LED should have a 4 second period, so 
it should be high for 2 seconds and low for 2 seconds. The LED should continue to blink in this alternating fashion for as long as the 
Arduino receives power.*/

void setup() {
	pinMode(13, OUTPUT);
}

void loop() {
	for(int i = 0, ms; i < 10; i++) {
		if( i < 5)
			ms = 500;
		else
			ms = 2000;
		digitalWrite(13, HIGH);
		delay(ms);
		digitalWrite(13, LOW);
		delay(ms);
	}
}
