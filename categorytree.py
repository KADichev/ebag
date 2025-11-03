
class CategoryTree:
    def __init__(self):
        self.myhash = {}
        self.root = None

    def moveCategoryToNewParent(self, child, parent):
        if not child in self.myhash or not child:
            print("Unknown category")
        elif child.parent is None:
            print("I refuse to move root node")
        else:
            old_parent = child.parent
            old_parent.remove(child)
            if parent:
                parent.children.append(child)
            # we are becoming new root!
            else:
                self.root = child
                child.children.append(parent)

    def addCategoryBelowParent(self, child, parent):
        if child.name == "":
            print("Category name can't be empty!")        
        if parent is None:
            if not self.root is None:
                print("Ambiguous use of insertion: Root already exists:", self.root.name, " but no parent given.")
            else:
                self.root = child
                self.myhash[child.name] = child
        elif not parent.name in self.myhash:
            print("The parent does not exist, no insertion")
        elif child.name in self.myhash:
            print("The category already exists in the tree")
        else:            
            parent.children.append(child)
            child.parent = parent
            self.myhash[child.name] = child

    def getCategoriesByParent(self, node):
        successors = []
        if node is None:
            node = self.root

        if node is None:
            return []
        else:
            successors.append(node)
            for ch in node.children:                
                tmp = self.getCategoriesByParent(ch)
                successors += tmp
            return successors

    def getAllCategories(self):
        return self.getCategoriesByParent(None)

    def removeCategory(self, category):
        if not category.name in self.myhash:
            print("The category does not exist, no deletion")
        else:
            if category.parent:
                category.parent.children.remove(category)
                category.parent.children += category.children
                del self.myhash[category.name]
            else:
                print("Refuse to delete category, root category!")

    def getCategoryByName(self, name):
        return self.myhash[name]

    def updateCategory(self, old, new):
        if not old.name in self.myhash:
            print("Old category does not exist")
        else:
            del self.myhash[old.name]
            old.update(new)
            self.myhash[old.name] = old # new values
            
