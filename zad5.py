import string

datoteka = "song.txt"

try:
    datoteka = open(datoteka, "r")
    rijeci_brojac = {}

    for linija in datoteka:
        linija = linija.lower()
        for znak in string.punctuation:
            linija = linija.replace(znak, "")
        
        rijeci = linija.split()

        for rijec in rijeci:
            if rijec in rijeci_brojac:
                rijeci_brojac[rijec] += 1
            else:
                rijeci_brojac[rijec] = 1

    datoteka.close()

    rijeci_jednom = []
    for rijec in rijeci_brojac:
        if rijeci_brojac[rijec] == 1:
            rijeci_jednom.append(rijec)

    print("Broj rijeci koje se pojavljuju samo jednom:", len(rijeci_jednom))
    print("Te rijeci su:", ", ".join(rijeci_jednom))

except:
    print("Datoteka nije pronadena!")
