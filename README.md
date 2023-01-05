# Cow Allocator
#### Created by Braden Piper, bradenpiper.com
#### Created on Wed Jan 4, 2023
#### Version = 1.1
---
## DESCRIPTION
A program that uses a greedy algorithm and a brute force algorithm to solve a
knapsack problem, and compares the timeliness of each algorithm.

Backstory
A colony of Aucks (super-intelligent alien bioengineers) has landed on Earth 
and has created new species of farm animals! The Aucks are performing their
experiments on Earth, and plan on transporting the mutant animals back to their
home planet of Aurock.
The aliens have succeeded in breeding cows that jump over the moon! Now they
want to take home their mutant cows. The aliens want to take all chosen cows
back, but their spaceship has a weight limit and they want to minimize the
number of trips they have to take across the universe. Somehow, the aliens
have developed breeding technology to make cows with only integer weights.

The data for the cows to be transported is stored in cow_data.txt.

You can expect the data to be formatted in pairs of x,y on each line, where x 
is the name of the cow and y is a number indicating how much the cow weighs in
tons, and that all of the cows have unique names.
---
##### NOTE:
This program was completed as part of the course MITx 6.00.2x - Introduction
to Computational Thinking and Data Science. The general framework, and some
of the functions were provided materials. The majority of the implementation is
my own work.
The provided functions include:
- `load_cows()`
The following function names were provided with docstrings, but the implementations
are my own work:
- `greedy_cow_transport()`
- `brute_force_cow_transport()`
- `compare_cow_transport_algorithms()`