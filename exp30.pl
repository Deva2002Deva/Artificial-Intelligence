% Knowledge Base

% Facts
parent(john, mary).       % John is a parent of Mary
parent(jane, mary).       % Jane is a parent of Mary
parent(mary, susan).      % Mary is a parent of Susan
parent(mary, tom).        % Mary is a parent of Tom
parent(susan, alice).     % Susan is a parent of Alice

% Rules
mother(X, Y) :- parent(X, Y), female(X).  % X is the mother of Y if X is a parent of Y and X is female
father(X, Y) :- parent(X, Y), male(X).    % X is the father of Y if X is a parent of Y and X is male

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).  % X is a grandparent of Y if X is a parent of Z and Z is a parent of Y

sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y. % X and Y are siblings if they share a parent and are not the same person

% Gender facts
female(jane).   % Jane is female
female(mary).   % Mary is female
female(susan).  % Susan is female
female(alice).  % Alice is female

male(john).     % John is male
male(tom).      % Tom is male

% Queries
% Who are the grandparents of Alice?
% ?- grandparent(Grandparent, alice).

% Who are the siblings of Tom?
% ?- sibling(Sibling, tom).

% Is Mary the mother of Susan?
% ?- mother(mary, susan).
