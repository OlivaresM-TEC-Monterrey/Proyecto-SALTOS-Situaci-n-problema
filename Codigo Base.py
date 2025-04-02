# Código de Juego | Aquí es donde se programará todo ツ

matrix = [] # Tablero de Juego
def Inicializar_Tablero():
    for n in range(5):
        pack = []
        for m in range(5):
            pack.append(m+1)
        matrix.append(pack)



def Imprimir_Tablero():
    Filas = ["A", "B", "C", "D", "E"]
    print("\033[1m\t1\t2\t3\t4\t5\033[0m")
    print("    "+"+-------"*5 + "+")
    for n in range(len(matrix)):    
        print("\033[1m"+str(Filas[n]) + "\033[0m" + "   |   0"*len(matrix) + "   |")
        print("    "+"+-------"*5 + "+")

            

Inicializar_Tablero()
Imprimir_Tablero()