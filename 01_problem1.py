class twodvector:
    def __init__(self , i , j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the vector is ({self.i}i, {self.j}j)")

class threedvector(twodvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"the vector is ({self.i}i, {self.j}j, {self.k}k)")

a=threedvector(1, 2, 3)
a.show()
b=twodvector(4, 5)
b.show()