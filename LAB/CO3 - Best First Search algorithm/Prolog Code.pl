% Graph
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).
edge(d, h).
edge(e, h).
edge(f, g).
edge(g, h).

% Heuristic values
h(a, 7).
h(b, 6).
h(c, 5).
h(d, 4).
h(e, 3).
h(f, 4).
h(g, 2).
h(h, 0).

% Best First Search
best_first(Start, Goal, Path) :-
    search([node(Start, [Start])], Goal, Path).

search([node(Goal, Path)|_], Goal, Path).

search([node(Current, Path)|Rest], Goal, Solution) :-
    findall(
        node(Next, [Next|Path]),
        (edge(Current, Next),
         \+ member(Next, Path)),
        Children
    ),
    append(Rest, Children, NewList),
    sort_nodes(NewList, SortedList),
    search(SortedList, Goal, Solution).

% Sort nodes according to heuristic value
sort_nodes(Nodes, Sorted) :-
    predsort(compare_nodes, Nodes, Sorted).

compare_nodes(<, node(A,_), node(B,_)) :-
    h(A, HA),
    h(B, HB),
    HA < HB.

compare_nodes(>, node(A,_), node(B,_)) :-
    h(A, HA),
    h(B, HB),
    HA > HB.

compare_nodes(=, _, _).
