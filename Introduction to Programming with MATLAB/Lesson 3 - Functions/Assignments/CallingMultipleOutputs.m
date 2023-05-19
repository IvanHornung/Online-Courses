%Write a function called corners that takes a matrix as an input argument
%and returns for outputs: the elements at its four courners in this order:
%top_left, top_right, bottom_left, and bottom_right. (Note that loops and
%if-statements are neither necessary not allowed as we have not covered
%them yet.)

A = randi(100,4,5)
[top_left, top_right, bottom_left, bottom_right] = corners(A)
B = [1; 2]
[top_left, top_right, bottom_left, bottom_right] = corners(B)
