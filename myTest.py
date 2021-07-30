t = (1, 2, 3)
p = {
    'a':12,
    'b':10,
    'c':20
}

def mydef(a, b, c):
    print(a + b + c)

mydef(**p)
