C = input("Enter the real and the imaginary parts of the first complex number separated by a space: ")
D = input("Enter the real and the imaginary parts of the second complex number separated by a space: ")

C_real, C_imag = map(float, C.split())
D_real, D_imag = map(float, D.split())

class Complex_Numbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex_Numbers):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex_Numbers(real, imag)
        
    def __sub__(self, other):
        if isinstance(other, Complex_Numbers):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex_Numbers(real, imag)
        
    def __mul__(self, other):
        if isinstance(other, Complex_Numbers):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex_Numbers(real, imag)
       
    def __truediv__(self, other):
        if isinstance(other, Complex_Numbers):
            real = (self.real * other.real + self.imag * other.imag) / (other.real**2 + other.imag**2)
            imag = (self.imag * other.real - self.real * other.imag) / (other.real**2 + other.imag**2)
            return Complex_Numbers(real, imag)
      
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def __repr__(self):
        if self.imag >= 0:
            return f"{self.real:.2f} + {self.imag:.2f}i"
        else:
            return f"{self.real:.2f} - {abs(self.imag):.2f}i"

C = Complex_Numbers(C_real, C_imag)
D = Complex_Numbers(D_real, D_imag)

add = C + D
sub = C - D
mul = C * D
div = C / D
mod_C = abs(C)
mod_D = abs(D)

if C_imag >= 0 and D_imag >= 0:
    print(f"First complex number: {C_real:.2f} + {C_imag:.2f}i")
    print(f"Second complex number: {D_real:.2f} + {D_imag:.2f}i")
elif C_imag >= 0 and D_imag < 0:
    print(f"First complex number: {C_real:.2f} + {C_imag:.2f}i")
    print(f"Second complex number: {D_real:.2f} - {abs(D_imag):.2f}i")
elif C_imag < 0 and D_imag >= 0:
    print(f"First complex number: {C_real:.2f} - {abs(C_imag):.2f}i")
    print(f"Second complex number: {D_real:.2f} + {D_imag:.2f}i")
else:
    print(f"First complex number: {C_real:.2f} - {abs(C_imag):.2f}i")
    print(f"Second complex number: {D_real:.2f} - {abs(D_imag):.2f}i")

print(f"{add}")
print(f"{sub}")
print(f"{mul}")
print(f"{div}")
print(f"{mod_C:.2f} + 0.00i")
print(f"{mod_D:.2f} + 0.00i")
