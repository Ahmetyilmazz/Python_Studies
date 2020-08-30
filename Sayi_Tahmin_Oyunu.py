
# Programmer : Ahmet YILMAZ

import random

print ("Sayi Tahmin Oyununa Hoşgeldiniz ! Lütfen 1-100 arasında bir sayi tahmin ediniz .")

sayi = random.randint(0,10)
sayi_tahmin_hakki = 5 

while 1:

    tahmin = int(input("Tahmininiz : "))

    if tahmin == sayi :
        print ("Tebrikler ! Random Sayi : " + str(sayi))
        break
    else:
        print ("Yanlış !!! Tekrar bir sayi giriniz : ")
        sayi_tahmin_hakki -= 1

    if sayi_tahmin_hakki == 0 :
        print ("Tahmin Hakkiniz Bitmistir, Bilgisayarin sectiği sayi : " + str(sayi))
        break