% Base case: the sum of an empty list is 0
sum_list([], 0).

% Recursive case: the sum of a list with head H and tail T is H plus the sum of T
sum_list([H|T], Sum) :-
    sum_list(T, SumTail),
    Sum is H + SumTail.
