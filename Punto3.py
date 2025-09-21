##La explicacion del codigo se encuentra a detalle en las lineas de comentarios

def lista_primos(n):
    #Se crea una lista vacia para almacenar los numeros ingresados
     lista_primer=[]
     #Un for que va hasta donde el usuario decida
     for i in range(n):
          f=i+1
          print("Ingrese el",f,"dato")
          n_cuenta=int(input("-------->"))
          lista_primer.append(n_cuenta) #Se van agregando los datos a la lista
          
     print("La lista de los numeros es=",lista_primer)
     lista_secund=[]#Lista para almacenar los numeros primos
     #For que recorre la lista de numeros ingresados
     for j in lista_primer:
          if j > 1:  
               es_primo = True
               for k in range(2, int(j**0.5) + 1): #Criterio para determinar si un numero es primo
                    #Si los numeros menores de la raiz no dividen al numero, entonces es primo
                    if j % k == 0:
                         es_primo = False
                         break
               if es_primo:
                    lista_secund.append(j)
                    #Se agregan los numeros primos a la lista secundaria
     print("La lista de datos primos es=",lista_secund)

     return(lista_secund)
#Este cicloes para caso de errores ademas se cierra cuando se ingrese un cero
while True:
 
     print("Hola!Pulsa cero para salir del programa=")
     number=int(input("Por favor ingrese el numero de datos de la lista="))
     if number <0:
          print("Por favor ingresa datos validos ")
     elif number==0:
         print("Programa finalizado!")
         break
     else:
         lista_primos(number)


       