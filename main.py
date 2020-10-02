from AgenteOso import AgenteOso
from Tablero import Tablero
from HumanoOso import HumanoOso

luis = HumanoOso()
juan = HumanoOso()
# juan = AgenteOso()

tablero = Tablero()
tablero.insertar_objeto(juan)
tablero.insertar_objeto(luis)
tablero.run()
