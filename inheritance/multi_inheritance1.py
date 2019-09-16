class A:
    def class_method(self):
        print("class_method of A called")


class B(A):
    def class_method(self):
        print("class_method of B called")


class C(A):
    def class_method(self):
        print("class_method of C called")


class D(B, C):
    def class_method(self):
        print("class_method of D called")


if __name__ == "__main__":
    inst1 = D()
    inst2 = C()
    inst3 = B()
    inst4 = A()
    inst1.class_method()
    inst2.class_method()
    inst3.class_method()
    inst4.class_method()
