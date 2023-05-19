%Write a function called trio that takes two positive integer inputs n and
%m. The function returns a 3n-by-m matrix called T. The top of T (an n by m
%submatrix) is all 1s, the middle third is all 2-s while the bottom third
%is all 3-s. CALL: T = trio(2,4)

function T = trio(n, m)
    T(3*n,m)=3;
    T(1:n,:)=1;
    T((n+1):2*n,:)=2;
    T((2*n+1):3*n,:)=3;
end
