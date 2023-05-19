%% Structs
%% Structs in Action
r.ssn = 12345678
% r = 
%       snn: 12345678
class(r) %struct
class(r.ssn) %double
%%%
r.name = 'Homer Simpson'
% r = 
%      ssn: 12345678
%      name: 'Homer Simpson'
r.address.street = '742 Evergreen Terrace'
%+address: [1x1 struct]
%% Account Example
account.number = 12345
acount.owner.name = 'Joe Biden'
account.owner.email = 'joe@biden.com'
account(2).number = 67890
