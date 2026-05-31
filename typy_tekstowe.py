# str (string)
# Typ prosty/ prymitywny

# miasto = "Katowice"
# nazwisko = "Kowalski"
#
# sprawdz_typ = type(nazwisko)
# print(sprawdz_typ)
#
# #Konkat
#
# jezyk = "Python"
# az
# zdanie = jezyk + " to popularnt jezyk programowania"
# zdanie2 = "Moj ulubiony jezyk to " + jezyk + ". Jest on " + typ_jezyka + "."
#
# zdanie3 = f"Moj ulubiony jezyk to {jezyk}. Jest on {typ_jezyka}."
#
# print(zdanie2)
# print(zdanie3)

film = "haRRy pOtter"
duza_litera = film.upper()
tytul = film.title()
zastap_znaki = tytul.replace("r","b")
policz = film.count("r")
policz_bez_czulosci_na_litery = film.lower().count("r")

akapit = "To jest moj tekst"

pierwsza_litera = akapit[0]
ostatnia_litera = akapit[-1]
fragment = akapit[0:7]

print(fragment)
print(duza_litera)
print(film)
print(zastap_znaki)
print(policz)
print(policz_bez_czulosci_na_litery)