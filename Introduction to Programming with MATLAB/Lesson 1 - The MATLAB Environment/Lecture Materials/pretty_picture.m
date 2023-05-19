function pretty_picture(N)
%PRETTY PICTURE plot a growing cosine wave versus a growing sine
%   PRETTY PICTURE(N) N = the number of points plotted. 500 is a good choice

t = 0:(.99*pi/2):N;
x = t.*cos(t);
y = t.*sin(t);
plot(x,y,'k')
axis square
