% Initial Facts
fact(bird(tweety)).
fact(has_wings(tweety)).
fact(bird(eagle)).
fact(has_wings(eagle)).

% Rule 1: Bird + Wings -> Can Fly
fly_rule(bird(X), has_wings(X), can_fly(X)).

% Rule 2: Can Fly -> Can Move
move_rule(can_fly(X), animal_can_move(X)).

% Forward Chaining
forward_chaining(FinalFacts) :-
    findall(F, fact(F), InitialFacts),
    findall(F,
            (fly_rule(A, B, F),
             member(A, InitialFacts),
             member(B, InitialFacts)),
            FlyFacts),
    append(InitialFacts, FlyFacts, Facts2),
    findall(F,
            (move_rule(A, F),
             member(A, Facts2)),
            MoveFacts),
    append(Facts2, MoveFacts, FinalFacts).

% Query
query(Q) :-
    forward_chaining(Facts),
    member(Q, Facts).
