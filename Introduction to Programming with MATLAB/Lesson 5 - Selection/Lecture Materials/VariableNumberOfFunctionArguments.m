%nargin returns the number of actual input arguments that the function was
%called with. nargout returns the number of output arguments that the
%function caller requested.

%Returns an n-by-m multiplication table in the output argument table.
%Optionally, it can return the sum of all elements in the output argument
%summa. If m is not provided, it returns a n-by-n matrix
function [table summa] multable(n,m)
   if nargin < 2
       m = n
   end
   table = (1:n)' * (1:m);
  
   if nargout == 2
       summa = sum(table(:));
   end
