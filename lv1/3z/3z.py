brojevi = []

while 1:
    unos = input('Unesite broj ili Done za kraj: ')
    if unos == 'Done':
        break
    try:
        broj = float(unos)
        brojevi.append(broj)
    except ValueError:
        print('Nevaljan unos')

velicina_liste = len(brojevi)
srednja_vrijednost = sum(brojevi) / velicina_liste
minimalna_vrijednost = min(brojevi)
maksimalna_vrijednost = max(brojevi)
sortirani_brojevi = sorted(brojevi)

print()
print('Unesen slijedeci broj brojeva: ', velicina_liste)
print('Srednja vrijednost brojeva: ', srednja_vrijednost)
print('Minimalna vrijednost: ', minimalna_vrijednost)
print('Maksimalna vrijednost: ', maksimalna_vrijednost)
print('Vasa lista brojeva: ', sortirani_brojevi)