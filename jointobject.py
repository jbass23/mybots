class JOINT:
    def __init__(self, parentID, childID, position, jointAxis):
        self.name = f"Link{parentID}_Link{childID}"
        self.parent = f"Link{parentID}"
        self.child = f"Link{childID}"
        self.position = position
        self.jointAxis = jointAxis
