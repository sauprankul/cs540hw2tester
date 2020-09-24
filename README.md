# cs540hw2tester
This is a public tester for UW Madison's CS540's HW2. The program name is funny_puzzle.py.

### Test 1 (Saurabh's)
How to run:
1. download / `git clone` the repo
2. `python3 -m pip install numpy` (skip if you have)
3. `python3 test.py`

If your output matches mine, you'll only see the following line:

"If this is all you see, your code is good."

Otherwise, you'll see something like this:

Yours: Max queue length: 367
Ref:   Max queue length: 366

Note: This program will generate a file called test.txt. Deleting or modifying
it will not affect the operation of the tester.

I'm on discord as -smashndash- if you want to contact me. 

BTW don't worry about the license or whatever. I just picked that
because github forced me to. I don't care who gets a copy of this or
uses this in their program.

### Test 2 (Benjamin)
How to run:
1. download / `git clone` the repo
2. python3 test2.py

Will generate 10 random test cases of `depth` 10 every time you run, and perform two checks, an equality and length check.

* Equality: is your solution the same as the generated test case?
* Length: is your solution less than or equal to the length of the test case?

test cases are generated by starting from the `goal` state, and enumrating successors smartly.

Note: equality checks can occasionally fail as the generated test case may not be the optimal solution, or there may be many optimal solutions to a generated test case, however the length check should never fail.  An equality check failing is a sign of code smell (may require further investigation), a length check failing is an incorrect answer.

Honestly read the code in more detail if youre interested in how this works.
