class CategoryNode:
    def __init__(self, name, description = None, image = None):
        self.name = name
        self.description = ""
        self.image = None
        if description:
            self.description = description
        if image:
            self.image = image
        self.children = []
        self.parent = None
    def update(self, new):
        self.name = new.name
        self.description = new.description
        self.image = new.image
