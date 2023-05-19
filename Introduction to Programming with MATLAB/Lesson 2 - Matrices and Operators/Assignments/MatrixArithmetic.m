%{Given Matrix A:
 - Create a row vector of 1's that has the same number of elements as A has rows.
 - Create a column vector of 1's that has the same number of elements as A has columns. 
 - Using matrix multiplication, assign the product of the row vector, the matrix A, and the column vector (in this order) to the variable result.%]
 
A = [1:5; 6:10; 11:15; 16:20];
row_vector = ones(1,size(A,1)) %function
column_vector = ones(size(A,2), 1)
result = row_vector*A*column_vector
