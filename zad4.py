txt = input("Unesite ime tekstualne datoteke: ")
dir="C:\\Users\\student\Downloads\\"+txt

try:
    with open(dir, "r") as datoteka:
        brojevi = []

        for linija in datoteka:
            if linija.startswith("X-DSPAM-Confidence: "):
                try:
                    vrijednost = float(linija.strip().split(":")[1])
                    brojevi.append(vrijednost)
                except:
                    continue
        if brojevi:
            prosjek = sum(brojevi) / len(brojevi)
            print(f"Srednja vrijednost pouzdanosti: {prosjek}")
        else:
            print("Greska!")
except:
    print("Datoteka nije pronadena!")
