
# Programmer : Ahmet YILMAZ 

#denklem = ax**2 + bx + c = 0

a = float(input("Lütfen x karenin katsayısını yazınız : ",))
b = float(input("Lütfen x'in katsayısını yazınız : "))
c = float(input("Lütfen sabit sayiyi yazınız : "))

delta = b**2 - 4 * a * c 

if delta > 0 :
    x1 = (- b - delta**0.5)/(2*a)
    x2 = (- b + delta**0.5)/(2*a) 

    print ("Denklemin 2 Reel Kökü Vardır Bunlar : ")
    print ("x1 = ",x1)
    print ("x2 = ",x2)

if delta == 0 :
    x1 = (- b - delta**0.5)/(2*a)
    x2 = (- b + delta**0.5)/(2*a)
    x1 = x2
    print ("Bu Denklemin Bir Kökü Vardır = ", x1)


if delta < 0 :
    print ("Bu denklemin Reel Kökü Yoktur.")