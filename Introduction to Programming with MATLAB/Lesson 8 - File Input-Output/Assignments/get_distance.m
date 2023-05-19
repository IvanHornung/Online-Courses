% The attached Distances.xlsx  file contains a spreadsheet with the pairwise 
% distances in miles of the top 100 US cities by population. A preview of the 
% spreadsheet is shown below. The first row and first column contain the city names
% using the following format: city name comma space capitalized state abbreviation,
% e.g., Nashville, TN. Note that the very first cell of the spresheet, A1, is blank. 
% Write a function called get_distance that accepts two character vector
% inputs representing the names of two cities. The function returns the
% distance between them as an output argument called distance. For ex, the
% call get_distance('Seattle, WA','Miami, FL') should return 3723. If one or
% both of the specified cities are not in the file, the function returns -1.

function distance = get_distance(x,y)
    [~,~,text] = xlsread('Distances.xlsx');
    [first second]=size(text);
    t1=0; t2=0;
    for i = 2:first
        if strcmp(text{i,1},x) == 1
            t1 = i;
        end
    end
    for i = 2:second
        if strcmp(text{1,i}, y) == 1
            t2=i;
        end
    end
    if t2>1 && t1>1
        distance = text{t1, t2};
    else 
        distance = -1;
    end
