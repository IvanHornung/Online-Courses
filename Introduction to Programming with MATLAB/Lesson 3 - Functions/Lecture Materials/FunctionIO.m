function [a,s] = myRand(low, high) %two outputs
    a = low+rand(3,4)*(high-low);
    v = a(:); %all elements
    s = sum(v);
end
