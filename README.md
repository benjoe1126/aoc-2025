# AOC-2025 solutions

This is a personal repo containing my solutions for advent-of-code 2025.

## Day 1
<p align="left">
<img src="https://skillicons.dev/icons?i=elixir" />
</p>

### Part One: 
  The first subtask was quite simple, even though it required some utility to get going.  
  After creating the functions seen in the AocUtility module, the solution was as follows:
  - create a function `Solution.PartOne.solve` that took in a list of rotations (having made them negative if rotation is to the left, and positive otherwise), current position and an accumulator
  - if the list is empty, return the accumulator
  - if the position is zero, recursively call itself with the accumulator argument being incremented
  - if it is not empty and not zero, then do the rotation and recursively call itself
  - call the solve function with position set to 50 and accumulator set to 0
  
### Part Two: 
  The second subtask was in many ways similar, the differences are the following:
  - there is no solve matching the zero position explicitly
  - `Solution.PartTwo.times_zero_hit` function is created, which calculates how many zero hits there were (rotation/100 truncated + 1 if overrotated to either side or we hit a zero)
  - accumulator is always incremented by `times_zero_hit`

## Day 2
<p align="left">
<img src="https://skillicons.dev/icons?i=perl" />
</p>

### Part One: 
  The solution uses the followin prolog predicates:
  - `split_middle/3` -> given a string generates two stringes which is the original split in the middle if possible
  - `list_digits/2` -> from the first parameter creates a list contining each digit of the first param (number)
  - `collect_same_halves/2` -> given a list (input, list of K-V-s) collects all numbers between K and V where split_middle works and the two strings are the same
  - `sum_same_halves/2` -> given a list (same format) uses findall to get all numbers where collect_same_halves is applicable and sums the list it generated
  
### Part Two: 
  Almost same philosophy as before, but now uses `append/3` to generate all sublists of `list_digits/2`, and then uses `repeated_n_times/3` to check if the list from append n times repeated is the original list
  

## Day 3
<p align="left">
<img src="https://skillicons.dev/icons?i=cpp" />
</p>

### Part One: 
  The first part had a greedy solution with the following pricnciples:
  - function `max_to_jigs` finds the greatest number that either is the greatest in the sequence or the greatest where there will be other numbers after, else it own't be 2 digits
  - also find the second greatest number, without prejudice
  - return the found pair of number
  
### Part Two: 
  The solution in principle is the exact same, only difference is that instead of making a special case for the last number, we have to check each time if the number is greater than the current one.  
  A check is also made if there are still enough digits to make it 12 digits
  

## Day 4
<p align="left">
<img src="https://skillicons.dev/icons?i=go" />
</p>

### Part One: 
  The solution is very much trivial, after reading the file into a slice of strings, the following operations are performed:
  - call `countadjacentRollsFunc` passing in the slice, this returns a func that using the variable `adjacentMatrix` iterates over possible positions and if they are within bounds, checks if a roll is there
  - at the end of the call, we have calculated the amount of adjacent roles, for part 1 we just add one to variable `count` each time the function returns less than 4
  
### Part Two: 
  Same solution as part one, only now we iterate "indefinetly", each iteration if we found a valid roll we count it up and replace it with an arbitrary character  
  Repeat until no changes were made, i.e after iterating over the slice no roll with less than 4 adjacent neighbors is found
  

## Day 5
<p align="left">
<img src="https://skillicons.dev/icons?i=rust" />
</p>

### Part One: 
  Simply iterate over the ingredient ID-s and check if it fits into any range
  
### Part Two: 
  Create a new vector containing an interval endpoint (+ 1 if it is the end) and +/-1 depending if it is a start(+) or end(-) of an interval.  
  Sort this new vector by the first element of the tuple (endpoint).  
  After that, iterate over the list, always adding the +/- 1 to variable `sweep`.  
  If the sweep decreases that means an interval ended, adding the end of the current interval - the start of the previous interval to the sum, also changing the last start point to the current endpoint.
  

## Day 6
<p align="left">
<img src="https://skillicons.dev/icons?i=cs" />
</p>

### Part One: 
  Read in the file, create an Equation class for each column with operation being the symbol of the last line and same column.  
  After reading the input, call `Solve` on each equation and aggregate the results (`Solve` itself aggregates each element based on the operation)
  
### Part Two: 
  Same method, reading is different, read through each column of each line and create a number from them (using modulo 10 each time to get last digit)
  

## Day 7
<p align="left">
<img src="https://skillicons.dev/icons?i=kotlin" />
</p>

### Part One: 
  Create a set of current positions, and for each iteration if any of those positions encounters a split increment `count` by one, also create a new set with the new head poistions
  
### Part Two: 
  Dynamic programming solution, with the following process:
  - the first line of the dynamic table is filled with 0 except for where 'S' is, there it is one
  - for each line give current positions (same as before) the amount of timelines (possible ways to get to a point) at a given position is the sum of its top three (2 diagonal + above) timelines count given we could get to that position from those position
  - the final number of timelines is the sum of possible timelines in the last row
  

## Day 8
<p align="left">
<img src="https://skillicons.dev/icons?i=java" />
</p>

### Part One: 
  Senju no hate. Todokazaru yami no mite, utsurazaru ten no ite.  
  Hikari o otosu michi, hidane o aoru kaze, tsudoite madō na, waga yubi o miyo.  
  Kōdan, hasshin, kujō, tenkei, shippō, tairin, haiiro no hōtō.  
  Yumihiku kanata, kōkō toshite kiyu.
  
### Part Two: 
  Nijimidasu kondaku no monshō. Fusonnaru kyōki no utsuwa.  
  Waki agari, hitei shi, shibire, matataki, nemuri o samatageru.  
  Hakōsuru tetsu no ōjo. Taezu jikaisuru doro no ningyō.   
  Ketsugōseyo, hanpatsuseyo. Chi ni michi onore no muryoku o shire
  

## Day 9
<p align="left">
<img src="https://skillicons.dev/icons?i=javascript" />
</p>

### Part One: 
  Part one is written in vanilla js, simply check for every point pair if their distance (area of rectangle) is the greatest.
  
### Part Two: 
  I cheated. Using python shapely it is algorithmically easy to find a solution.  
  My original js solution was too slow, but it used a few tricks and techniques:
  - ray-casting with open-closed line segments to check if point is inside the polygon
  - memoization to not doublecheck any point
  - interval trimming, because of the shape of the actual input you only need to iterate over one semicircle to find the solution (actually used in the python code)
  There are algorythms making it faster, maybe checking it out later (probably wont)
  

## Day 10
<p align="left">
<img src="https://skillicons.dev/icons?i=python" />
</p>

### Part One: 
  Simple brute force algorythm, represent each button and the goal state as a binary number,  
  try pressing every button (xor with the possible previous states) and once we find the end state that is our solution (that is the number of presses happening)
  
### Part Two: 
  The secret ingredient is crime.  
  Used numpy and scipy to solve linear equation system created by circuits and the joltage.
  Formally:
  - A := matrix where a<sub>i,j</sub> is the ith buttons contribution to joltage j
  - b := the vector of joltages
  - x := the vector of coefficients we are looking for  
  
  After constructing the matrices we just use `scipy.optimize.milp` to solve the euqation (getting smallest integer solutions to the system of equations)
  

## Day 11
<p align="left">
<img src="https://skillicons.dev/icons?i=python" />
</p>

### Part One: 
  Given the graph from the input, create a canonical order and an adjecency list from that.  
  After that use DP to find the number of paths to each node (sum of number of nodes that preceed the given node).   
  Once done, return the last element of this list.
  
### Part Two: 
  Same as before, but instead of calculating from a -> b I calculate  a -> b -> c -> d and multiply each result  
  (a -> b) * (b -> c) * (c -> d)
  

## Day 12
<p align="left">
<img src="https://skillicons.dev/icons?i=python" />
</p>

### Part One: 
  I was literally trying to do some complex logic with fitting algorythm (worked) and adding backtracking to test all possible ways.  
  Turns out you can just be braindead, see if the sum of the areas of blocks are greater than the size of the grid.  
  I literally screamed when this turned out to be the case. I wasted an entire hour on this. Why?
  
### Part Two: 
  No part two, finish day 9
  
