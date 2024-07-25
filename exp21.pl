% Move N disks from Source to Target using Auxiliary peg
hanoi(0, _, _, _) :- !.  % Base case: No disks to move
hanoi(N, Source, Target, Auxiliary) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Target),    % Move N-1 disks from Source to Auxiliary
    move(Source, Target),                    % Move the Nth disk from Source to Target
    hanoi(N1, Auxiliary, Target, Source).    % Move N-1 disks from Auxiliary to Target

% Move a single disk from Source to Target
move(Source, Target) :-
    write('Move disk from '), write(Source),
    write(' to '), write(Target), nl.

% Utility to start the Hanoi problem
start_hanoi(N) :-
    write('Solving Towers of Hanoi for '), write(N), write(' disks:'), nl,
    hanoi(N, a, c, b).  % Move N disks from peg 'a' to peg 'c' using peg 'b' as auxiliary

