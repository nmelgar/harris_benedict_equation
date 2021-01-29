print("Formula Harris-Benedict para Mujer")

pesoKg = input("¿Cuál es el peso en de la paciente en KG?  ")
pesoKg = float(pesoKg)

alturaCm = input("¿Cuál es la altura de la paciente en CM?  ")
alturaCm = float(alturaCm)

edad = input("¿Cuál es la edad de la paciente?  ")
edad = float(edad)
formula = (655.1 +(9.56 * (pesoKg)) + (1.85 *(alturaCm)) - (4.68*(edad)))
formula = str(formula)

print(f"El MB(Kcal entre Día) de la paciente es = " + formula)

print(f"\n¿Agregarías grado de estrés?")
siono = input("Responda si o no: ")
siono = str(siono)

if siono == "si":
    print("¿Qué rango le darías de entre 1.2 a 1.9?")
    rango = input("Escriba el rango aquí: ")
    rango = float(rango)
    formula = float(formula)
    finalConRango = (formula * rango)
    finalConRango = str(finalConRango)
    print("El MB de la paciente es: " + finalConRango)
else:
    print("Siga su dieta :)")

