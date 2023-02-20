class LINK:
    def __init__(self, linkID, pos, size, isSensor):
        self.name = f"Link{linkID}"
        self.pos = pos
        self.size = size
        if isSensor:
            self.rgba = '    <color rgba="0 1.0 0 1.0"/>'
            self.colorName = '<material name="Green">'
        else:
            self.rgba = '    <color rgba="0 0 1.0 1.0"/>'
            self.colorName = '<material name="Blue">'

    def __str__(self):
        return f"LINK({self.name}: pos={self.pos}, size={self.size}, color={self.colorName})"
