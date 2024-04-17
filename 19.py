sayi1 = int(input("1. Sayı : "))
sayi2 = int(input("2. Sayı : "))
Total = 0
if(sayi1>sayi2):
    while sayi1>sayi2+1:
        Total += sayi2+1
        sayi2 +=1
    else:
        print(Total)
elif(sayi2>sayi1):
    while sayi2>sayi1+1:
        Total += sayi1+1
        sayi1 +=1
    else:
        print(Total)
else:
    print("Bu iki sayı eşittir")