speed_kps = 300000
year_sec = 365*24*60*60

lightyear_km = year_sec * speed_kps
%9.4608e+12 = 9.4608 * 1 trillion (12 zeros)

%ALL OF THE BELOW ASSIGN 0.05 to x
x = 5e-2
x = 0.05
x = 0.005e1

earth_to_sun_km = 150e6
%>>150000000

earth_to_sun_sec = earth_to_sun_km/speed_kps
%>>500
eath_to_sun_minutes = earth_to_sun_sec/60
#>>8.3333

%Calculate Moon-Earth time
earth_to_moon_km = 384400
earth_to_sun_sec = earth_to_moon_km/speed_kps
%>>1.28

>>save
%saves the file

>>clear
%clears out the workspace

>>clc
%clear command window

abs_zero_C = -273.15
abs_zero_F = abs_zero_C*9/5 + 32; %colon blocks immediate output in wrkspc
paper_ignition_F = 451;

x = 42; y = 8; %two commands in one line
x = 42, y = 87; %does actually print x = 42

%commands that are long
a_really_long_variable_name = 7;
another_long_one = 17;
yet_another_long_variable_name = a_really_long_variable_name*...
another_long_one
#>>119
