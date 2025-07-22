numero = int(input("Ingresa el número de la ACL: "))

if 1 <= numero <= 99 or 1300 <= numero <= 1999:
    print("Es una ACL Estándar.")
elif 100 <= numero <= 199 or 2000 <= numero <= 2699:
    print("Es una ACL Extendida.")
else:
    print("El número no corresponde a una ACL válida.")
