class A:
    def class_method(self):
        print("class_method of A called")


class B(A):
    def class_method(self):
        print("class_method of B called")
        A.class_method(self)


class C(A):
    def class_method(self):
        print("class_method of C called")
        A.class_method(self)


class D(B, C):
    def class_method(self):
        print("class_method of D called")
        B.class_method(self)
        C.class_method(self)
        

if __name__ == "__main__":
    inst1 = D()
    inst1.class_method()
