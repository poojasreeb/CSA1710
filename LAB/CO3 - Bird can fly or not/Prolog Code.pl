bird(sparrow).
bird(eagle).
bird(parrot).
bird(pigeon).
bird(penguin).
bird(ostrich).

can_fly(sparrow).
can_fly(eagle).
can_fly(parrot).
can_fly(pigeon).

cannot_fly(penguin).
cannot_fly(ostrich).

fly(Bird) :-
    can_fly(Bird).

fly(Bird) :-
    cannot_fly(Bird),
    fail.
