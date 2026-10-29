edad = int(input("Edad: "))
documento = input("¿Tiene documento? (s/n): ") == "s"
if edad >= 18 and documento == True:
    print("Cumple los requisitos")
else:
    print("No cumple los requisitos")



