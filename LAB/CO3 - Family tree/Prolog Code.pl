% Parent facts
parent(john, alice).
parent(mary, alice).
parent(john, bob).
parent(mary, bob).
parent(bob, charlie).
parent(susan, charlie).

% Father rule
father(X, Y) :-
    parent(X, Y),
    male(X).

% Mother rule
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Gender facts
male(john).
male(bob).
male(charlie).

female(mary).
female(susan).
female(alice).

% Sibling rule
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Grandparent rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
