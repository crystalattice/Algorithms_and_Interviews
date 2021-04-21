class A:
    def class_method(self):
        print("class_method of A called")


class B(A):
    def class_method(self):
        print("class_method of B called")
        super().class_method()


class C(A):
    def class_method(self):
        print("class_method of C called")
        super().class_method()


class D(B, C):
    def class_method(self):
        print("class_method of D called")
        super().class_method()


if __name__ == "__main__":
    inst1 = D()
    inst1.class_method()
