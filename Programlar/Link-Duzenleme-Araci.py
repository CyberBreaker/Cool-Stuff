x = input("Linki girin: \t") #Linkin veya yazını girilmesi istendi.
z = input("Kaç sayfa yazdırılsın: \t") # Kaç defa yazırılması istendeği soruldu.
y = int(z) #Kaç defa yazdırılacağı karakter olarak girilmişti tam sayıya çevrildi.
s = input("Arttırılan sayının sonuna gelecek olan yazı:\t") #Linkin  veya yazının ortasından sayı arttırmak istiyorsanız buraya arttırılan sayıdan sonra gelecek kısımı yazın.
a = 0
while a < y: # linki girdikten sonra sayfa sayıları sırasıyla arttırıldı.
    a += 1
    print(x,a ,sep="",end=s +"\n")
