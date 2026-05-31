txt = 'hello world!'

# Zmień pierwszą literę na dużą
x = txt.capitalize()

# Zamień słowo world na słowo świecie
y = txt.replace("world","świecie")

# Wskaż miejsce od którego zaczyna się wskazana fraza
z = txt.rfind("r")

# Dzieli stringa na pojedyńcze elementy i zamienia w listę
a = txt.split()

# Zwraca true jeśli wszystkie litery są alfanumeryczne (a-z i 0-9)
b = txt.isalnum()

# Zwraca true jeśli wszystkie litery są małe
c = txt.islower()

# Sprawdza i zwraca true jeśli string zaczyna się od wskazanej frazy
d = txt.startswith("hello")
