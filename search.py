from parallelhillclimber import PARALLEL_HILL_CLIMBER
import sys


fileNumber = int(sys.argv[1])

phc = PARALLEL_HILL_CLIMBER(fileNumber)
phc.Evolve()
phc.Save_Data(fileNumber)
input("Press Enter to continue...")
phc.Show_Best()
