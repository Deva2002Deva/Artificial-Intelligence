% Facts defining symptoms for each disease
symptom(flu, fever).
symptom(flu, headache).
symptom(flu, chills).
symptom(flu, sore_throat).

symptom(common_cold, cough).
symptom(common_cold, sore_throat).
symptom(common_cold, runny_nose).
symptom(common_cold, sneezing).

symptom(covid_19, fever).
symptom(covid_19, cough).
symptom(covid_19, shortness_of_breath).
symptom(covid_19, loss_of_taste_or_smell).

symptom(allergy, sneezing).
symptom(allergy, runny_nose).
symptom(allergy, itchy_eyes).

% Rule to diagnose disease based on a list of symptoms
diagnose(Disease, Symptoms) :-
    findall(S, symptom(Disease, S), DiseaseSymptoms),
    subset(DiseaseSymptoms, Symptoms).

% Utility to check if a list is a subset of another list
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).

% Query to start the diagnosis
start_diagnosis :-
    write('Enter symptoms (end with a period):'), nl,
    read(Symptoms),
    findall(D, diagnose(D, Symptoms), Diagnoses),
    write('Possible diagnoses: '), write(Diagnoses), nl.
