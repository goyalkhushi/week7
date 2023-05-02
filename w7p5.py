def prime(n):
    count = 0
    i=2
    while i<n:
        if n%i==0:
            count+=1
    if count == 0:
        print("Prime")
    else: 
        print("Composite")
    i+=1
num  = int(input("Enter number: "))
print(prime(num))