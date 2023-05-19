%{I have to write a function called echo_gen that adds an echo effect to an audio recording. The function is to be called like this:
output = echo_gen(input, fs, delay, amp);
where input is a column vector with values between -1 and 1 representing a time series of digitized sound data. 
The input argument fs is the sampling rate. The sampling rate specifies how many samples we have in the data each second.
For example, an audio CD uses 44,100 samples per second. The input argument delay represent the delay of the echo in seconds.
That is, the echo should start after delay seconds have passed from the start of the audio signal. Finally, amp specifies the
amplification of the echo which normally should be a value less than 1, since the echo is typically not as loud as the original signal. 
The output of the function is a column vector containing the original sound with the echo superimposed. The output vector will be
longer than the input vector if the delay is not zero (round to the nearest number of points needed to get the delay, as opposed 
to floor or ceil). A sound recording has values between -1 and 1, so if the echo causes some values to be outside of this range,
you will need to normalize the entire vector, so that all values adhere to this requirement.%}

function output = echo_gen(input, fs, delay, amp)
    rounded = round(delay/(1/fs));
    output = [input; zeros(rounded, 1)] + [zeros(rounded, 1); input.*amp];
    if max(abs(output)) > 1
       output = output./max(abs(output));
    end
    end
