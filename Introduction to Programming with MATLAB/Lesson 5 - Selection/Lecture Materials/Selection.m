%Example if-else function
function guess_my_number(x)
    if x == 2
        fprintf('Congrats! You Guessed my number.\n')
end

%Example elseif
function guess_my_number(x)
    if x == 42
        fprintf('Congrats! You Guessed my number.\n')
    elseif x < 42
        fprintf('Too small. Try again.\n')
    else
        fprintf('Too big. Try again.\n')
end
