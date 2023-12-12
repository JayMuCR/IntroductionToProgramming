opc = int(input("Menu de opciones:\n 1.Numero perfecto.\n 2.Numero primo.\n 3.Calculadora.\n 4.Salir\n Digite su opcion a continuacion: "))
while opc != 4:
    if opc ==1:
        num = int(input("Digite un numero entero: "))
        div = 2
        conta = 0
        while div <= num:
            if num % div == 0:
                conta += num // div
            div= div+1

        if conta == num:
            print("El numero insertado es perfecto.")
        else:
            print("El numero insertado no es perfecto.")
        
        
    elif opc ==2:
        num = int(input("Digite el numero que desea saber si es primo o no: "))

        if num < 0:
            print(num, " no es un numero primo.")
        elif num > 0:
            for i in range(2,num):
                if (num % i) == 0:
                   print(num," no es un numero primo.")
                   break
            else:
                print(num," es un numero primo.")
                
    elif opc== 3:
        print("Calculadora")
        num1= int(input("Digite el primer numero: "))
        num2= int(input("Digite el segundo numero: "))
        opc=int(input("Digite mediante un numero que desea hacer con los numeros anteriores segun las siguientes opciones:\n 1.Sumar(+)\n 2.Restar(-)\n 3.Multiplicar(*)\n 4.Dividir(/)\n 5.Potencia(**)\n 6.Residuo de la division(%).\n Opcion: "))
        if opc ==1:
            result= num1+num2
            print("El resultado de la suma es:", result)
        elif opc ==2:
            result= num1-num2
            print("El resultado de la resta es:", result)
        elif opc ==3:
            result=num1*num2
            print("El resultado de la multiplicacion es:", result)
        elif opc ==4:
            result= num1/num2
            print("El resultado de la division es:", result)
        elif opc==5:
            result= num1**num2
            print("El resultado de la potencia es:", result)
        elif opc == 6:
            result= num1%num2
            print("El residuo de la division es:", result)
        else:
            print("Opcion invalida. Intentelo nuevamente.")

    elif opc==4:
        print("Cerrando el programa")

    else:
        print ("Opcion invalida, intentelo nuevamente.")
    opc = int(input("\nMenu de opciones:\n 1.Numero perfecto.\n 2.Numero primo.\n 3.Calculadora.\n 4.Salir\n Digite su opcion a continuacion: "))


        
