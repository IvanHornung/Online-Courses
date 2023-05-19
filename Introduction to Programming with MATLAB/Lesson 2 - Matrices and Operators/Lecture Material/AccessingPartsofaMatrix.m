x = [1:4; 5:8; 9:12]; %3r 4c
x(2,3); %7
center = x(2,3);
x(2,3) = 97;
XYZ(2,2) = 123;
%makes blank(0) 2-2 matrix with 2,2 = 123
x(4,5) = 456; %extends current matrix
x = [1 2 3; 4 5 6];
x(2, [1 3]); %interestedin second row, columns 1 & 3
x([2,1],2); %row 2, then 1, column 2 for both
x(2:-1:1, 3:-1:1);
x(end, 2); %last row index
x(2, end) %reserved word
x([2 end 1 end], 3);
x(:,:); %all rows all column
x(1,:); %same as 1:end
