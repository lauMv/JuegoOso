from AgenteIA.Entorno import Entorno
from AgenteIA.AgenteJugador import ElEstado
import pygame as pg
import sys
from pygame.locals import *


class Tablero(Entorno):

    def __init__(self, h=8, v=8):
        Entorno.__init__(self)
        
        movidasConS = [(x, y,'S') for x in range(1, h + 1) for y in range(1, v + 1)]
        movidasConO = [(x, y,'O') for x in range(1, h + 1) for y in range(1, v + 1)]
        movidas = movidasConS + movidasConO

        self.cantidad_osos = 0
        self.juegoActual = ElEstado(jugador='A', get_utilidad=0, tablero={}, movidas=movidas)
        self.ancho = 600
        self.alto = 600
        pg.init()
        self.ventana = pg.display.set_mode((self.ancho + 100, self.alto + 100), 0, 32)
        pg.display.set_caption("Sistemas Inteligentes - Juego Oso")

    def percibir(self, agente):
        agente.estado = self.juegoActual
        if agente.estado.movidas:
            agente.programa()
        estado = agente.getResultado(self.juegoActual, agente.acciones)
        
        if agente.testTerminal(estado):
            agente.vive = False

    def ejecutar(self, agente):
        print("Agente ", agente.estado.jugador, " juega ", agente.acciones)
        self.juegoActual = agente.getResultado(self.juegoActual, agente.acciones)
        agente.mostrar(self.juegoActual)
        print("Utilidad ", self.juegoActual.get_utilidad)

    def mostrar_opciones(self):
        op_s_img = pg.image.load("img/s_modified.jpeg")
        op_y_img = pg.image.load("img/o_modified.jpeg")
        op_s_img = pg.transform.scale(op_s_img, (60, 60))
        op_y_img = pg.transform.scale(op_y_img, (60, 60))
        self.ventana.blit(op_s_img, (620, 200))
        self.ventana.blit(op_y_img, (620, 400))

    def iniciar_pantalla(self):
        color_linea = (0, 0, 0)
        self.ventana.fill((255, 255, 255))
        self.mostrar_opciones()
        # lineas verticales
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8, 0), (self.ancho / 8, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 2, 0), (self.ancho / 8 * 2, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 3, 0), (self.ancho / 8 * 3, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 4, 0), (self.ancho / 8 * 4, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 5, 0), (self.ancho / 8 * 5, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 6, 0), (self.ancho / 8 * 6, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 7, 0), (self.ancho / 8 * 7, self.alto), 7)
        # pg.draw.line(self.ventana, color_linea, (self.ancho / 8 * 8, 0), (self.ancho / 8 * 8, self.alto), 7)
        # lineas horizontales
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8), (self.ancho, self.alto / 8), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 2), (self.ancho, self.alto / 8 * 2), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 3), (self.ancho, self.alto / 8 * 3), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 4), (self.ancho, self.alto / 8 * 4), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 5), (self.ancho, self.alto / 8 * 5), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 6), (self.ancho, self.alto / 8 * 6), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 8 * 7), (self.ancho, self.alto / 8 * 7), 7)
        font = pg.font.SysFont(None, 25)
        turno = font.render("Turno: A", True, (0, 0, 0))
        self.ventana.blit(turno, [620,50])

    def marcar(self, row, col, ficha, jugador):
        x_img = pg.image.load("img/s_modified.jpeg")
        y_img = pg.image.load("img/o_modified.jpeg")
        x_img = pg.transform.scale(x_img, (50, 50))
        o_img = pg.transform.scale(y_img, (50, 50))
        posx, posy = 0, 0
        if row == 1:
            posx = 0 + 10
        if row == 2:
            posx = self.ancho / 8 + 10
        if row == 3:
            posx = self.ancho / 8 * 2 + 10
        if row == 4:
            posx = self.ancho / 8 * 3 + 10
        if row == 5:
            posx = self.ancho / 8 * 4 + 10
        if row == 6:
            posx = self.ancho / 8 * 5 + 10
        if row == 7:
            posx = self.ancho / 8 * 6 + 10
        if row == 8:
            posx = self.ancho / 8 * 7 + 10
        if col == 1:
            posy = 0+ 10
        if col == 2:
            posy = self.alto / 8 + 10
        if col == 3:
            posy = self.alto / 8 * 2+ 10
        if col == 4:
            posy = self.alto / 8 * 3 + 10
        if col == 5:
            posy = self.alto / 8 * 4 + 10
        if col == 6:
            posy = self.alto / 8 * 5 + 10
        if col == 7:
            posy = self.alto / 8 * 6 + 10
        if col == 8:
            posy = self.alto / 8 * 7 + 10
        if jugador == 'S':
            self.ventana.blit(x_img, (posy, posx))
        else:
            self.ventana.blit(o_img, (posy, posx))
        
        pg.display.update()

    def accion_humano(self, age, ficha):
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
        age.acciones = fila, columna, ficha

    def run(self):
        self.iniciar_pantalla()
        actual = 0
        fps = 30
        ficha = 'O'
        tiempo = pg.time.Clock()
        victoriaXImg = pg.image.load('img/victoriaX.png')
        victoriaOImg = pg.image.load('img/victoriaO.png')
        victoriaEmpate = pg.image.load('img/victoriaEmpate.png')

        op_s_selected = pg.image.load('img/s_modified_selected.png')
        op_y_selected = pg.image.load('img/o_modified_selected.png')
        op_s_selected = pg.transform.scale(op_s_selected, (60, 60))
        op_y_selected = pg.transform.scale(op_y_selected, (60, 60))

        op_s_img = pg.image.load("img/s_modified.jpeg")
        op_y_img = pg.image.load("img/o_modified.jpeg")
        op_s_img = pg.transform.scale(op_s_img, (60, 60))
        op_y_img = pg.transform.scale(op_y_img, (60, 60))
        font = pg.font.SysFont(None, 25)

        self.mostrar_opciones()
        while True:
            for event in pg.event.get():
                x, y = pg.mouse.get_pos()
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if self.agentes[actual].__class__.__name__ == "HumanoOso":

                    if event.type is MOUSEBUTTONDOWN and (620 + 60 > x > 620 and 400 + 60 > y > 400):         
                        self.ventana.blit(op_s_img, (620, 200))
                        self.ventana.blit(op_y_selected, (620, 400))
                        ficha = 'O'

                    if event.type is MOUSEBUTTONDOWN and (620 + 50 > x > 620 and 200 + 50 > y > 200):
                        self.ventana.blit(op_y_img, (620, 400))
                        self.ventana.blit(op_s_selected, (620, 200))
                        ficha = 'S'
                    
                    if event.type is MOUSEBUTTONDOWN and (0 <= x < self.ancho and 0 <= y < self.alto):
                        self.agentes[actual].estado = self.juegoActual
                        if self.agentes[actual].estado.movidas :
                            self.accion_humano(self.agentes[actual],ficha)
                        estado = self.agentes[actual].getResultado(self.juegoActual, self.agentes[actual].acciones)
                        if estado != None:
                            self.cantidad_osos += estado.get_utilidad
                            turno = font.render("Turno:   ", True, (0, 0, 0))
                            self.ventana.blit(turno, [620,50])
                            turno = font.render("Turno: " + self.agentes[actual].estado.jugador, True, (0, 0, 0))
                            self.ventana.blit(turno, [620,50])
                            pg.display.update()
                            if self.agentes[actual].testTerminal(estado):
                                self.agentes[actual].vive = False
                            self.ejecutar(self.agentes[actual])
                            actual = 1
                    else :
                        actual = 0
                else:
                    self.percibir(self.agentes[actual])
                    self.ejecutar(self.agentes[actual])
                    actual = 0
            tablero = self.juegoActual.tablero
            for x, y in tablero.keys():
                self.marcar(x, y,ficha, tablero.get((x, y)))
            if self.finalizado():
                a = self.juegoActual.get_utilidad
                ##cantidad de osos con utilidad
                if self.cantidad_osos > 0 :
                        self.ventana.blit(victoriaXImg, (400, 250))
                        print("Victoria B")
                elif self.cantidad_osos < 0:
                        self.ventana.blit(victoriaOImg, (400, 250))
                        print("Victoria A")
                else :
                    self.ventana.blit(victoriaEmpate, (400, 250))
                    print("Empate")
                pg.quit()
                sys.exit()
            pg.display.update()
            tiempo.tick(fps)

