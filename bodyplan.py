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

    def Create_Blueprint(self):
        self.Create_Base_Link()
        for i in range(c.numLinks):
            self.Create_Joint_Then_Link()

        for i in self.links:
            print(i)
        for i in self.joints:
            print(i)
        return self.links, self.joints

    def Create_Base_Link(self):
        pos = [0, 0, 1]
        size = np.random.rand(3) * 1.25 + 0.25
        self.links.append(linkobject.LINK(self.linkID, pos, size, self.sensorBoolArray[self.linkID] == 1))
        self.linkID += 1

    def Create_Link(self, xyz, direction):
        size = np.random.rand(3) * 1.25 + 0.25
        pos = [0, 0, 0]
        pos[xyz] = size[xyz] / 2 * direction
        self.links.append(linkobject.LINK(self.linkID, pos, size, self.sensorBoolArray[self.linkID] == 1))
        self.linkID += 1

    def Create_Joint_Then_Link(self):
        parentID = np.random.randint(len(self.links))
        face = np.random.randint(6)
        if face == 0:
            pos = [self.links[parentID].size[0] / 2, 0, 0]
            xyz = 0
            direction = 1
        elif face == 1:
            pos = [self.links[parentID].size[0] / -2, 0, 0]
            xyz = 0
            direction = -1
        elif face == 2:
            pos = [0, self.links[parentID].size[1] / 2, 0]
            xyz = 1
            direction = 1
        elif face == 3:
            pos = [0, self.links[parentID].size[1] / -2, 0]
            xyz = 1
            direction = -1
        elif face == 4:
            pos = [0, 0, self.links[parentID].size[2] / 2]
            xyz = 2
            direction = 1
        else:
            pos = [0, 0, self.links[parentID].size[2] / -2]
            xyz = 2
            direction = -1

        self.joints.append(jointobject.JOINT(parentID, self.linkID, pos))
        self.Create_Link(xyz, direction)


bp = BODY_PLAN()
bp.Create_Blueprint()
