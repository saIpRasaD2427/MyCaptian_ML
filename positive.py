lis1  = []
n = int(input("Enter the length of list"))
for i in range(n):
    lis1.append(int(input()))
positive_numbers = [num for num in lis1 if num > 0]
print(positive_numbers)
