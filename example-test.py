import numpy as np
from categorynode import CategoryNode
from categorytree import CategoryTree
from similarity import Similarity

brown = CategoryNode("Brown")
green = CategoryNode("Green")
blue = CategoryNode("Blue")
red = CategoryNode("Red")
violet = CategoryNode("Violet")
darkred = CategoryNode("DarkRed")
orange = CategoryNode("Orange")
yellow = CategoryNode("Yellow")
white = CategoryNode("White")
black = CategoryNode("Black")
tree = CategoryTree()
tree.addCategoryBelowParent(white, None)
tree.addCategoryBelowParent(green, white)
tree.addCategoryBelowParent(brown, white)
tree.addCategoryBelowParent(red, white)
tree.addCategoryBelowParent(violet, white)
tree.addCategoryBelowParent(blue, white)
tree.addCategoryBelowParent(darkred, red)
tree.addCategoryBelowParent(orange, white)
tree.addCategoryBelowParent(yellow, white)
tree.addCategoryBelowParent(black, white)

green.description = "Newly added description of colour green, it is the nicest colour"
tree.updateCategory(green)


allColors = tree.getAllCategories()
sim = Similarity()
for i in allColors:
    sim.addCategory(i)

sim.addSimilar(green, red)
sim.addSimilar(red, blue)
sim.addSimilar(blue, violet)
sim.addSimilar(yellow,orange)
black = CategoryNode("Black", "Black colour description")

def printRabbitInfo(sim):
    processed_cats = set()
    tupleList = []
    for i in sim.categories:
        if not i in processed_cats:
            steps, cats = sim.getRabbitHole(i)
            tupleList.append((steps,cats))
            processed_cats |= set(cats)
    tupleList.sort(key=lambda tup: tup[0], reverse=True)
    print("Longest rabbit hole (", tupleList[0][0], " jumps required ):", end='')
    for i in tupleList[0][1]:
        print(i.name, end=' ')
    print("\n==Rabbit islands==")
    for ind, i in enumerate(tupleList):
        print("Island", ind, ':')
        for k in i[1]:
            print(k.name, end=' ')
        print('\t')
    
print("Colors:")
for i in allColors:
    print(i.name,end=' ')
print('')

for i in allColors:
    for j in allColors:
        if i != j and sim.isSimilar(i,j):
            print("similar:", i.name, j.name)
printRabbitInfo(sim)
    
