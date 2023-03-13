from solution import SOLUTION
import pickle
import sys


seed = int(sys.argv[1])
num = sys.argv[2]

if num == "all":
    i = 0
    while True:
        try:
            member = pickle.load(open(f"pickles/run{seed}_pickle{i}.pkl", "rb"))
            member.Start_Simulation("GUI", ampersand=False)
            i += 1
        except FileNotFoundError:
            break
else:
    try:
        num = int(num)
        member = pickle.load(open(f"pickles/run{seed}_pickle{num}.pkl", "rb"))
        member.Start_Simulation("GUI")
    except ValueError:
        print("ERROR: Invalid argv[2]!")
        print(f"Enter a number at the end of a \'pickles/run{seed}_pickle*.pkl\' file, or \'all\' to run all pickles.")
