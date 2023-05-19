%Write a function called minimax that takes M, a matrix input argument and
%returns mmr, a row vector containing the absolute values of the difference
%between the maximum and minimum valued elements of each row. As a second
%output argument called mmm, it provides the difference between the maximum
%and the minimum in the entire matrix.
%CALL: [mmr, mmm] = minimax([1:4;5:8;9:12]);

function [mmr, mmm] = minimax(matrix)
    mmr=abs(max(matrix')-min(matrix'));
    mmm=(max(max(matrix'))-min(min(matrix')))
end
