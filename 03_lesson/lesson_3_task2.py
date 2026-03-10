from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S25", +79051235451),
    Smartphone("Honor", "X9", +79279876541),
    Smartphone("Xiaomi", "T14", +79156547891),
    Smartphone("Techno", "POVA 7", +79081289451),
    Smartphone("Google", "Pixel", +79544561285),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")