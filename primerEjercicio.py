edad = int(input("Edad: "))
documento = input("¿Tiene documento por favor? (s/n): ") == "s"
if edad >= 15 and documento:
    print("Cumple los requisitos")
else:
    print("No cumple los requisitos")



