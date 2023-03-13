from solution import SOLUTION
import pickle
import sys


seed = int(sys.argv[1])

i = 0
while True:
    try:
        member = pickle.load(open(f"pickles/run{seed}_pickle{i}.pkl", "rb"))
        member.Start_Simulation("GUI", ampersand=False)
        i += 1
    except FileNotFoundError:
        break
