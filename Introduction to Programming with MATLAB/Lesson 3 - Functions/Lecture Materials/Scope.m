function [a,s] = myRand(low, high)
    a = low+rand(3,4)*(high-low);
    s = sumAllElements(v);

function summa = sumAllElements(M)
    global v;
    v = M(:);
    summa = sum(v);
