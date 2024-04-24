sayi = input('Bir sayı giriniz: ')
sayac = 0
for i in range(2,int(sayi)):
  if(int(sayi)%i==0):
    sayac+=1
    break
if(sayac!=0):
  print("Bu sayı asal Değildir")
else:
  print("Bu sayı asaldır.")
    