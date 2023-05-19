#Servo Control

'Servo Motor Wiring'
#Three wires:
#   -Power (red)
#   -Ground (black)
#   -Signal (white or yellow)
#PWN applied to signal wire
#Power should supply sufficient current

'Servo Motor Power'
#External power supply should be used
#   -~5 Volts
#Raspberry Pi cannot supply enough current to drive typical motors
#   -~1 Amp
#External supply has power and ground wires
#   -Wire external power wire to Servo power wire
#   -External ground wired to Raspberry Pi ground

'Servo Wiring'
#Only pins 12 and 24 (BOARD numbering) can produce PWN signals
#Resistor might be used to isolate pins from servo