% Facts: disease(Disease, RecommendedDiet)
disease(diabetes, low_sugar).
disease(high_blood_pressure, low_sodium).
disease(obesity, low_calorie).
disease(high_cholesterol, low_fat).
disease(celiac_disease, gluten_free).
disease(lactose_intolerance, dairy_free).
disease(arthritis, anti_inflammatory).
disease(gout, low_purine).

% Query to suggest a dieting system based on a disease
suggest_diet(Disease, Diet) :-
    disease(Disease, Diet),
    write('For '), write(Disease), write(', the recommended diet is '), write(Diet), nl.

suggest_diet(Disease, _) :-
    \+ disease(Disease, _),
    write('No dietary suggestion available for '), write(Disease), nl.

% Utility to print all diseases and their recommended diets
print_diets :-
    findall((Disease, Diet), disease(Disease, Diet), List),
    print_list(List).

% Helper predicate to print a list of tuples
print_list([]).
print_list([(Disease, Diet)|T]) :-
    write(Disease), write(': '), write(Diet), nl,
    print_list(T).

% Example queries
start :-
    % Suggest diet for specific diseases
    write('Diet suggestions:'), nl,
    suggest_diet(diabetes, _),
    suggest_diet(high_blood_pressure, _),
    suggest_diet(gout, _),

    % Print all diseases and their recommended diets
    write('All diseases and their recommended diets:'), nl,
    print_diets.
