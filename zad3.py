brojevi = []

while True:
    unos = input("Unesite brojeve ('Done' za zavrsetak): ")

    if unos.lower() == "done":
        break
    
    try:
        broj = float(unos)
        brojevi.append(broj)
    except:
        print("Greska!")

if brojevi:
    brojeva_uneseno = len(brojevi)
    srednja_vrijednost = sum(brojevi) / len(brojevi)
    max_vr = max(brojevi)
    min_vr = min(brojevi)
    sortirani = sorted(brojevi)

print(f"Broj unesenih brojeva: {brojeva_uneseno}")
print(f"Srednja vrijednost: {srednja_vrijednost}")
print(f"Minimalna vrijednost: {min_vr}")
print(f"Maksimalna vrijednost: {max_vr}")
print(f"Sortirana lista: {sortirani}")