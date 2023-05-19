%% The Ultimate Legend of Big John
page{1} = 'You could find him on the field almost any day.';
page{2} = 'Tall, dark hair, and eyes of steel gray.';
page{3} = 'They say he pulled on Frisbee ''bout half a mile,';
page{4} = 'And when he''d stick in the corner, you could almost catch a smile';
page{5} = 'On Big John.';
%% Print it
fprintf('\n');
for ii = 1:length(page)
    fprintf('%s\n',page{ii});
end
fprintf('\n');
%% Cell array ex
p = cell(2,3);
p{2,1} = pi;
p{1,1} = int8(-17);
p{2,2} = 'Awesome';
p{2,3} = [2 4; 6 8; 10 12];
p{1,3} = sum(p{2,3});
p{1,2} = 1/0;
class(p); %cell
class(p{1,2}) %double
class(p(1,2)) %cell

p{2,3}(3,2); %ans = 12
