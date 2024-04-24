number = int(input("Enter a number : "))

odd_number = 0
even_number = 0

for i in range(1,number+1):
    if i%2==0:
        even_number +=i
    else:
        odd_number +=i

print("Tek sayıların toplamı : {0}".format(odd_number))
print("Çift sayıların toplamı : {0}".format(even_number))
