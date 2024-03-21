yas = int(input("Yaşınızı giriniz:"))

if(yas>=18):
    print("Ehliyet alabilirsiniz.")
elif(yas>0):
    print("Ehliyet alamazsınız.")
else:
    print("Geçersiz değer.")