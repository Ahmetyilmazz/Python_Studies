
# Programmer : Ahmet YILMAZ

print ("Bu program Vize ve Final notu ile ortalama hesaplar ve bu ortalamaya göre öğrencinin geçip geçmeme durumunu belirtir.")

vize = int(input("Lütfen Vize notunuzu Giriniz : "))
final = int(input("Lütfen Final notunuzu Giriniz : "))

ortalama = (vize*0.4 + final*0.6) # Vize = %40 , Final = %60 baz alınarak yazılmıştır.
print ("Ders Ortalamanız : ",ortalama)

if ortalama >= 60 :
    print ("Tebrikler, GEÇTİNİZ !!!")
else :
    print ("Maalesef bu dersten GEÇEMEDİNİZ !.!.!")