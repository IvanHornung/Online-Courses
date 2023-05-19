daig([7 3 9 1]);  %diagonal matrix

fix(1+rand(5,4)*10); %java-int type

randi(10,5,4); %1-10, 5x4M
randi([5 10], 2,3) %5-10

randn(5); %bell-curve distrubution. Range: -INF-+INF
r = rand(1, 1000000); %standard dev of 1, mean of 1M
hist(r,100); %prints histogram of data. _,number of bins

rng(0); %reset random number strain to 0
rng(1); %starts at second position
[rand, randn, randi(10)]
rng('shuffle'); [rand, randn, randi(10)]; %microsecond clock
