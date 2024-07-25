% Define the graph using facts
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 3).
edge(c, d, 1).
edge(c, e, 6).
edge(d, e, 1).

% Define the heuristic function (example heuristic values)
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 0).

% Best First Search algorithm
best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),
    bfs([[Start, H]], Goal, [], Path).

% Base case: if the goal is reached
bfs([[Goal|Path]|_], Goal, _, [Goal|Path]).

% Recursive case: expand the most promising node
bfs([[Node|Path]|Rest], Goal, Visited, FinalPath) :-
    findall([NextNode, NextH, Node|Path],
            (edge(Node, NextNode, _), \+ member(NextNode, [Node|Path]), heuristic(NextNode, NextH)),
            Neighbors),
    append(Rest, Neighbors, NewQueue),
    sort(2, @=<, NewQueue, SortedQueue),
    bfs(SortedQueue, Goal, [Node|Visited], FinalPath).

% Utility to print the path
print_path([]).
print_path([H|T]) :-
    write(H), write(' '),
    print_path(T).

% Example usage
start :-
    best_first_search(a, e, Path),
    reverse(Path, CorrectPath),
    write('Path: '), print_path(CorrectPath), nl.
