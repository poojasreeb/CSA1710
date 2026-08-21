% Monkey Banana Problem

solve(Actions) :-
    solve(monkey(door), box(window), floor, no, Actions).

solve(monkey(B), box(B), floor, no,
      [push_box(B, middle)|Actions]) :-
    B \= middle,
    solve(monkey(middle), box(middle), floor, no, Actions).

solve(monkey(middle), box(middle), floor, no,
      [climb_box|Actions]) :-
    solve(monkey(middle), box(middle), on_box, no, Actions).

solve(monkey(middle), box(middle), on_box, no,
      [grasp_banana]) :-
    write('Monkey gets the bananas.'), nl.

solve(monkey(A), box(B), floor, no,
      [walk(A,B)|Actions]) :-
    A \= B,
    solve(monkey(B), box(B), floor, no, Actions).
