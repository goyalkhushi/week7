#function call by reference

def xyz(c):
    return c+3
x = 10
y = xyz(x)
print(y)