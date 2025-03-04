datoteka = "SMSSpamCollection.txt"

try:
    with open(datoteka, "r") as datoteka:
        ham_broj_rijeci = 0
        ham_broj_poruka = 0
        spam_broj_rijeci = 0
        spam_broj_poruka = 0
        spam_zavrsava_usklicnikom = 0

        for linija in datoteka:
            podaci = linija.strip().split("\t")
            if len(podaci) < 2:
                continue
            
            tip, poruka = podaci[0], podaci[1]
            broj_rijeci = len(poruka.split())

            if tip == "ham":
                ham_broj_rijeci += broj_rijeci
                ham_broj_poruka += 1
            elif tip == "spam":
                spam_broj_rijeci += broj_rijeci
                spam_broj_poruka += 1
                if poruka.endswith("!"):
                    spam_zavrsava_usklicnikom += 1

    prosjek_ham = ham_broj_rijeci / ham_broj_poruka if ham_broj_poruka > 0 else 0
    prosjek_spam = spam_broj_rijeci / spam_broj_poruka if spam_broj_poruka > 0 else 0

    print(f"Prosjecan broj rijeci u ham porukama: {prosjek_ham:.2f}")
    print(f"Prosjecan broj rijeci u spam porukama: {prosjek_spam:.2f}")
    print(f"Broj spam poruka koje zavrsavaju usklicnikom: {spam_zavrsava_usklicnikom}")

except:
    print("Datoteka nije pronadena!")
