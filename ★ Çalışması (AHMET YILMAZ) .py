
# Programmer : Ahmet YILMAZ

print ("Bu Program sizden aldığı boyuta göre alt alta olacak şekilde 'AHMET' yazdırır.")

boyut = int(input("Boyutu Giriniz : "))

print ("\n")

# A harfi 
for i in range(boyut) :
    for j in range(boyut) :
        if i == 0 : # İlk satırda mıyız ?
            if (j == 0) | (j == (boyut - 1)) : # İlk ve son stündaki boşluklar.
                print (' ', end="")
            else :
                print ('★', end="")
        elif i == int(boyut/2) : # A'nın orta çizgisine geldiysek..
            print ('★', end="") # i boyut/2 iken j döngü sayısı kadar ★ yazıcak.
        else :
            if (j == 0) | (j == (boyut - 1)) :  # İlk ve son stündaki yıldızlar.
                print ('★', end="")
            else :
                print (' ', end="")
    print("\n", end="")

print ("\n")

# H harfi 
for i in range(boyut) :
    for j in range(boyut) :
        if i == 0 : # İlk satirda miyiz ? 
            if (j == 0 ) | (j == (boyut - 1)) : # İlk ve son stündaki ★lar.
                print ('★', end="")
            else :
                print (' ', end="")
        elif i == int (boyut/2) : # H'ın orta çizgisine geldiysek..
            print ('★', end="")
        else :
            if (j == 0) | (j == boyut - 1) : # Diğer durumlardaki ilk ve son stündaki ★lar.
                print ('★', end="")
            else :
                print (' ', end="")
    print("\n", end="")

print ("\n")

# M harfi 
for i in range(boyut):
    for j in range(boyut):
        if (j == 0) | (j == (boyut - 1)) : # M'nin ilk ve son stündaki ★lar.
            print ('★', end="")
        else :
            if (i > 0 ) & (i < (boyut/2)) :
                if (j == i ) | (j == (boyut - i - 1)) :  # i'nin değerinin gittikçe azalması ve denklemi sağlaması için yazıldı. (j == (boyut-i-1))
                    print ('★', end="")
                else:
                    print (' ', end="") 
            else :
                print (' ', end="")
    print("\n", end="")

print ("\n")

# E harfi 
for i in range (boyut):
    for j in range (boyut):
        if (i == 0) | (i == int(boyut/2)) | (i == boyut-1): # E'nin 0, (boyut/2) ve (boyut-1)nci indisleri.
            print ('★', end="")
        else :
            if (j == 0) :
                print ('★', end="")
            else :
                print (' ', end="")
    print ("\n", end="")

print ("\n")

# T harfi 
for i in range (boyut):
    for j in range (boyut):
        if i == 0 :
            print ('★', end="")
        else :
            if (j == int(boyut/2)):
                print ('★', end="")
            else :
                print (' ', end="")
    print ("\n", end="")

print ("\n")
