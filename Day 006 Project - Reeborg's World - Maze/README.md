# Lost in a maze

Reeborg was exploring a dark maze and the battery in its flashlight ran out.
Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

What you need to know

- The functions `move()` and `turn_left()`.
- Either the test `front_is_clear()` or `wall_in_front()`, `right_is_clear()` or `wall_on_right()`, and `at_goal()`.
- How to use a while loop and `if/elif/else` statements.
- It might be useful to know how to use the negation of a test (not in Python).

Link to the problem: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Also make sure to debug the infinte loop issue and provide solution for that. The issue can be reproduced by loading `problem_word.json`, `problem_word2.json` and `problem_word3.json` from the Reeborg World Tests folder.

# Reeborgs_word
Check out my [Reeborgs_world_solutions](https://github.com/ashutosh-vaidya/Reeborgs_world_solutions) to many different Reeborg's world challenges.
