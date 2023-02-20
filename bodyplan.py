import constants as c
import linkobject
import jointobject
import numpy as np


class BODY_PLAN:
    def __init__(self):
        self.links = []
        self.joints = []
        self.linkID = 0
        self.sensorBoolArray = np.random.randint(2, size=c.numSensorNeurons)

    def Create_First_Link(self):
        pos = [0, 0, 1]
        baseSize = np.random.rand(3) * 1.25 + 0.25
        self.links.append(linkobject.LINK(self.linkID, pos, baseSize, self.sensorBoolArray[self.linkID] == 1))
