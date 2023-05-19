%% Character Arrays
%% Ex 1
function char_codes
    for ii = 33:126
        fprintf('%s',ii);
    end
    fprintf('%s',10); %newline character
%% Ex 2
MOOC_title = 'MATLAB for Smarties';
length(MOOC_title) %ans = 19
MOOC_title(1) %ans = M
MOOC_title(end-8:end) %ans = Smarties
a = MOOC_title(1:6) %ans = MATLAB
b = a(end:-1:1) %b = BALTAM
%% Ex 3
message = 'Let''s skip class today!'
code = double(message)
%76 101 116 39 115...
secret = char(code + 3)
%encoded message
%% Ex 4
friends = ['Bill';'Mary';'John'] %have to have same lengths
%% Ex 5
MOOC_title; %MATLAB for Smarties
findstr(MOOC_title, 'LAB') %ans = 4
findstr(MOOC_title, 'r') %ans = 10  15
lang = 'MATLAB'
strcmp(MOOC_title, lang) %ans = 0
strcmp(MOOC_title(1:6), lang) %ans = 1
strcmpi(MOOC_title(1:6), 'Matlab') %ans = 1 true
str2num();
