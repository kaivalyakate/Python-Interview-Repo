from typing import TypeVar


A_type = TypeVar('A_type')


class A:

    def pt(self):
        print("A")


class B(A):

    def pt(self):
        print("B")


def ptx(obj: A) -> A_type:
    return B()


if __name__ == "__main__":
    a = A()
    b = ptx(a)
    b.pt()