from AgenteIA.AgenteJugador import AgenteJugador
from AgenteIA.AgenteJugador import ElEstado


class AgenteOso(AgenteJugador):

    def __init__(self, h=8, v=8, k=3):
        AgenteJugador.__init__(self)
        self.h = h
        self.v = v
        self.k = k

    def jugadas(self, estado):
        return estado.movidas

    def getResultado(self, estado, m):
        x,y,ficha = m
        if m not in estado.movidas:
            return ElEstado(jugador=('A' if estado.jugador == 'B' else 'B'),
                            get_utilidad=self.computa_utilidad(estado.tablero, m, estado.jugador),
                            tablero=estado.tablero, movidas=estado.movidas)

        tablero = estado.tablero.copy()
        #tablero[m] = estado.jugador
        tablero[m] = ficha
        movidas = list(estado.movidas)
        movidas.remove(m)
        return ElEstado(jugador=('A' if estado.jugador == 'B' else 'B'),
                        get_utilidad=self.computa_utilidad(tablero, m, estado.jugador),
                        tablero=tablero, movidas=movidas)

    def get_utilidad(self, estado, jugador):
        return estado.get_utilidad if jugador == 'B' else -estado.get_utilidad

    def testTerminal(self, estado):
        return estado.get_utilidad != 0 or len(estado.movidas) == 0

    def mostrar(self, estado):
        tablero = estado.tablero
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(tablero.get((x, y), '.')+" ", end="")
            print()

    def computa_utilidad(self, tablero, m, jugador):
        if (self.en_raya(tablero, m, jugador, (0, 1)) or
                self.en_raya(tablero, m, jugador, (1, 0)) or
                self.en_raya(tablero, m, jugador, (1, -1)) or
                self.en_raya(tablero, m, jugador, (1, 1))):
            return +1 if jugador == 'B' else -1
        else:
            return 0

    def en_raya(self, tablero, m, jugador, delta_x_y):
        (delta_x, delta_y) = delta_x_y
        x, y, ficha = m
        resultado = ['A','B','A']
        c = 0
        n = 0
        while c<3 and c>=0:
            if tablero.get((x, y)) == resultado[c]:
                #print(tablero.get((x, y)) + "  " + resultado[c] + "  " + str(c))
                n += 1
                c += 1
                x, y = x + delta_x, y + delta_y
                print("contador " + str(c))
            else:
                c = 3
        x, y, ficha = m
        c = 0
        while c<3 and c>=0:
            if tablero.get((x, y)) == resultado[c]:
                n += 1
                c += 1
                x, y = x - delta_x, y - delta_y
            else:
                c = 3
        n -= 1
        return n >= self.k
