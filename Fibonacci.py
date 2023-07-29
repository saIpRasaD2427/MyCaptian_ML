n = int(input("Enter the number of numbers to be printed: "))
first = 0
second = 1
l = [0,1]
for i in range(1,n):
    third = first + second
    first = second
    second = third
    l.append(third)
print(l)

    
