%COMMENTS APPEAR IN HELP + METHOD_NAME CMD

function [table summa] = multable(n,m)
   %MULTITABLE multiplication talbe.
   % T = MULTALBE(N) returns a N-by-N matrix
   % containing the multiplication table for
   % the integers 1 through N.
   % MULTABLE(N,M) returns an N-by-M matrix.
   % Both input arguments must be positive integers.
   % [T SM] = MULTABLE(...) returns the matrix
   % containing the multiplication talbe in T
   % and the sum of all its elements in SM.
  
   if nargin < 1
       error('must have at least one input argument');
   end
   if nargin < 2
       m = n;
   elseif ~isscalar(m) || m < 1 || m ~= fix(m)
       error('m needs to be a positive integer');
   end
   if ~isscalar(m) || m < 1 || m ~= fix(m)
       error('m needs to be a positive integer');
   end
  
   table = (1:n)' * (1:m);
  
   if nargout = 2
       summa = sum(table(:));
   end
