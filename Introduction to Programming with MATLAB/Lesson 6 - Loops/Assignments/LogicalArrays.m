%Write a function called freezing that takes a vector of numbers that
%correspond to daily low temperatures in Fahrenheit. Return numfreeze, the
%number of days with subfreezing temperatures (below 32 F) without using
%loops. CALL: numfreeze = freezing([45 21 32 31 51 12])

function numfreeze = freezing(vector)
    numfreeze = length(vector(vector<32));
end
