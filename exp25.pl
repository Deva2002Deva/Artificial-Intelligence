% Initial state: monkey and box at door, banana at middle
initial(state(at_door, at_door, on_floor, has_not)).

% Goal state: monkey has the banana
goal(state(_, _, _, has)).

% move the monkey from one place to another
move(state(Monkey, Box, on_floor, has_not), go(Monkey, NewPlace), state(NewPlace, Box, on_floor, has_not)).

% push the box from one place to another
move(state(Monkey, Monkey, on_floor, has_not), push(Monkey, NewPlace), state(NewPlace, NewPlace, on_floor, has_not)).

% climb on the box
move(state(Monkey, Box, on_floor, has_not), climb, state(Box, Box, on_box, has_not)).

% grasp the banana if standing on the box
move(state(Monkey, Box, on_box, has_not), grasp, state(Monkey, Box, on_box, has)).

% solve the problem by finding a sequence of moves from initial state to goal state
solve(S, S, []).

solve(S, G, [Move|Moves]) :-
    move(S, Move, S1),
    solve(S1, G, Moves).

% start solving the problem
start :-
    initial(S),
    goal(G),
    solve(S, G, Moves),
    write('Moves: '), write(Moves), nl.
