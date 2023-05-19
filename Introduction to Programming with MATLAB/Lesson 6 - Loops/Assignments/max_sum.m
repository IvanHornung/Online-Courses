function [summa,index] = max_sum(v,n)
    if n > length(v)
        summa = 0;
        index = -1;
        return;
    end      
    sums = [];
    ttl=0;
    isum = 0;
    for j = 1:((length(v)-n) + 1)
        for i=1:n           
           isum = isum + v(ttl+i);
        end
        sums(j) = isum;
        ttl=ttl+1;
        isum = 0;
    end
    summa = max(sums);
    ind = find(sums==max(sums));
    index = ind(1);
end
