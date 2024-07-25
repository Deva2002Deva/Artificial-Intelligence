% Base case: The sum of integers from 1 to 0 is 0.
sum_to_n(0, 0).

% Recursive case: The sum of integers from 1 to N is N plus the sum of integers from 1 to N-1.
sum_to_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_to_n(N1, Sum1),
    Sum is N + Sum1.

% Query to start the summation
start_sum(N, Sum) :-
    sum_to_n(N, Sum),
    write('The sum of integers from 1 to '), write(N), write(' is '), write(Sum), nl.
