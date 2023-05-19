function total = accumulate(n)
    persistent summa; %keeps value until next call
    if isempty(summa)
        summa = n;
    else
        summa = summa + n;
    end
    total = summa;
