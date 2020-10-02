from AgenteOso import AgenteOso


class HumanoOso(AgenteOso):
    def __init__(self):
        AgenteOso.__init__(self)

    def programa(self):
        print("Jugadas permitidas: {}".format(self.jugadas(self.estado)))
        print("")
        cad_movida = input('jugada? ')
        movida = eval(cad_movida)
        self.acciones = movida
