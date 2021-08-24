import random as rm

def niveles(nivel):
    if nivel == 1 : return ["elefante","ballena","ornitorrinco","salamandra"]
    elif nivel == 2 : return ["Reino Unido","Republica Checa","Nueva Zelanda"]
    else: return["Lo simple a veces es mejor","Nunca pares de aprender","Los limites los pones tu"]


def buscar(objetivo, letra, objetivoOculto):
    vuelta = objetivo.count(letra)
    inicio = 0
    for i in range(vuelta):
        pos = objetivo.find(letra, inicio)
        objetivoOculto = objetivoOculto[:pos] + letra + objetivoOculto[pos+1:]
        inicio = pos+1
    return objetivoOculto


def ocultar(palabra):
    for i in range(len(palabra)):
        if palabra[i] != " ":
            palabra = palabra.replace(palabra[i],"*")

    return palabra



def ahogado(nivel):
    if nivel <= 3:
        print(f"""
        Nivel {nivel}

        """)
        objetivo = rm.choice(niveles(nivel))
        objetivoOculto = ocultar(objetivo)
        while objetivo != objetivoOculto:
            print(objetivoOculto)
            letra = input("Ingrese letra: ")
            objetivoOculto = buscar(objetivo,letra,objetivoOculto)
            objetivoOculto = buscar(objetivo,letra.upper(),objetivoOculto)
            objetivoOculto = buscar(objetivo,letra.lower(),objetivoOculto)
        nivel = nivel +1
        ahogado(nivel)

    return True
        
    


if __name__ == "__main__":
    jugar = bool(input("""
        ********** Desea jugar al juego de los Ahorcado **********
        si quiere judar escribir si; en caso no, dar solo entrer:"""))
    while jugar:
        print("""
        Empecemos!!!""")
        nivel = 1
        resultado = ahogado(nivel)
        if resultado: 
            print("Ganaste!!! ")
        jugar = bool(input("""
        ********** Desea jugar al juego de los Ahorcado **********
        si quiere judar escribir si; en caso no, dar solo entrer:"""))
    print("Espero verlo luego, adios")
    exit()


    


    