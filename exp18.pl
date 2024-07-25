% Facts: name and date of birth (dob(Name, Day, Month, Year))
dob(john_doe, 15, june, 1990).
dob(jane_smith, 22, july, 1985).
dob(alice_jones, 3, march, 1978).
dob(bob_brown, 12, december, 2000).
dob(charlie_black, 25, august, 1995).

% Query to find the date of birth by name
find_dob(Name, Day, Month, Year) :-
    dob(Name, Day, Month, Year).

% Query to find all people born in a specific month
born_in_month(Month, Name) :-
    dob(Name, _, Month, _).

% Query to find all people born in a specific year
born_in_year(Year, Name) :-
    dob(Name, _, _, Year).

% Utility to print all entries in the database
print_db :-
    findall((Name, Day, Month, Year), dob(Name, Day, Month, Year), List),
    print_list(List).

% Helper predicate to print a list of tuples
print_list([]).
print_list([(Name, Day, Month, Year)|T]) :-
    write(Name), write(': '), write(Day), write(' '), write(Month), write(' '), write(Year), nl,
    print_list(T).

% Example queries
start :-
    % Find the date of birth of john_doe
    find_dob(john_doe, Day, Month, Year),
    write('John Doe was born on: '), write(Day), write(' '), write(Month), write(' '), write(Year), nl,

    % Find all people born in July
    write('People born in July: '), nl,
    born_in_month(july, Name1), write(Name1), nl, fail; true,

    % Find all people born in 1995
    write('People born in 1995: '), nl,
    born_in_year(1995, Name2), write(Name2), nl, fail; true,

    % Print all entries in the database
    write('Database entries: '), nl,
    print_db.
