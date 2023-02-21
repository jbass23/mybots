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
        pos = [0, 0, 2]
        size = np.random.rand(3) * 1.25 + 0.25
        self.links.append(linkobject.LINK(self.linkID, pos, [0, 0, 0], size, self.sensorBoolArray[self.linkID] == 1))
        self.linkID += 1

    def Create_Link(self, xyz, direction, absJointPos):
        size = np.random.rand(3) * 1.25 + 0.25
        pos = [0, 0, 0]
        pos[xyz] = size[xyz] / 2 * direction
        self.links.append(linkobject.LINK(self.linkID, pos, absJointPos, size, self.sensorBoolArray[self.linkID] == 1))
        self.linkID += 1

    def Create_Joint_Then_Link(self):
        while True:
            parentID = np.random.randint(len(self.links))
            absLinkPos = self.links[parentID].absolutePosition
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

            absJointPos = np.add(absLinkPos, pos)
            print(absLinkPos)
            print(absJointPos)
            print(self.links[parentID].absJointPos)
            relJointPos = np.subtract(absJointPos, self.links[parentID].absJointPos)
            print(relJointPos)

            self.joints.append(jointobject.JOINT(parentID, self.linkID, relJointPos))
            self.Create_Link(xyz, direction, absJointPos)

            if self.links[self.linkID - 1].aabb[2][0] >= 0 and not self.Detect_Collision(self.linkID - 1):
                break
            else:
                self.joints.pop()
                self.links.pop()
                self.linkID -= 1

    def Detect_Collision(self, linkID):
        for i in range(len(self.links)):
            if i == linkID:
                continue

            if self.links[i].aabb[0][0] < self.links[linkID].aabb[0][1]:
                if self.links[i].aabb[0][1] > self.links[linkID].aabb[0][0]:
                    if self.links[i].aabb[1][0] < self.links[linkID].aabb[1][1]:
                        if self.links[i].aabb[1][1] > self.links[linkID].aabb[1][0]:
                            if self.links[i].aabb[2][0] < self.links[linkID].aabb[2][1]:
                                if self.links[i].aabb[2][1] > self.links[linkID].aabb[2][0]:
                                    return True

        return False