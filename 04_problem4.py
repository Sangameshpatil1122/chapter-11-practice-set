class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self ,c2):
        return complex(self.real + c2.real, self.imag + c2.imag)

    def __str__(self):
        return f"sum is {self.real} + {self.imag}i"
    
    
c1=complex(2,3)
c2=complex(4,5)
c3=c1+c2
print(f"the sum of complex number is : {c3}")