class Person:
    def __init__(self, *args):
        self.name, self.age = args

    def sayhello(self):
        print('hello, %s, the age is %s' % (self.name, self.age))


p1 = Person("karl", 20)
p1.sayhello()
