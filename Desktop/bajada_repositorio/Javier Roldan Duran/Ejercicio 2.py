def buscarPalabra():
    letra=input("Introduce una letra: ").lower()
    numero_palabras=len(lista_palabras)
    for i in lista_palabras:
       letra_palabra=i[:numero_palabras]  
       if letra==letra_palabra:
           lista_final.append(i)
          
lista_final=[]     
lista_separada=[]    
lista_palabras=["bocadillo", "pez", "ornitorrinco", "viaje","patrocinio", "ocio", "orangutan"]   
buscarPalabra()