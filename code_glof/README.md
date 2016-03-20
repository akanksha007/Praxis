# code_golf
What is Code Golf?
Code-golf is a competition to solve a particular problem in the fewest bytes of source code.

Improvised Code Golf:
Code will be judged on execution time. Fastest Code Wins.

Problem Statement:

You are the owner of a restaurant. You are opening in a new area in Cartesia where there is only one main road, known as the y-axis. You want to place your restaurant such that you minimize the total distance from your restaurant and each of the houses in that area.

Input:

The input will be

n, the number of houses
house1
house2
house3
...
houseN

where each house is a coordinate in the form x y. Each unit represents one kilometer.

You can take input as a string or provide a function that takes the input, in whatever format you choose, as its arguments.

Output: The y-coordinate of your restaurant (remember, it will be located on the y-axis). Actually, it will be located on the side of the road, but the difference is negligible.

Essentially, if nth house is h_n and D is the distance function, then you want to find k such that D(h_0, (0, k)) + D(h_1, (0, k)) + D(h_2, (0, k)) + ... + D(h_n, (0, k)) is minimized.

Note that distance is calculated as though the customer travels in an exactly straight line from their house to the restaurant. That is the distance from (x, y) to your restaurant is sqrt(x^2 + (y - k)^2).

The output should be accurate to at least 2 decimal places.

Output can be printed as a string or can be returned from the function.

Example input/output:

Input:
2
5.7 3.2
8.9 8.1
Output:
5.113013698630137

The total distance in this example is about 15.4003 kilometers.

What languages to use?
python
