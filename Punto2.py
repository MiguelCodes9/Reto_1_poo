""" 
Los detalles del codigo se ecncuentran resumidos 
en las lineas de comentarios, donde basicamente
se usa un for que recorre la palabra y compara
las letras de forma simetrica 

""" 

def palindromo(palabra):
    #.lower() para ignorar mayusculas y minusculas lo que hace mas entendible el codigo

    palabra=palabra.lower()
    #Esto para la longitud de la palabra
    n_palabra=len(palabra)
    #Recorremos la palabra desde el inicio hasta la mitad
    #y comparamos con la letra correspondiente desde el final
    for i in range(n_palabra//2):
        if palabra[i] != palabra[n_palabra - i - 1]:
            print("No es un palindromo")
            return False #Si no es palindromo retorna falso
        else:
            print("es un palidromo")
   
    return True  


if __name__ == "__main__":
    
  palabra=str(input("Ingrese una palabra: "))
  palindromo(palabra)