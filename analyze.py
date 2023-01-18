import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
matplotlib.pyplot.plot(frontLegSensorValues, label="back leg", linewidth=3)
matplotlib.pyplot.plot(backLegSensorValues, label="front leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

targetAnglesBL = numpy.load("data/targetAnglesBL.npy")
targetAnglesFL = numpy.load("data/targetAnglesFL.npy")
matplotlib.pyplot.plot(targetAnglesBL, label="back leg", linewidth=3)
matplotlib.pyplot.plot(targetAnglesFL, label="front leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
