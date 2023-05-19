[row col] = size(A);
for r = 1:row
    fprintf('Working on row %d...',r);
    for c = 1:col
        P(r,c) = A(r,c) * A(r,c);
        fprintf('(%d %d)\n',r,c)
    end
end

%* tree
N = 7; 
for mm = 1:N
    for nn = 1:mm
        fprintf('*');
    end
    fprintf('\n');
end
