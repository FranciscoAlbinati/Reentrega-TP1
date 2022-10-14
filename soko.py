PARED = "#"
CAJA = "$"
JUGADOR = "@"
OBJETIVO = "."
OBJETIVO_CAJA = "*"
OBJETIVO_JUGADOR = "+"
ESPACIO_VACIO = " "

def crear_grilla(grilla):
    f = len(grilla)
    for i in range(0,f):
        grilla [i] =list(grilla[i])
    return grilla
        
     
def dimensiones(grilla) :
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla'''
    columnas = int(len(grilla[0]))
    filas = int(len(grilla))
    return columnas,filas

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f)'''
    return grilla[f][c] == PARED

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f)'''
    return grilla[f][c] == OBJETIVO or  grilla[f][c] == OBJETIVO_JUGADOR or grilla[f][c] == OBJETIVO_CAJA

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f)'''
    return grilla[f][c] == CAJA or grilla[f][c] == OBJETIVO_CAJA

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f)'''
    return grilla[f][c] == OBJETIVO_JUGADOR or grilla[f][c] == JUGADOR

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado'''
    c,f = dimensiones(grilla)
    for i in range(0,f):
        for z in range (0,c):
            if grilla[i][z] == OBJETIVO or grilla[i][z] == OBJETIVO_JUGADOR:
               return False        
    return True


def mov (grilla,direccion,pos_x,pos_y):
         
        nueva_grilla =  crear_grilla(grilla[:])

        pos_sigX_1, pos_sigX_2, pos_sigY_1, pos_sigY_2 = pos_x + direccion[0], pos_x + direccion[0]*2, pos_y + direccion[1], pos_y + direccion[1]*2
              
        if nueva_grilla[pos_y][pos_x] == JUGADOR and nueva_grilla[pos_sigY_1][pos_sigX_1] == ESPACIO_VACIO:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = ESPACIO_VACIO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = JUGADOR
            return nueva_grilla
       
        elif nueva_grilla[pos_y][pos_x] == JUGADOR and nueva_grilla[pos_sigY_1][pos_sigX_1] == OBJETIVO_CAJA and hay_pared(nueva_grilla,pos_sigX_2,pos_sigY_2):
            return nueva_grilla 
        

        elif nueva_grilla[pos_y][pos_x] == JUGADOR and hay_objetivo(nueva_grilla,pos_sigX_1,pos_sigY_1) and nueva_grilla[pos_sigY_2][pos_sigX_2] == ESPACIO_VACIO and  nueva_grilla[pos_sigY_2][pos_sigX_2] != OBJETIVO:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = ESPACIO_VACIO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = OBJETIVO_JUGADOR
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == JUGADOR and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1)  and nueva_grilla[pos_sigY_2][pos_sigX_2] == ESPACIO_VACIO:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = ESPACIO_VACIO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = CAJA
            return nueva_grilla
            

        elif nueva_grilla[pos_y][pos_x] == JUGADOR and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1)  and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2) and  nueva_grilla[pos_sigY_2][pos_sigX_2] != OBJETIVO_CAJA and  nueva_grilla[pos_sigY_1][pos_sigX_1] != OBJETIVO_CAJA:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = ESPACIO_VACIO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = OBJETIVO_CAJA
            return nueva_grilla

        elif nueva_grilla[pos_y][pos_x] == OBJETIVO_JUGADOR and nueva_grilla[pos_sigY_1][pos_sigX_1] == ESPACIO_VACIO:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = OBJETIVO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = JUGADOR
            return nueva_grilla

        elif nueva_grilla[pos_y][pos_x] == OBJETIVO_JUGADOR and nueva_grilla[pos_sigY_1][pos_sigX_1] == OBJETIVO_CAJA and nueva_grilla[pos_sigY_2][pos_sigX_2] == ESPACIO_VACIO:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = OBJETIVO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = OBJETIVO_JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = CAJA
            return nueva_grilla

        elif nueva_grilla[pos_y][pos_x] == OBJETIVO_JUGADOR and hay_objetivo(nueva_grilla,pos_sigX_1,pos_sigY_1):
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = OBJETIVO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = OBJETIVO_JUGADOR
            return nueva_grilla
           
        elif nueva_grilla[pos_y][pos_x] ==  OBJETIVO_JUGADOR and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1) and nueva_grilla[pos_sigY_2][pos_sigX_2] == ESPACIO_VACIO:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = OBJETIVO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = CAJA       
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == OBJETIVO_JUGADOR and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1) and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2):
            nueva_grilla[pos_y][pos_x] = OBJETIVO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = OBJETIVO_CAJA           
            return nueva_grilla
            
            
        elif nueva_grilla[pos_y][pos_x] == OBJETIVO_JUGADOR and nueva_grilla[pos_sigY_1][pos_sigX_1] == OBJETIVO_CAJA and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2):
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = OBJETIVO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = OBJETIVO_JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = OBJETIVO_CAJA
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == JUGADOR and nueva_grilla[pos_sigY_1][pos_sigX_1] == OBJETIVO_CAJA and nueva_grilla[pos_sigY_2][pos_sigX_2] == ESPACIO_VACIO:
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = ESPACIO_VACIO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = OBJETIVO_JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = CAJA
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == JUGADOR and nueva_grilla[pos_sigY_1][pos_sigX_1] == OBJETIVO_CAJA and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2):
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = ESPACIO_VACIO
            nueva_grilla[pos_sigY_1][pos_sigX_1] = OBJETIVO_JUGADOR
            nueva_grilla[pos_sigY_2][pos_sigX_2] = OBJETIVO_CAJA            
            return nueva_grilla

        else:
            return nueva_grilla

def buscar_jugador (grilla):
    c,f = dimensiones(grilla)
    for i in range (0,f):
        for z in range (0,c):
            if grilla[i][z] == JUGADOR or grilla[i][z] == OBJETIVO_JUGADOR:
                return z,i

def mover (grilla, direccion):
  c,f = buscar_jugador(grilla)
  grilla_2= mov(grilla,direccion,c,f)
  return grilla_2



