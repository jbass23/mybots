import numpy as np


class LINK:
    def __init__(self, linkID, pos, absJointPos, size, isSensor):
        self.linkID = linkID
        self.name = f"Link{linkID}"
        self.pos = pos
        self.size = size
        self.absJointPos = absJointPos
        self.absolutePosition, self.aabb = self.Compute_Dimensions()
        if isSensor:
            self.rgba = '    <color rgba="0 1.0 0 1.0"/>'
            self.colorName = '<material name="Green">'
        else:
            self.rgba = '    <color rgba="0 0 1.0 1.0"/>'
            self.colorName = '<material name="Blue">'

    def Compute_Dimensions(self):
        if self.linkID == 0:
            absolutePosition = [0, 0, 2]
        else:
            posRelToJoint = np.copy(self.pos)
            for i in range(len(posRelToJoint)):
                if posRelToJoint[i] < 0:
                    posRelToJoint[i] = self.size[i] / -2
                elif posRelToJoint[i] > 0:
                    posRelToJoint[i] = self.size[i] / 2

            absolutePosition = np.add(self.absJointPos, posRelToJoint)
        aabb = [[absolutePosition[0] - self.size[0] / 2, absolutePosition[0] + self.size[0] / 2],
                [absolutePosition[1] - self.size[1] / 2, absolutePosition[1] + self.size[1] / 2],
                [absolutePosition[2] - self.size[2] / 2, absolutePosition[2] + self.size[2] / 2]]
        return absolutePosition, aabb

    def __str__(self):
        return f"LINK({self.name}: relative_pos={self.pos}, absolute_pos={self.absolutePosition}, size={self.size}\n" \
               f"     aabb={self.aabb},\n" \
               f"     color={self.colorName})"
