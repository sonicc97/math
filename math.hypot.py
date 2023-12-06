import math
def hipotenuza():
    a = float(input("Unesite duzinu prve katete:"))
    b = float(input("Unesite duzinu druge katete:"))
    c = math.hypot(a,b)
    print(f'Duzina hipotenuze je {c}')
hipotenuza()