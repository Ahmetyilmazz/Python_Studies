# Basit_Hesap_Makinesi                         // Toplama,Çıkarma,Çarpma,Bölme
# Programmer : AHMET YILMAZ                       OrtalamaBulma,ÜsAlma,Karekök //


from math import sqrt                             # Math kütüphanesinin kullanılma sebebi : sqrt ifadesini çağırmaktır.

a= int(input ("1. Sayiyi Giriniz (A) : "))        # 'str' yazılırsa sayi yerine harf yazılmalıdır. 
b= int(input ("2. Sayiyi Giriniz (B) : "))
c= int(input ("3. Sayiyi Giriniz (C) : "))
d= int(input ("4. Sayiyi Giriniz (D) : "))
e= int(input ("5. Sayiyi Giriniz (E) : "))        # 'float' yazıldığı zaman ise ondalıklı ifade edilir.


print("Toplam : ",a+b+c+d+e)
print("Aritmetik Ortalaması : ",(a+b+c+d+e)/5)
print(" A - B : ",a-b)
print(" B üzeri C : ",b**c)                           # b**c ifadesi b üzeri c anlamına gelmektedir.
print(" (AxB) x (BxA) : ",(a*b)*(b*a))

print("Karekökleri Sirasiyla : ",sqrt(a) ,sqrt(b) ,sqrt(c) ,sqrt(d) ,sqrt(e))  # Bu satir ile birlikte tek satirda hepsinin de karekökleri alınabilir.
print("A'nın karekökü : ",sqrt(a))  
print("B'nin karekökü : ",sqrt(b))
print("C'nin karekökü : ",sqrt(c))
print("D'nin karekökü : ",sqrt(d))
print("E'nin karekökü : ",sqrt(e))

