a = (1:10).^2
plot(a)
a= (-10:10).^2
figure(2)
plot(a)

t = -10:10
b = t.^2
figure
plot(t,b);

x1 = 0:0.1:2*pi; y1 = sin(x1);
x2 = pi/2:0.1:3*pi; y2 = cos(x2);

plot(x1,y1,x2,y2);


figure
plot(x1,y1,'r',x2,y2,'k:'); %red, black-dotted
help plot

figure(1)
plot(t,b, 'm--o') %magenta dashed line, circles at points

figure(2)
plot(x1,y2,'r')
hold on
plot(x2,y2,'k:')
hold off
plot(x1,y1,'g*')
figure(3)
grid %shows some lines on the graph
legend('sine,'cosine') %creates a legend
axis([-2 12 -1.5 1.5])
close(4)
close(1)
close all
clear
clc
