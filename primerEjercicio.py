edad = int(input("Edad: "))
documento = input("¿Tiene documento confirme:_? (s/n): ") == "s"
if edad >= 15 and documento:
    print("Cumple los requisitos")
else:
    print("No cumple los requisitos")



