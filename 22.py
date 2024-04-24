number = int(input("Enter a number : "))

even_number = 0
odd_number = 0

for i in range(1,number+1):
    if i%2==0:
        even_number +=i
    else:
        odd_number +=i

print(odd_number)
print(even_number)