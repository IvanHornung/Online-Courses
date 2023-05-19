%% Excel Files
%% Ex 1
[num, txt, raw] = xlsread('Nashville_climate.xlsx');
[~, text] = xlsread('Nashville_climate.xlsx');
[~, ~, everything] = xlsread('Nashville_climate.xlsx');
num = xlsread('Nashville_climate.xlsx', 1, 'D15');
num = xlsread('Nashville_climate.xlsx', 1, 'D15:E17');
