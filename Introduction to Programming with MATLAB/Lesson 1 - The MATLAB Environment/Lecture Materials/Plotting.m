x_coordinates = [1,3,10]; %vector
y_coordinates = [2,-4.2,12.3];
plot(x_coordinates, y_coordinates);

length(x_coordinates)
%3

plot(x_coordinates, y_coordinates, '*'); %plots asteriks instead of line

plot(x_coordinates, y_coordinates, 'rs'); %points are now red squares
grid on

xlabel('Selection')
ylabel('Change')
title('Changes in Selections during the past year')

axis([0,12,-10,20]);
bar(x_coordinates, y_coordinates);  %bar graph

figure
pie([4 2 7 4 7])
close(2) %closes figure 2
close all

imread('Palace.JPG') %CRTL+C

pretty_picture = imread('Palace.JPG');
image(pretty_picture) %displays picture
axis off
quit %closes MATLAB
