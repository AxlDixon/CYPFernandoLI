A = int(input("Introduzca un número entero positivo:"))
B = int(input("Introduzca otro número entero positivo:"))
C = int(input("Introduzca otro número entero positivo:"))
if A > B:
    if A > C:
        print(f"{A} es el mayor.")
    else:
        if A == C:
            print(f"{A} y {C} son los mayores.")
        else:
            print(f"{C} es el mayor.")
else:
    if A == B:
        if A > C:
            print(f"{A} y {B} son los mayores.")
        else:
            if A == C:
                print(f"{A}, {B} y {C} son iguales.")
            else:
                print(f"{C} es el mayor.")
    else:
        if B > C:
            print(f"{B} es el mayor.")
        else:
            if B == C:
                print(f"{B} y {C} son los mayores.")
            else:
                print(f"{C} es el mayor.")

print("Fin del programa!!")
