def odredi_ocjenu(ocjena):
    if ocjena >= 0.9:
        return "A"
    elif ocjena >= 0.8:
        return "B"
    elif ocjena >= 0.7:
        return "C"
    elif ocjena >= 0.6:
        return "D"
    else:
        return "F"

try:
    ocjena = float(input("Unesite ocjenu (izmedu 0.0 i 1.0): "))

    if 0.0 <= ocjena <= 1.0:
        print(f"Ocjena: {odredi_ocjenu(ocjena)}")
    else:
        print(" Uneseni broj nije u intervalu!")

except:
    print("Greska!")