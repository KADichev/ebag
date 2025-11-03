import numpy as np
class Similarity:
    def __init__(self):
        self.mat = np.zeros((0,0), dtype=np.int32)
        self.categories = set()
        self.cat2ind = {}
        self.ind2cat = {}

    def addCategory(self, c):
        if not c in self.categories:
            matSize = self.mat.shape[0]
            # add a row
            row=np.zeros((matSize,1))
            self.mat = np.append(self.mat, row, axis=1)
            # add a column
            col=np.zeros((1,matSize+1), dtype=np.int32)
            self.mat = np.append(self.mat, col, axis=0)
            self.mat[matSize, matSize] = 1 #self-similarity is always true
            self.categories.add(c)
            self.cat2ind[c] = matSize
            self.ind2cat[matSize] = c

    def addSimilar(self, n1, n2):
        # are the categories new?
        # if yes, extend matrix
        for i in n1,n2:
            self.addCategory(i)
        self.mat[self.cat2ind[n1]][self.cat2ind[n2]] = 1
        self.mat[self.cat2ind[n2]][self.cat2ind[n1]] = 1

    def removeSimilar(self, n1, n2):
        if n1 in self.categories and n2 in self.categories:
            self.mat[self.cat2ind[n1]][self.cat2ind[n2]] = 0
            self.mat[self.cat2ind[n2]][self.cat2ind[n1]] = 0
        else:
            print("At least one category not known")

    def isSimilar(self, n1, n2):
        if n1 in self.categories and n2 in self.categories:
            return self.mat[self.cat2ind[n1]][self.cat2ind[n2]] == 1
        else:
            return False
    # entry parameter is a category to begin with
    # from this category, follow all similarities and
    # return a pair: <steps, list of categories>
    # steps: number of times a jump between similar categories
    # was made
    # list of categories: the rabbit island
    def getRabbitHole(self, entry):
        cat_list = [entry]
        matLen = self.mat.shape[0]
        tmp = np.zeros((matLen,matLen),dtype=np.int32)
        # the only starting point is the input category
        # everything else is derived from the matrix multiply
        tmp[self.cat2ind[entry]][self.cat2ind[entry]] = 1
        steps = 0
        for i in range(matLen):
            #convert int matrix to boolean matrix
            tmp2 = tmp > 0
            # multiply current matrix by self.mat
            # which corrensponds to "one further step
            # in each direction"
            # EXPENSIVE ~O(n^3)
            tmp3 = np.matmul(tmp, self.mat) > 0
            # tmp4 holds the diff, i.e. the extension
            # of the matrix within the last step
            tmp4 = np.logical_xor(tmp3, tmp2)
            nz_indices = np.nonzero(tmp4)
            for ind in nz_indices:
                if len(ind) > 0:
                    for k in ind:
                        new_cat = self.ind2cat[k]
                        if new_cat not in cat_list:
                            cat_list.append(new_cat)
            tmp[nz_indices] = 1
            # it one step did not lead to extended reach,
            # the islands are complete
            if len(nz_indices[0]) == 0:
                break
            else:
                steps += 1
        return steps, cat_list

