#Para este codigo utilice una estructura parecida al punto anterior

def numeritos(n):
    #Lista vacia para almacenar los numeros
     lista_primer=[]
     
     for i in range(n):
          f=i+1
          print("Ingrese el",f,"dato")
          n_cuenta=int(input("-------->"))
          #Se van agregando los datos a la lista
          lista_primer.append(n_cuenta)
          
     print("La lista de los numeros es=",lista_primer)
     
     #Se empieza con la primer suma de los dos primeros elementos
     elemento_de_lista = lista_primer[0] + lista_primer[1] 
     #for que recorre la lista
     for i in range(1, n- 1):
        #Se van sumando los elementos consecutivos
        suma = lista_primer[i] + lista_primer[i + 1]
        #Si la suma es mayor que el elemento de la lista se actualiza
        if suma > elemento_de_lista:
           elemento_de_lista = suma
     
     print("La mayor suma de numeros consecutivos es=",elemento_de_lista)
     
   
     return(elemento_de_lista)
#Un ciclo while en caso de errores 
while True:
     print("---PROGRAMA PARA EVALUAR LA MAYOR SUMA DE CONSECUTIVOS---")
     print("  Indicaciones:                                        -|")
     print("->Por favor ingresa mas de dos numeros en la lista     -|")
     print("->Pulsa cero para salir del programa                   -|")
     n_datos=int(input("Por favor ingrese el numero de datos de la lista="))
     if n_datos <2 and n_datos>0 or n_datos<0:
          print("-------INGRESA DOS DATOS O MAS------- ")
     elif n_datos==0:
         print("Programa finalizado!")
         break
     else:
         #si todo esta bien se llama la funcion
         numeritos(n_datos)
