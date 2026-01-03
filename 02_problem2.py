class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
         print("bow bow!")
    
d=dog
d.bark()