function sumintup(N)
    total = 0;
    for n = 1:N
        total = total + n;
    end
    fprintf('total equals %d\n',total);
    
    
    %another example
    list = rand(1,5); %assigns a row vector of random numbers
    for x = list
        if x > 0.5
            fprintf('Random number %f is large.\n',x);
        else
            fprintf('Random number %f is small.\n',x);
        end
    end
    
    %same thing but calling a function
    for x = rand(1,5)
        if x > 0.5
            fprintf('Random number %f is large.\n',x);
        else
            fprintf('Random number %f is small.\n',x);
        end
    end
