function [n total] = possum(limit)
    total = 0;
    n = 0;
    while total <= limit
        n = n + 1;
        total = total + n;
    end
    fprintf('sum: %d   count: %d\n', total,n)
    
function y = approx_sqrt(x)
    y = x;
    while abs(y^2 - x) > 1e-7*x
        y = (x/y+y)/2
    end
    
    %sqrt(-200) -- retrns 14.14i
    %15 + 3i = 15i
    %i = 7; clear i
