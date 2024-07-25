% Facts defining the color of different fruits
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(lemon, yellow).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).
fruit_color(kiwi, green).
fruit_color(watermelon, green).

% Query to find the color of a specific fruit
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Query to find all fruits of a specific color
fruits_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
