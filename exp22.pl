% Facts: bird(Name, CanFly)
bird(eagle, true).
bird(parrot, true).
bird(penguin, false).
bird(ostrich, false).
bird(sparrow, true).
bird(kiwi, false).

% Query to check if a particular bird can fly
can_fly(Bird) :-
    bird(Bird, true),
    write(Bird), write(' can fly.'), nl.

can_fly(Bird) :-
    bird(Bird, false),
    write(Bird), write(' cannot fly.'), nl.

% Utility to print all birds and their flying ability
print_birds :-
    findall((Bird, CanFly), bird(Bird, CanFly), List),
    print_list(List).

% Helper predicate to print a list of tuples
print_list([]).
print_list([(Bird, CanFly)|T]) :-
    (CanFly = true -> write(Bird), write(' can fly.'), nl ;
    write(Bird), write(' cannot fly.'), nl),
    print_list(T).

% Example queries
start :-
    % Check if specific birds can fly
    can_fly(eagle),
    can_fly(penguin),
    can_fly(kiwi),

    % Print all birds and their flying ability
    write('All birds and their flying ability:'), nl,
    print_birds.
