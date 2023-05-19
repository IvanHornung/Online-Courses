%Write a function called char_counter that counts the number of a certain
%character in a text file. The function takes two input arguments, fname, a
%char vector of the filename and character, the char it counts in the file.
%The function returns charnum, the number of characters found. If the file
%is not found or character is not a valid char, the function returns -1.
%Use simple.txt and Frankenstein-by-Shelley.txt

function charnum = char_counter(fname, character)
    fhandle = fopen(fname,'rt');
    if fhandle < 0
        charnum = -1;
        return;
    end
    if (ischar(character)) && (fhandle > 0)
        iter = 0;
        read = fgets(fhandle);
        while ischar(read)
            iter = count(read,character) + iter;
            read = fgets(fhandle);
        end
        charnum = iter;
    else 
        charnum = -1;
    end
    fclose(fhandle);
