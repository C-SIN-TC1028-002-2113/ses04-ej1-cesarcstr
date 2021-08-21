def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if edad<=0:
      print ("Respuesta incorrecta")
    elif edad<18: 
        print ("No cumples requisitos")
    elif edad>=18:
        id = input("¿Tienes identificación oficial? (s/n): ")
        if id!= 's' and id!= 'n':
            print ("Respuesta incorrecta")
        elif id == 'n':
            print ("No cumples requisitos")
        else: print("Trámite de licencia concedido")
    


    

if __name__ == '__main__':
    main()
