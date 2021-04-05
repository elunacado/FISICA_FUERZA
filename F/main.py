def calculo():

    ul = ["a = asceleracion", "m = masa", "f = fuerza"]

    print(ul)
    peticion=input("que quieres calcular?")


    def fuerza():
        m = float(input("dime el valor de la m "))
        a = float(input("dime el valor de la a "))
        result=m * a
        print(result)
        again=input("ingresa r y presiona enter si quieres realizar otra formula o presiona enter y cierra el pregrama")

        if again == "r":
            calculo()

    def asceleracion():
        f = float(input("dime el valor de la f "))
        m = float(input("dime el valor de la m "))
        result=f/m
        print(result)
        again = input("ingresa r y presiona enter si quieres realizar otra formula o presiona enter y cierra el pregrama")

        if again == "r":
            calculo()

    def masa():
        f = float(input("dime el valor de la f "))
        a = float(input("dime el valor de la a "))
        result=f/a
        print(result)
        again = input("ingresa r y presiona enter si quieres realizar otra formula o presiona enter y cierra el pregrama")

        if again == "r":
            calculo()

    if peticion=="f":
        fuerza()

    elif peticion=="a":
         asceleracion()

    elif peticion=="m":
        masa()


    else:
        print("not yet")
        input()

calculo()
