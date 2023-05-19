%caeser shift encryption/decryption method
function coded = caesar(character_vector,shift_amount)
    rawtext = double(character_vector)+ shift_amount
    for i = 1:length(rawtext)
        if rawtext(i) > 126
            while rawtext(i) > 126
             rawtext(i) = (rawtext(i)-126) + 31
            end
        end
        if rawtext(i) < 32
            while rawtext(i) < 32
             rawtext(i) = 126-(31-rawtext(i))
            end
        end
    end
    coded = char(rawtext);
