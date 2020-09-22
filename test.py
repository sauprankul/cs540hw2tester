from funny_puzzle import *
import sys
import time

if __name__ == '__main__':

    starttime = time.time()

    # this is necessary to print to file
    backup_stdout = sys.stdout
    sys.stdout = open('test.txt', 'w')

    # these are a bunch of random test cases
    solve([6, 4, 7, 8, 5, 0, 3, 2, 1])
    solve([8, 2, 7, 3, 1, 6, 4, 0, 5])
    solve([[6, 5, 7, 1, 8, 2, 3, 4, 0]])
    solve([8, 6, 5, 7, 1, 4, 0, 2, 3])
    solve([6, 4, 8, 2, 3, 5, 1, 7, 0])
    solve([7, 8, 6, 5, 4, 0, 2, 3, 1])
    solve([6, 5, 7, 4, 0, 2, 3, 1, 8])
    solve([3, 6, 2, 5, 8, 0, 4, 7, 1])

    print_succ([6, 4, 7, 8, 5, 0, 3, 2, 1])
    print_succ([8, 2, 7, 3, 1, 6, 4, 0, 5])
    print_succ([6, 5, 7, 1, 8, 2, 3, 4, 0])
    print_succ([8, 6, 5, 7, 1, 4, 0, 2, 3])
    print_succ([6, 4, 8, 2, 3, 5, 1, 7, 0])
    print_succ([7, 8, 6, 5, 4, 0, 2, 3, 1])
    print_succ([6, 5, 7, 4, 0, 2, 3, 1, 8])
    print_succ([3, 6, 2, 5, 8, 0, 4, 7, 1])

    # These are unsolvable
    #solve([7, 2, 8, 5, 0, 4, 3, 6, 1])
    #solve([1, 2, 3, 4, 0, 6, 7, 8, 5])
    #solve([8, 7, 5, 6, 0, 4, 3, 2, 1])



    # these are examples from the writeup
    print_succ([1, 2, 3, 4, 5, 0, 6, 7, 8])
    solve([4, 3, 8, 5, 1, 6, 7, 2, 0])
    print_succ([8, 7, 6, 5, 4, 3, 2, 1, 0])
    solve([1, 2, 3, 4, 5, 6, 7, 8, 0])
    solve([1, 2, 3, 4, 5, 6, 7, 0, 8])

    sys.stdout.close()
    sys.stdout = backup_stdout
    live = open('test.txt', 'r')
    ref = open('ref.txt', 'r')

    live_l = live.readlines()
    ref_l = ref.readlines()

    live.close()
    ref.close()

    for l, r in zip(live_l, ref_l):
        if not l == r:
            print("Yours: " + l.strip())
            print("Ref:   " + r)

    print("If the time below is all you see, your code is good.")

    endtime = time.time()
    print("Elapsed time was: " + str(endtime - starttime) + "s")
    print("Ref elapsed time: 3.1s")
