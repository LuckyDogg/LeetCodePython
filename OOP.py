class Foo(object):

    def __new__(cls, *agrs, **kwds):
        inst = object.__new__(cls, *agrs, **kwds)
        print(inst)
        return inst

    def __init__(self, price=50):
        self.price = price

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

foo = Foo()
print(foo.how_much_of_book(8))