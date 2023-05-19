%% Logical Indexing
%% Example 1
    w = [];
    jj = 0;
    for ii = 1:length(v)
        if v(ii) >= 0
            jj = jj+1;
            w(jj) = v(ii);
        end
    end
%% Example 1 Revised
    w = [];
    for ii = 1:length(v)
        if v(ii) >= 0
            w = [w v(ii)];
        end
    end
%% Example 1 Ultimate Solution
    w = v(v >= 0); %logical indexing. All in one line.
%% Built-in Logical function
holmes = logical([1 -2 0 0 9.12 -2]);
%1 1 0 0 1 1 
c = 1:3;
a(c); %1 3
%a is c where logical values are true
rng(0);
r = randi(10,1,6); %9 10 2 10 7 1
holmes; %1 1 0 0 1 1 
r(holmes) %9 10 7 1
