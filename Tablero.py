from AgenteIA.Entorno import Entorno
from AgenteIA.AgenteJugador import ElEstado
import pygame as pg
import sys
from pygame.locals import *


class Tablero(Entorno):

    def __init__(self, h=8, v=8):
        Entorno.__init__(self)
        movidas = [(x, y, ficha) for x in range(1, h + 1) for y in range(1, v + 1) for ficha in "OS"]
        self.juegoActual = ElEstado(jugador='A', ficha='S', get_utilidad=0, tablero={}, movidas=movidas)
        self.ancho = 600
        self.alto = 600
        pg.init()
        self.ventana = pg.display.set_mode((self.ancho + 100, self.alto + 100), 0, 32)
        pg.display.set_caption("Sistemas Inteligentes - Juego Oso")

    def percibir(self, agente):
        agente.estado = self.juegoActual
        if agente.estado.movidas:
            agente.programa()
        if agente.testTerminal(agente.getResultado(self.juegoActual, agente.acciones)):
            agente.vive = False

    def ejecutar(self, agente):
        print("Agente ", agente.estado.jugador, " juega ", agente.acciones)
        self.juegoActual = agente.getResultado(self.juegoActual, agente.acciones)
        agente.mostrar(self.juegoActual)
        print("Utilidad ", self.juegoActual.get_utilidad)

    def iniciar_pantalla(self):
        color_linea = (0, 0, 0)
        self.ventana.fill((255, 255, 255))
        op_x_img = pg.image.load("img/X_modified.png")
        op_y_img = pg.image.load("img/o_modified.png")
        op_x_img = pg.transform.scale(op_x_img, (50, 50))
        op_y_img = pg.transform.scale(op_y_img, (60, 60))
        self.ventana.blit(op_x_img, (620, 200))
        self.ventana.blit(op_y_img, (620, 400))
        # lineas verticales
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8, 0), (self.ancho / 8, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 2, 0), (self.ancho / 8 * 2, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 3, 0), (self.ancho / 8 * 3, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 4, 0), (self.ancho / 8 * 4, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 5, 0), (self.ancho / 8 * 5, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 6, 0), (self.ancho / 8 * 6, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 7, 0), (self.ancho / 8 * 7, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 8, 0), (self.ancho / 8 * 8, self.alto), 7)
        # lineas horizontales
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8), (self.ancho, self.alto / 8), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 2), (self.ancho, self.alto / 8 * 2), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 3), (self.ancho, self.alto / 8 * 3), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 4), (self.ancho, self.alto / 8 * 4), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 5), (self.ancho, self.alto / 8 * 5), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 6), (self.ancho, self.alto / 8 * 6), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 7), (self.ancho, self.alto / 8 * 7), 7)

    def marcar(self, row, col, jugador):
        x_img = pg.image.load("img/X_modified.png")
        y_img = pg.image.load("img/o_modified.png")
        x_img = pg.transform.scale(x_img, (80, 80))
        o_img = pg.transform.scale(y_img, (80, 80))
        posx, posy = 0, 0
        if row == 1:
            posx = 30
        if row == 2:
            posx = self.ancho / 8 
        if row == 3:
            posx = self.ancho / 8 * 2 
        if row == 4:
            posx = self.ancho / 8 * 3 
        if row == 5:
            posx = self.ancho / 8 * 4 
        if row == 6:
            posx = self.ancho / 8 * 5 
        if row == 7:
            posx = self.ancho / 8 * 6 
        if row == 8:
            posx = self.ancho / 8 * 7 
        if col == 1:
            posy = 30
        if col == 2:
            posy = self.alto / 8 
        if col == 3:
            posy = self.alto / 8 * 2
        if col == 4:
            posy = self.alto / 8 * 3 
        if col == 5:
            posy = self.alto / 8 * 4 
        if col == 6:
            posy = self.alto / 8 * 5 
        if col == 7:
            posy = self.alto / 8 * 6 
        if col == 8:
            posy = self.alto / 8 * 7 
        if jugador == 'B':
            self.ventana.blit(x_img, (posy, posx))
        else:
            self.ventana.blit(o_img, (posy, posx))
        pg.display.update()

    def accion_humano(self, age):
        mouse = pg.mouse.get_pos()
        ficha = "O"
        op_x_selected = pg.image.load('img/X_modified_selected.png')
        op_y_selected = pg.image.load('img/o_modified_selected.png')
        op_x_selected = pg.transform.scale(op_x_selected, (50, 50))
        op_yop_y_selected_img = pg.transform.scale(op_y_selected, (60, 60))
        if 620 + 50 > mouse[0] > 620 and 200 + 50 > mouse[1] > 200:         
            self.ventana.blit(op_x_selected, (620, 200))
            ficha = "X"
        if 620 + 60 > mouse[0] > 620 and 400 + 60 > mouse[1] > 400:         
            self.ventana.blit(op_y_selected, (620, 400))
            ficha = "O"

        x, y = pg.mouse.get_pos()
        # obtener columna del click
        if x < self.ancho / 8:
            columna = 1
        elif x < self.ancho / 8 * 2:
            columna = 2
        elif x < self.ancho / 8 * 3:
            columna = 3
        elif x < self.ancho / 8 * 4:
            columna = 4
        elif x < self.ancho / 8 * 5:
            columna = 5
        elif x < self.ancho / 8 * 6:
            columna = 6
        elif x < self.ancho / 8 * 7:
            columna = 7
        elif x < self.ancho:
            columna = 8
        else:
            columna = None
        # obtener fila del click
        if y < self.alto / 8:
            fila = 1
        elif y < self.alto / 8 * 2:
            fila = 2
        elif y < self.alto / 8 * 3:
            fila = 3
        elif y < self.alto / 8 * 4:
            fila = 4
        elif y < self.alto / 8 * 5:
            fila = 5
        elif y < self.alto / 8 * 6:
            fila = 6
        elif y < self.alto / 8 * 7:
            fila = 7
        elif y < self.alto:
            fila = 8
        else:
            fila = None
        # acciones del agente humano = fila columna seleccionada
        age.acciones = fila, columna

    def run(self):
        self.iniciar_pantalla()
        actual = 0
        fps = 30
        tiempo = pg.time.Clock()
        victoriaXImg = pg.image.load('img/victoriaX.png')
        victoriaOImg = pg.image.load('img/victoriaO.png')
        victoriaEmpate = pg.image.load('img/victoriaEmpate.png')
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if self.agentes[actual].__class__.__name__ == "HumanoOso":
                    #controla ficha elegida
                    if event.type is MOUSEBUTTONDOWN:
                        print("juega humano")
                        self.agentes[actual].estado = self.juegoActual
                        if self.agentes[actual].estado.movidas:
                            self.accion_humano(self.agentes[actual])
                        if self.agentes[actual].testTerminal(self.agentes[actual].getResultado(self.juegoActual, self.agentes[actual].acciones)):
                            self.agentes[actual].vive = False
                        self.ejecutar(self.agentes[actual])
                        actual = 1
                else:
                    self.percibir(self.agentes[actual])
                    self.ejecutar(self.agentes[actual])
                    actual = 0
                    print("juega maquina")
            tablero = self.juegoActual.tablero
            for x, y in tablero.keys():
                self.marcar(x, y, tablero.get((x, y)))
            if self.finalizado():
                a = self.juegoActual.get_utilidad
                if a != 0:
                    if a > 0:
                        self.ventana.blit(victoriaXImg, (400, 250))
                        print("Victoria X ")
                    else:
                        self.ventana.blit(victoriaOImg, (400, 250))
                        print("Victoria O ")
                else:
                    self.ventana.blit(victoriaEmpate, (400, 250))
                    print("Empate")
                pg.quit()
                sys.exit()
            pg.display.update()
            tiempo.tick(fps)
