
%{ We borrowed $1000 at a 10% annual interest rate. If we did not make a payment for two years,
and assuming there is no penalty for non-payment, how much do we owe now? Assign the result to a variable called %}

principle = 1000;
rate = 0.10;
years = 2;
debt = principle*(1+rate)^years
