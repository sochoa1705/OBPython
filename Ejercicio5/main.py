import math

year = int(input("Ingrese el año: "))

if math.fmod(year,4)==0:
    if math.fmod(year,100)==0:
        if math.fmod(year,400)==0:
            print(year, "Es bisiesto")
        else:
            print(year, "No es bisiesto")

    else:
        print(year, "Es bisiesto")

else:
    print(year, "No es bisiesto")


