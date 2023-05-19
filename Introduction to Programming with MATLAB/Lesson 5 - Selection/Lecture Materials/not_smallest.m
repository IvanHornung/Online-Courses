function a = not_smallest(x,y,z)
    if ~(x >= y || x >= z)
        a = 0;
    else
        a = 1;
end
