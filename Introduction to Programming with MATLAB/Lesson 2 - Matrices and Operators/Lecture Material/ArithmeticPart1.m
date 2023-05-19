>> x = [1 5 -2; 3 0 7]
x =
     1     5    -2
     3     0     7
>> y = [1:3, 4:6]
y =
     1     2     3     4     5     6
>> z = x + y
Matrix dimensions must agree. 
>> y = [1:3; 4:6]
y =
     1     2     3
     4     5     6
>> z = x + y
z =
     2     7     1
     7     5    13
>> %array multiplication
>> z = x.*y
z =
     1    10    -6
    12     0    42
    
