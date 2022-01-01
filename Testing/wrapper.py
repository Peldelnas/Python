"""from math import *"""


def wrapper(f):
    def new_f(*n):
        print("wrapper")
        f(*n)
        print("wrapper")

    return new_f

@wrapper
def d(n, m):
    """Función test"""
    print("derog " + str(n) + str(m))


d(10, 15)