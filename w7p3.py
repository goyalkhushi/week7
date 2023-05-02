#swapping using call by reference function

def swap(x, y):
    a = x
    x=y
    y = a
    return x,y
a = 1
b = 3
print(swap(a, b))

#swapping using call by value function

def swapv(x, y):
    a = x
    x = y
    y = a
    print(x, y)