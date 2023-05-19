%Write a function called saddle that finds saddle points in the input matrix M.
% For the purposes of this problem, a saddle point is defined as an element whose
% value is greater than or equal to every element in its row, and less than or equal
% to every element in its column. Note that there may be more than one saddle point 
% in M. Return a matrix called indices that has exactly two columns. Each row of indices
% corresponds to one saddle point with the first element of the row containing the row 
% index of the saddle point and the second element containing the column index. If there 
% is no saddle point in M, then indices is the empty array.
function indices = saddle(M)
    total = 0;
    [row, col] = size(M);
    indices = zeros(row+col,2);
    for i = 1:row
        tMax = max(M(i,:));
        [tempVar1,tempVar2] = find(M(i,:) == tMax);
        for v = 1:length(tempVar1)
            iterVarT2 = tempVar2(v);
            minim = min(M(:, iterVarT2));
            if M(i, iterVarT2) == minim
                total = total + 1;
                indices(total, :) = [i,iterVarT2];
            end
        end
    end
    indices = indices(1:total,:);
    end
