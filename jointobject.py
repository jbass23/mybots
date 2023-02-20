class JOINT:
    def __init__(self, parentID, childID, position, jointAxis = "0 1 0"):
        self.name = f"Link{parentID}_Link{childID}"
        self.parent = f"Link{parentID}"
        self.child = f"Link{childID}"
        self.position = position
        self.jointAxis = jointAxis

    def __str__(self):
        return f"JOINT({self.name}: pos={self.position})"
