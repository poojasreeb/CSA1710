% Medical Diagnosis System

diagnose(flu) :-
    fever,
    cough,
    body_pain,
    fatigue.

diagnose(common_cold) :-
    cough,
    sneezing,
    runny_nose.

diagnose(malaria) :-
    fever,
    chills,
    sweating,
    headache.

diagnose(typhoid) :-
    fever,
    headache,
    stomach_pain,
    weakness.

% Symptoms
fever.
cough.
body_pain.
fatigue.
sneezing.
runny_nose.
chills.
sweating.
headache.
stomach_pain.
weakness.
