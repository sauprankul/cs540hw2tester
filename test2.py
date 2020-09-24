from io import StringIO
import random, sys
from funny_puzzle import *

#helper dicts
__START = [((i+1) % 9) for i in range(9)]
__TRANS_2D = {(x, y): (x + y*3) for x in range(3) for y in range(3)}
__TRANS_1D = {(x + y*3): (x, y) for x in range(3) for y in range(3)}

"""
generate successors given a list of states
"""
def gen_succ(state):
    succ = []
    hs = []

    #first we find that 0 because we only need to concern oursleves with surrounding pieces
    pos = state.index(0)
    pos_x, pos_y = __TRANS_1D[pos]

    #generate list of surrounding states to check
    s = [pos_x - 1 if pos_x > 0 else None, pos_x + 1 if pos_x < 2 else None, pos_y - 1 if pos_y > 0 else None, pos_y + 1 if pos_y < 2 else None]
    s_x = s[0:2]
    s_y = s[2:]

    #check surrounding states, code replicated for x and y axes
    for i in range(2):
        #x axes
        state_copy = state.copy()
        if s_y[i] != None:
            #swap position of 0 and tile
            p = __TRANS_2D[(pos_x, s_y[i])]
            state_copy[pos] = state_copy[p]
            state_copy[p] = 0

            #calculate heuristic of new state
            h = 0
            for j in range(9):
                if state_copy[j] != 0:
                    h += manhattan_distance(j, state_copy[j] - 1)

            succ.append(state_copy)
            hs.append(h)

        #y axes
        state_copy = state.copy()
        if s_x[i] != None:
            #swap position of 0 and tile
            p = __TRANS_2D[(s_x[i], pos_y)]
            state_copy[pos] = state_copy[p]
            state_copy[p] = 0

            #calculate heuristic of new state
            h = 0
            for j in range(9):
                if state_copy[j] != 0:
                    h += manhattan_distance(j, state_copy[j] - 1)

            succ.append(state_copy)
            hs.append(h)

    return (succ, hs)

"""
generate a test case input `depth` moves from the goal state

the general algorithm is to start from the goal state and enumerate successor states
randomly greeding on one as the next state in the "scrambled" version of the puzzle.

this doesnt always ensure generating a good scrambled state, so we constrain that we
cannot generate an already visited state, and require our randomly selected state to
have a higher heuristic cost than our previous state.

The algorithm is more likely now to generate a state "further" away from the goal, 
however, it may not always be successful in doing so. We add a final struggle mechanic 
where after a certain threshold of iterations if the algorithm is not able to find a 
viable successor state, randomly select one of the current successors regardless of 
if the state conditions are not ideal.
"""
def gen_input(depth):
    __DEPTH = depth
    __PATH = [(__START, 0, __DEPTH)]
    __CLOSED = { tuple(__START): (0, __DEPTH) }
    succ, hs = gen_succ(__START)
    s = list(zip(succ, hs))
    h = 0
    prev_h = -1

    c = __START
    for i in range(1, __DEPTH + 1):
        #choose a random state (with a larger h) we havent been to before (no repeated states)
        #struggle if not able to find a successor
        tries = 0
        while tuple(c) in __CLOSED or h < prev_h:
            c, h = random.choice(s)
            if tries > 9:
                break

            tries += 1

        #add our random state to set of closed states and path
        __CLOSED[tuple(c)] = (h, __DEPTH - i)
        __PATH.append((c, h, __DEPTH - i))

        #find new successors
        succ, hs = gen_succ(c)
        s = list(zip(succ, hs))

        prev_h = h

    return (__PATH[-1], __PATH[::-1])

"""
Generate a random test case that is `depth` steps away from the goal

returns: (src_val, test_val)
src_val: generated test case
test_val: generated solution based on test case input

known bugs: test case may not be optimal solution leading to the test case failing when it shouldnt
    thats why two checks are in place one for equality and one to ensure the running program generated
    an input of length less than or equal to the test case.
"""
def test(depth):
    old_stdout = sys.stdout
    src_val, test_val = None, None
    with StringIO() as buf:
        sys.stdout = buf

        __INPUT, __PATH = gen_input(depth)
        solve(__INPUT[0])

        test_val = buf.getvalue()
        test_val = test_val.split("\n")
        while "" in test_val:
            test_val.remove("")
        if "queue length" in test_val[-1]:
            test_val.pop()
        
        b = ""
        for v in test_val:
            b += v + "\n"

        test_val = b

    with StringIO() as buf:
        sys.stdout = buf

        for n in __PATH:
            #print ("---" * 20)
            #print(str(n[0][0:3]) + "\n" + str(n[0][3:6]) + "\n" + str(n[0][6:]))
            #print("\n")
            print(f"{n[0]} h={n[1]} moves: {n[2]}")

        src_val = buf.getvalue()

    sys.stdout = old_stdout
    return (src_val, test_val)

if __name__ == '__main__':
    for i in range(10):
        print("===" * 20)
        src_val, test_val = test(10)
        print(src_val)
        print("===" * 20)
        print(test_val)
        print(f"Equality Test: {src_val == test_val}")
        print(f"Length Test: {len(test_val) <= len(src_val)}")
