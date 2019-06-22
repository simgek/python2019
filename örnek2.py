try:
    sayi_bir = int(input("Lütfen bir sayi girin : "))
    sayi_iki = int(input("Lütfen ikinci sayiyi girin : "))

    toplam = sayi_bir + sayi_iki
    fark   = sayi_bir - sayi_iki
    bolum  = sayi_bir / sayi_iki
    carpim = sayi_bir * sayi_iki

    print( "sayıların toplamı  :",toplam,
          "\nsayıların farkı   :",fark,
          "\nsayıların bölümü  :",bolum,
          "\nsayıların çarpımı :",carpim )

except (ValueError,SyntaxError) :
    print("Value Error hatası veya sytax error hatası")
except ZeroDivisionError:
    print("zero division error hatası")
except FileExistsError:
    print(" file exists error")
except:
    print("hata mesajı")