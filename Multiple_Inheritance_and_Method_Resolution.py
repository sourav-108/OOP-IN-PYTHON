class A:
    def describe(self):
        return "A"

class B(A):
    def describe(self):
        return "B" + super().describe()

class C(A):
    def describe(self):
        return "C" + super().describe()

class D(B, C):
    pass


print(D().describe())  # BCA