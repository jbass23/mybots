from parallelhillclimber import PARALLEL_HILL_CLIMBER
import numpy as np
import sys


fileNumber = int(sys.argv[1])

np.random.seed(fileNumber)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Save_Data(fileNumber)
input("Press Enter to continue...")
phc.Show_Best()
