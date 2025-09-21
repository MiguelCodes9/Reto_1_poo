""" 
La estructura que decidi hacer para este codigo fue 
mostrando un menu de opciones para que el usuario en donde
se le da la opcion de escoger la operacion que desea realizar, ademas
de usar correcciones en caso de que no se cumpla alguna condicion, luego segun 
el usuario escoja se llama la funcion correspondiente


"""
##Funciones que se pueden realizar 
def sumar(a,b):
    s=a+b
    print("La suma de ",a,"y",b,"es=",s)
    return sumar
def restar(a,b):
    s=a-b
    print("La resta de ",a,"y",b,"es=",s)
    return restar
def multiplicar(a,b):
    s=a*b
    print("El producto de ",a,"y",b,"es=",s)
    return multiplicar
def dividir(a,b):
    s=a/b
    print("La divison entre ",a,"y",b,"es=",s)
    return multiplicar


if __name__ == "__main__":
##Menu de opciones 
    print("Ingrese el número segun la operacion=")
    print("|Sumar        1|")
    print("|Restar       2|")
    print("|Multiplicar  3|")
    print("|Dividir      4|")    
    #Seccion para pedir datos 
    opc=int(input("|-------------->"))
    if 1 < opc > 4:
        print("Numero incorrecto")              
    else:
        print("De acuerdo a la operación escojida ingrese los datos=")
        num1=int(input("Ingrese el primer numero="))
        num2=int(input("Ingrese el segundo numero="))
        ##Dependiendo la opcion se llama la funcion
        
        if opc ==1:
            sumar(num1,num2)
        elif opc==2:
            restar(num1,num2)
        elif opc==3:
            multiplicar(num1,num2) 
        elif opc==4:
            dividir(num1,num2)
        elif opc>4 and opc<1:
            print("Dato incorrecto, vuelva a ingresar el dato")



