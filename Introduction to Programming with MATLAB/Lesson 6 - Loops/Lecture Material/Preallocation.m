%% Preallocation
%% Tic Toc
tic; sum(1:1e3); toc
%Elapsed time is 0.001008 seconds.
%% Example 1
function noprealloc
    N = 5000;
    for ii = 1:N
        for jj = 1:N
            A(ii,jj) = ii*jj;
        end
    end
end
    %tic toc is like 45 seconds. 25M calculations
%% Example 2
function prealloc 
    N = 5000;
    A = zeros(N,N);
    for ii = 1:N
        for jj = 1:N
            A(ii, jj) = ii*jj;
        end
    end
end   %memory allocation. this is 78 times faster than the previous example
