boy= float(input("Boy (m) : "))
kilo = float(input("Kilo (kg) :"))
vki = float(kilo/(boy*boy))

if(vki<18):
    print("Zayıf : ",vki)
elif(vki>=18 and vki<=25):
    print("normal : ",vki)
elif(vki>=18 and vki<=25):
    print("normal : ",vki)
elif(vki>=25 and vki<=30):
    print("kilolu : ",vki)
elif(vki>=30 and vki<=40):
    print("obez : ",vki)
else:
    print("Geçersiz değer")
