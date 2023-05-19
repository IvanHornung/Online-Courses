%Write a function called next_prime that takes a scalar positive input n.
%Use a while-loop to find and return k, the smallest prime number that is
%greater than n. Feel free to use the built-in isprime function.

function k = next_prime(n)
    prime = false;
    i = n + 1;
    while ~prime
        if isprime(i)
            prime = true;
            k = i;
        end
        i = i + 1;
    end
