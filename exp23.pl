% Facts: parent(Parent, Child)
parent(john, mary).
parent(john, tom).
parent(mary, alice).
parent(mary, bob).
parent(tom, claire).
parent(tom, dave).
parent(alice, eve).
parent(bob, frank).

% Rules to define relationships

% A person is a mother if they are a parent and the child is their offspring
mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

% A person is a father if they are a parent and the child is their offspring
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

% Siblings share at least one parent
sibling(Person1, Person2) :-
    parent(Parent, Person1),
    parent(Parent, Person2),
    Person1 \= Person2.

% A grandparent is a parent of a parent
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

% Check if a person is female
female(mary).
female(alice).
female(claire).
female(eve).

% Check if a person is male
male(john).
male(tom).
male(bob).
male(frank).
male(dave).

% Utility to print all relationships
print_family :-
    findall((Mother, Child), mother(Mother, Child), Mothers),
    findall((Father, Child), father(Father, Child), Fathers),
    findall((Person1, Person2), sibling(Person1, Person2), Siblings),
    findall((Grandparent, Grandchild), grandparent(Grandparent, Grandchild), Grandparents),
    write('Mothers:'), nl, print_list(Mothers),
    write('Fathers:'), nl, print_list(Fathers),
    write('Siblings:'), nl, print_list(Siblings),
    write('Grandparents:'), nl, print_list(Grandparents).

% Helper predicate to print a list of tuples
print_list([]).
print_list([(A, B)|T]) :-
    write(A), write(' - '), write(B), nl,
    print_list(T).

% Example queries
start :-
    % Find siblings of Alice
    write('Siblings of Alice:'), nl,
    sibling(alice, Sibling),
    write(Sibling), nl, fail; true,

    % Find grandparents of Eve
    write('Grandparents of Eve:'), nl,
    grandparent(Grandparent, eve),
    write(Grandparent), nl, fail; true,

    % Print all relationships
    print_family.
mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

sibling(Person1, Person2) :-
    parent(Parent, Person1),
    parent(Parent, Person2),
    Person1 \= Person2.

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).
