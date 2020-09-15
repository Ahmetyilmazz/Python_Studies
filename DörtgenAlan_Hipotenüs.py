
# # Programmer : Ahmet YILMAZ

# print ("Bu program dörtgen çevresi ve alanını hesaplar .!.")

# kisa_kenar = float(input("Lütfen kısa kenarı giriniz : "))
# uzun_kenar = float(input("Lütfen uzun kenarı giriniz : "))

# cevre = (kisa_kenar + uzun_kenar)*2
# alan  = kisa_kenar * uzun_kenar

# print ("Girdiğiniz şeklin çevresi = ",cevre)
# print ("Girdiğiniz şeklin alanı   = ",alan)

print ("Bu uygulama bir DİK ÜÇGEN'in hipotenüs kenarını bulur .!.")

dik_kenar1 = float(input("Lütfen 1. Dik Kenarı giriniz : "))
dik_kenar2 = float(input("Lütfen 2. Dik Kenarı giriniz : "))

hipotenüs = float(dik_kenar1**2 + dik_kenar2**2)**0.5 # üssünü alma sebebimiz yani 0.5 karekök al demektir.
print("Bu kenarlara ait olan üçgenin hipotenüs uzunluğu = ",hipotenüs)

