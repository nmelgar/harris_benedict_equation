print("Formula Harris-Benedict para Hombre")

pesoKg = input("¿Cuál es el peso en del paciente en KG?  ")
pesoKg = float(pesoKg)

alturaCm = input("¿Cuál es la altura del paciente en CM?  ")
alturaCm = float(alturaCm)

edad = input("¿Cuál es la edad del paciente?  ")
edad = float(edad)
formula = (66.5 +(13.75 * (pesoKg)) + (5 *(alturaCm)) - (6.75*(edad)))
formula = str(formula)

print(f"El MB(Kcal entre Día) del paciente es = " + formula)

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
    print("El MB del paciente es: " + finalConRango)
else:
    print("Siga su dieta :)")

