% Facts: planet(Name, Diameter_km, Distance_from_Sun_million_km, Has_moons)
planet(mercury, 4879, 57.9, false).
planet(venus, 12104, 108.2, false).
planet(earth, 12742, 149.6, true).
planet(mars, 6779, 227.9, true).
planet(jupiter, 139820, 778.3, true).
planet(saturn, 116460, 1427.0, true).
planet(uranus, 50724, 2871.0, true).
planet(neptune, 49244, 4497.0, true).

% Query to find information about a planet by name
planet_info(Name, Diameter, Distance, HasMoons) :-
    planet(Name, Diameter, Distance, HasMoons).

% Query to find all planets with moons
planets_with_moons(Name) :-
    planet(Name, _, _, true).

% Query to find all planets in a specific distance range from the Sun
planets_in_distance_range(MinDistance, MaxDistance, Name) :-
    planet(Name, _, Distance, _),
    Distance >= MinDistance,
    Distance =< MaxDistance.

% Query to find the planet with the largest diameter
largest_planet(Name, Diameter) :-
    findall(D, planet(_, D, _, _), Diameters),
    max_list(Diameters, MaxDiameter),
    planet(Name, MaxDiameter, _, _).

% Utility to print all entries in the database
print_db :-
    findall((Name, Diameter, Distance, HasMoons), planet(Name, Diameter, Distance, HasMoons), List),
    print_list(List).

% Helper predicate to print a list of tuples
print_list([]).
print_list([(Name, Diameter, Distance, HasMoons)|T]) :-
    write(Name), write(': Diameter = '), write(Diameter),
    write(' km, Distance from Sun = '), write(Distance),
    write(' million km, Has moons = '), write(HasMoons), nl,
    print_list(T).

% Example queries
start :-
    % Find information about Earth
    planet_info(earth, Diameter1, Distance1, HasMoons1),
    write('Earth: Diameter = '), write(Diameter1),
    write(' km, Distance from Sun = '), write(Distance1),
    write(' million km, Has moons = '), write(HasMoons1), nl,

    % Find all planets with moons
    write('Planets with moons: '), nl,
    planets_with_moons(Name1), write(Name1), nl, fail; true,

    % Find all planets in the distance range of 100 to 1500 million km from the Sun
    write('Planets in distance range 100 to 1500 million km: '), nl,
    planets_in_distance_range(100, 1500, Name2), write(Name2), nl, fail; true,

    % Find the planet with the largest diameter
    largest_planet(LargestName, LargestDiameter),
    write('Largest planet: '), write(LargestName),
    write(' with diameter = '), write(LargestDiameter), write(' km'), nl,

    % Print all entries in the database
    write('Database entries: '), nl,
    print_db.
