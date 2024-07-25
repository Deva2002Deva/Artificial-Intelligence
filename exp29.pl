% Facts
fact(raining).
fact(windy).

% Rules
rule(wet_grass) :-
    fact(raining).

rule(chilly) :-
    fact(windy).

rule(umbrella) :-
    fact(raining),
    fact(windy).

% Forward chaining to infer new facts
forward_chain :-
    findall(R, (rule(R), \+ fact(R)), Rules),
    apply_rules(Rules).

apply_rules([]).
apply_rules([H|T]) :-
    assert(fact(H)),
    apply_rules(T).

% Query to run forward chaining and display all inferred facts
start_forward_chaining :-
    forward_chain,
    findall(F, fact(F), Facts),
    write('Inferred facts: '), write(Facts), nl.
