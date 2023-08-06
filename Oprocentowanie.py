#Zadanie drugie - oprocentowanie pozyczki i oszczednosci na koncie.
WartoscKredytu = input('Podaj wartosc kredytu: ')
OprocentowanieKredytu = input('Podaj wartosc oprocentowania kredytu: ')
Rata = input('Podaj wartosc raty kredytu: ')
WartoscKredytu = float(WartoscKredytu)
OprocentowanieKredytu = float(OprocentowanieKredytu)
Rata = float(Rata)

#Pierwszy rok kredytu
InflacjaStyczen1 = 1.592824484
InflacjaLuty1 = -0.453509101
InflacjaMarzec1 = 2.324671717
InflacjaKwiecien1 = 1.261254407
InflacjaMaj1 = 1.782526286
InflacjaCzerwiec1 = 2.329384541
InflacjaLipiec1 = 1.502229842
InflacjaSierpien1 = 1.782526286
InflacjaWrzesien1 = 2.328848994
InflacjaPazdziernik1 = 0.616921348
InflacjaListopad1 = 2.352295886
InflacjaGrudzien1 = 0.337779545

#Drugi rok kredytu
InflacjaStyczen2 = 1.577035247
InflacjaLuty2 = -0.292781443
InflacjaMarzec2 = 2.48619659
InflacjaKwiecien2 = 0.267110318
InflacjaMaj2 = 1.417952672
InflacjaCzerwiec2 = 1.054243267
InflacjaLipiec2 = 1.480520104
InflacjaSierpien2 = 1.577035247
InflacjaWrzesien2 = -0.07742069
InflacjaPazdziernik2 = 1.165733399
InflacjaListopad2 =-0.404186718
InflacjaGrudzien2 = 1.499708521

#Wzor, ktory wykorzystalem z Excela
#Wzor = (1 + ((B3+3)/1200)) * C2 - 200

#Pierwsza rata styczen
Oprocentowanie1 = (1 + ((InflacjaStyczen1+OprocentowanieKredytu)/1200)) * WartoscKredytu - Rata
Roznica1 = (WartoscKredytu - Oprocentowanie1)
print(f'Twoja pozostała kwota kredytu to {Oprocentowanie1}, to {Roznica1} mniej.')
#Druga rata Luty
Oprocentowanie2 = (1 + ((InflacjaLuty1+OprocentowanieKredytu)/1200)) * Oprocentowanie1 - Rata
Roznica2 = (Oprocentowanie1 - Oprocentowanie2)
print(f'Twoja pozostała kwota kredytu to {Oprocentowanie2}, to {Roznica2} mniej niż w poprzednim miesiącu - Styczniu.')
#Trzecia rata Marzec
Oprocentowanie3 = (1 + ((InflacjaMarzec1+OprocentowanieKredytu)/1200)) * Oprocentowanie2 - Rata
Roznica3 = (Oprocentowanie2 - Oprocentowanie3)
print(f'Twoja pozostała kwota kredytu to {Oprocentowanie3}, to {Roznica3} mniej niż w poprzednim miesiącu - Lutym.')
#Czwarta rata Kwiecien
Oprocentowanie4 = (1 + ((InflacjaKwiecien1+OprocentowanieKredytu)/1200)) * Oprocentowanie3 - Rata
Roznica4 = (Oprocentowanie3 - Oprocentowanie4)
print(f'Twoja pozostała kwota kredytu to {Oprocentowanie4}, to {Roznica4} mniej niż w poprzednim miesiącu - Marcu.')
#Piata rata Maj
Oprocentowanie5 = (1 + ((InflacjaMaj1+OprocentowanieKredytu)/1200)) * Oprocentowanie4 - Rata
Roznica5 = (Oprocentowanie4 - Oprocentowanie5)
print(f'Twoja pozostała kwota kredytu to {Oprocentowanie5}, to {Roznica5} mniej niż w poprzednim miesiącu - Kwietniu.')
#Szosta rata Czerwiec
Oprocentowanie6 = (1 + ((InflacjaCzerwiec1+OprocentowanieKredytu)/1200)) * Oprocentowanie5 - Rata
Roznica6 = (Oprocentowanie5 - Oprocentowanie6)
print(f'Twoja pozostała kwota kredytu to {Oprocentowanie6}, to {Roznica6} mniej niż w poprzednim miesiącu - Maju.')