# Programcı hataları (error)
# Programcı kusurları (bug)
# istisnalar (exception)
# mantıksal hatalar
print("sad")



try:
    telefon_numarası = input("lütfen telefon numarası giriniz : ")
    print("telefon numaranız : ",int(telefon_numarası))
except ValueError:
    print("işlem hatası")
    print("Lütfen geçerli bi sayı girin")
except ZeroDivisionError:
    print("işlem hatası")
    print("sıfıra bölünme hatası")