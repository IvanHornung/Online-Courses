%Write a function called halfsum that takes as input a matrix and computes 
% the sum of its elements that are in the diagonal or are to the right of it.
% The diagonal is defined as the set of those elements whose column and row 
% indexes are the same. In other words, the function adds up the element in
% the uppertriangular part of the matrix. The name of the output argument is 
%summa. CALL: summa = halfsum([1 2 3; 4 5 6; 7 8 9])

function summa = halfsum(matrix)
    [row col] = size(matrix);
    summa = 0;
    for r = 1:row
        for c = 1:col
            if r == c
                summa = summa + matrix(r,c);
            elseif c > r
                summa = summa + matrix(r,c);
            end
        end
    end
