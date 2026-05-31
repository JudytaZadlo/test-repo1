# from tty import IFLAG
#
# # bool
# # Typ prosty / prymitywny
#
# prawda = True
# falsz = False
#
# # Bool mogę uzyskać z wyniku metody
#
# a = "7"
# check = a.isnumeric()
# # print(check)
#
# b = 'ABC'
# check2 = b.islower()
# # print (check2)
#
# x = 7>4
# # print(x)
#
# y = 8 < 4 # mniejsze od
# # print(y)
# z = 10 >= 10 # większe bądź równe
# h = 10 <= 12 # mniejsze bądź równe
# rowne = "abc" == "abcd" # porównanie

# print(rowne)

# IF
# a = 9

# Blok kodu if
# odpali się jeśli warunek spełniony
# if a >= 10:
#     print("zgadza się")
#     print("kolejna operacja")
#     print("jeszcze jedna")
# else:
#     print("liczba jest za mała")

# typ_konta = "mod"
#
# if typ_konta == "admin":
#     print("witaj w panelu admina")
# elif typ_konta == "mod":
#     print("witaj moderatorze")
# elif typ_konta == "klient":
#     print("witaj klient")
# else:
#     print("nie rozpoznano")

# koszyk = 201
# kod = "ABC2026"
# kraj = "PL"

# if koszyk >= 200 and kod == "ABC2026":
#     koszyk *= 0.9
#     print(f"Uzyskałeś rabat!!. Do zapłaty {koszyk} zł")
# else:
#     print("Nie udało się uzyskać rabatu")

# if koszyk >= 200 and kod == "ABC2026" and kraj == "PL":
#     koszyk *= 0.9
#     print(f"Uzyskałeś rabat!!. Do zapłaty {koszyk} zł")
# else:
#     print("Nie udało się uzyskać rabatu")
# Napisz dwie zmienne o nazwie user_role i is_logged
# Następnie przygotuj instrukcję warunkową która sprawdza typ konta zalogowanego użytkownika:
#
# -Jeśli użytkownik jest zalogowany i jest administratorem wyświetlaj napis "Witaj w panelu admina"
# -Jeśli użytkownik jest moderatorem i jest zalogowany wyświetlaj napis "Witaj w panelu moderatora"
# -Jeśli uzytkownik loguje się na zwykłe konto i jest zalogowany wyświetlaj napis "Witaj w panelu użytkownika"
# -W każdym innym przypadku wyświetlaj napis błąd logowania

# user_role = "admin"
# is_logged = True
#
# if user_role == "admin" and is_logged:
#     print("Witaj w panelu admina")
# elif user_role == "mod" and is_logged:
#     print("Witaj w panelu moderatora")
# elif user_role == "user" and is_logged:
#     print("Witaj w panelu użytkownika")
# else:
#     print ("błąd logowania")
# 2.
# Prowadzisz sklep, który dostarcza towar jedynie do Polski, Niemiec i Czech
#
# Napisz zmienną o nazwie user_country
# Następnie zaprojektuj instrukcję warunkową która sprawdzi czy kupujący składa zamówienie z któregoś z powyższych krajów,
# jeśli NIE, wyświetlaj tekst: Dostawa towaru niemożliwa
# user_country = "DE"
# if user_country == "PL" or user_country == "CZ" or user_country == "DE":
#     print("Dostawa możliwa")
# else:
#     print ("Dostawa niemożliwa")

# Spróbuj napisać zmienną, w której za pomocą Pythona umieścisz informacje o aktualnej godzinie
#
# Następnie napisz instrukcję warunkową, która wyświetla powitanie w zależności od pory dnia
# -Między 6 a 12 "Good Morning"
# -Między 12 a 18 "Good Afternoon"
# -Powyżej 18 "Good Evening"

#
# from datetime import datetime
# now = datetime.now().hour
# if now < 6 and now < 12:
#     powitanie = "Good Morning"
# elif now >=12 and now < 18:
#     powitanie = "Good Afternoon"
# elif now >=18:
#     powitanie = "Good Evening"
# print(powitanie)
