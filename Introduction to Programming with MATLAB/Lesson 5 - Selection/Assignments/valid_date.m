%Write a function called valid_date that takes three positive integer
%scaler inputs year, month, day. If these three represent a valid date,
%return a logical true, otherwise false. The name of the output argument is
%valid. If any of the inputs is not a positive integer scalar, return false
%as well. Note that every year is divisible by 4 is a leap year, except for
%the years that are exactly divisible by 100. However, years thatare
%exactly divisible by 400 are also leap years. For example, the year 1900
%was not a leap year, but the year 2000 was. Not that the solution must not
%contain any of the date related built-in MATLAB functions.

function valid = valid_date(year, month, day)
  valid = true;
  if month > 12
      valid = false;
  elseif (~isscalar(year) || year < 1 || year ~= fix(year)) || (~isscalar(month) || month < 1 || month ~= fix(month)) || (~isscalar(day) || day < 1 || day ~= fix(day))
      valid = false;
  elseif (day > 31) || (day > 30 && (month == 2 ||month == 4 ||month == 6 ||month == 9 ||month == 11))
      valid = false;
  elseif ((month == 2) && day == 29 && ((year/4~=fix(year/4)) || ((year/100==fix(year/100) && ~(year/400==fix(year/400))))))
      valid = false;
  end
