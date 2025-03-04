def total_euro(radni_sati, satnica):
    return radni_sati*satnica

print("Unesite broj radnih sati: ")
radni_sati = float(input())
print("Unesite satnicu: ")
satnica = float(input())

print(f"Ukupno: {total_euro(radni_sati, satnica)}")