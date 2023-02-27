import copy

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
            relJointPos = np.subtract(absJointPos, self.links[parentID].absJointPos)

            self.joints.append(jointobject.JOINT(parentID, self.linkID, relJointPos))
            self.Create_Link(xyz, direction, absJointPos)

            if self.links[self.linkID - 1].aabb[2][0] >= 0 and self.links[self.linkID - 1].aabb[2][1] <= 4 and \
                    not self.Detect_Collision(self.linkID - 1, self.links):
                break
            else:
                self.joints.pop()
                self.links.pop()
                self.linkID -= 1

    def Detect_Collision(self, linkID, links):
        for i in range(len(links)):
            if i == linkID:
                continue

            if links[i].aabb[0][0] < links[linkID].aabb[0][1]:
                if links[i].aabb[0][1] > links[linkID].aabb[0][0]:
                    if links[i].aabb[1][0] < links[linkID].aabb[1][1]:
                        if links[i].aabb[1][1] > links[linkID].aabb[1][0]:
                            if links[i].aabb[2][0] < links[linkID].aabb[2][1]:
                                if links[i].aabb[2][1] > links[linkID].aabb[2][0]:
                                    return True

        return False

    def Mutate_Link_Size(self, linkID, xyz):
        mutated = False
        for _ in range(5):
            # copy the lists of links and joints
            linksCopy = copy.deepcopy(self.links)
            jointsCopy = copy.deepcopy(self.joints)

            # change the size of the link
            # xyz = np.random.randint(3)
            newLength = np.random.rand() * 1.25 + 0.25
            oldLength = linksCopy[linkID].size[xyz]
            linksCopy[linkID].size[xyz] = newLength

            # change the relative position of the link (only if it is already moving in the direction of the change)
            if linkID != 0 and linksCopy[linkID].pos[xyz] != 0:
                if linksCopy[linkID].pos[xyz] < 0:
                    linksCopy[linkID].pos[xyz] = newLength / -2
                else:
                    linksCopy[linkID].pos[xyz] = newLength / 2

            # change the relative positions of joints off that link
            for joint in jointsCopy:
                if joint.parentID == linkID:
                    if joint.position[xyz] != 0:
                        # at this point, we know we must change the joint.position
                        if joint.position[xyz] < 0:
                            if joint.position[xyz] == -1 * oldLength:
                                joint.position[xyz] = -1 * newLength
                            else:
                                joint.position[xyz] = newLength / -2
                        else:
                            if joint.position[xyz] == oldLength:
                                joint.position[xyz] = newLength
                            else:
                                joint.position[xyz] = newLength / 2

            # recalculate for absolute position and aabb for entire body
            self.Calculate_All_Absolute_Positions(linksCopy, jointsCopy)

            # check for collisions: if collision, restart with new size, if not, implement
            collided = False
            for i in range(len(linksCopy)):
                if linksCopy[i].aabb[2][0] < 0 or linksCopy[i].aabb[2][1] > 4 or self.Detect_Collision(i, linksCopy):
                    collided = True
                    break

            if collided:
                continue

            self.links = copy.deepcopy(linksCopy)
            self.joints = copy.deepcopy(jointsCopy)
            mutated = True
            break

        return mutated


    def Calculate_All_Absolute_Positions(self, links, joints):
        for i in range(len(links)):
            if i == 0:
                links[i].absJointPos = [0, 0, 0]
            else:
                upstreamLink = joints[i-1].parentID
                links[i].absJointPos = links[upstreamLink].absJointPos + joints[i-1].position

            links[i].absolutePosition, links[i].aabb = links[i].Compute_Dimensions()
