% Facts
parent(john, mary).
parent(john, david).
parent(mary, susan).

male(john).
male(david).
female(mary).
female(susan).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

grandfather(X, Z) :-
    grandparent(X, Z),
    male(X).

grandmother(X, Z) :-
    grandparent(X, Z),
    female(X).
