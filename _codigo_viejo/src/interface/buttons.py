import pygame as pg
from .utils import Window, FontManager, ColorManager
from .ctrls import Ctrls
from .buttons_wrappers import ButtonWrappers
from typing import List, Callable

class ButtonGeneric:
    def __init__(self, save_btn:bool, id_btn:str, f:Callable, pos_x:int, pos_y:int, win:Window, ctrls:Ctrls):
        self.save_when_changing_scene = save_btn
        self.id_btn = id_btn            # Para distinguir los botones entre sí, o crear condicionales.
        self.f = f                      # Función que se ejecuta cuando el botón es pulsado.
        self.win = win
        self.ctrls = ctrls
        self.pos_btn = {"x": pos_x, "y": pos_y}     # Las claves son 'x', 'y', luego agregamos 'w', 'h' dependiente del tipo de boton que sea.

        self.is_active = True   # Indica si el botón se encuentra activo. De no estarlo, no ejecuta su funcionalidad al darle click.
        self.mouse_up = False   # Indica si la persona tiene el mouse arriba del botón o no.

    @ButtonWrappers.refresh_mouse_up
    def draw(self):
        self._how_to_draw()

    @ButtonWrappers.check_mouse_up
    @ButtonWrappers.check_is_active
    def event(self, *args, **kwargs):
        """ El evento tiene que cumplir las condiciones de los decoradores.
            Para agregar nuevas condiciones, se puede decorar la función 'self.f'."""
        self.f(self, *args, **kwargs)

    def _how_to_draw(self):
        """ Sobrescribir para pintar el botón en la pantalla.
            Si se quieren nuevas condiciones se puede agregar
            un decorador al sobrescribir."""
        pass


class Buttons:
    class Simple(ButtonGeneric):
        FONT_MANAGER = FontManager()
        COLOR_MANAGER = ColorManager()
        def __init__(self, save_btn:bool, id_btn:str, f:Callable, pos_x:int, pos_y:int, win:Window, ctrls:Ctrls, text:str, color:dict=None, font_name="Minecraft", font_size=15, margin=5):
            super().__init__(save_btn, id_btn, f, pos_x, pos_y, win, ctrls)
            self.text = text
            self.font = self.FONT_MANAGER.get_font(font_name, font_size)
            self.pos_text = {
                "x": pos_x + margin,
                "y": pos_y + margin
            }

            self._add_w_h(margin)                       # Las claves son 'x', 'y', 'w', 'h'.
            self.color = self._get_color_default() if color==None else color

        def _how_to_draw(self):
            """ Revisa si el mouse está encima o fuera del botón, dibuja un rectángulo
                con el texto dentro."""
            mouse_up_or_out = "up" if self.mouse_up else "out"
            text_render = self.font.render(self.text, True, self.color["text"][mouse_up_or_out])

            pg.draw.rect(self.win.get(), self.color["btn"][mouse_up_or_out], self._get_values_pos_btn())
            self.win.blit(text_render, (self.pos_text["x"], self.pos_text["y"]))

        def _add_w_h(self, margin:int):
            """ Agrega 'w' y 'h' a pos_text y pos_btn."""
            self.pos_text.update(self.FONT_MANAGER.get_text_size(self.font, self.text))
            self.pos_btn.update({
                "w": self.pos_text["w"] + 2*margin,
                "h": self.pos_text["h"] + 2*margin
            })
        
        def _get_values_pos_btn(self):
            return [
                self.pos_btn["x"],
                self.pos_btn["y"],
                self.pos_btn["w"],
                self.pos_btn["h"]
            ]
        
        def _get_color_default(self):
            """ Ver de rescribir esta función para que el usuario
                pueda cambiar la estética de los botones por default."""
            return {
                "text": {
                    "up": self.COLOR_MANAGER.get_color("White"),
                    "out": self.COLOR_MANAGER.get_color("LightGray"),
                },
                "btn": {
                    "up": self.COLOR_MANAGER.get_color("DeepSkyBlue"),
                    "out": self.COLOR_MANAGER.get_color("DodgerBlue"),
                }
            }


    class ImageButton(ButtonGeneric):
        def __init__(self, save_btn:bool, id_btn:str, f:Callable, pos_x:int, pos_y:int, win:Window, ctrls:Ctrls):
            super().__init__()


    
    
class Events:
    def change_scene(btn:Buttons.Simple):
        print(btn.id_btn)





class ButtonsContainer:
    """ Dentro de cada escena hay que instanciar un objeto que herede de ButtonsContainer,
        el cual va a guardar en BTNS todos los botones de la escena.
    
        Atributes
        ---------
        btns: (List[ButtonGeneric])
            Guardar todos los botones de la escena en esta variable. Cuando se sale de una escena
            esta variable debe quedar vacía. Para que al entrar al siguiente escenario se cargen
            los botones nuevos botones."""

    def __init__(self):
        self._btns: List[ButtonGeneric] = []
        self._btns_saved: dict[str, List[ButtonGeneric]] = {}

    def get(self) -> List[ButtonGeneric]:
        return self._btns

    def draw_all_btns(self):
        for btn in self._btns:
            btn.draw()

    def load_scene_buttons(self, scene:str, btns:List[ButtonGeneric]):
        """ La escena podría tener botones guardados y ordenados en la misma forma en
            que son declarados dentro del loop de la escena, por lo que hay que
            revisar para cada uno de los botones provistos, si el ID corresponde
            con alguno de los botones guardados en _btns_saved."""
        if not scene in self._btns_saved:       # Si no hay botones guardados de esta escena.
            self._btns = btns
        else:
            i=0
            for _ in range(len(self._btns_saved[scene])):
                flag = True
                while flag and i<len(btns):
                    """ Nos fijamos que le primer botón que esté guardado en la lista
                        coincida su id_btn con los botones dados por parámetro.
                        De encontrar una coincidencia, se reemplaza el que fué dado
                        por parámetro, con el guardado."""
                    if self._btns_saved[scene][0].id_btn == btns[i].id_btn:
                        btns[i] = self._btns_saved[scene].pop(0)
                        flag = False
                    i+=1
            self._btns_saved.pop(scene)         # Eliminamos la clave. Los btns fueron cargados y eliminados de aquí.

    def save_scene_buttons(self, scene:str):
        """ Guarda los botones configurados para guardarse al cambiar de escena."""
        self._btns_saved[scene] = [btn for btn in self._btns if btn.save_when_changing_scene]
        
        if len(self._btns_saved[scene]) == 0:       # Si no guardó ningún botón.
            self._btns_saved.pop(scene)
        
        self._btns = []                             # Borramos los botones.







"""
class Button_CambiarVentana(Button):
    def __init__(self, juego, poss_boton, text, NuevaVentana, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=15):
        super().__init__(juego, poss_boton, text, color_texto_out, color_texto_up, color_boton_out, color_boton_up, tipo_fuente, tamaño_fuente)
        self.NuevaVentana = NuevaVentana
    

    def EventosCambiarVentana(self):
        if self.mouse_up:
            self.win.CambiarDeVentana(self.NuevaVentana)


class Button_CheckButton(Button):
    def __init__(self, juego, poss_boton, text, Valor_True, Valor_False, Valor_Inicial, Color_Borde_True=WHITE, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=15):
        super().__init__(juego, poss_boton, text, color_texto_out, color_texto_up, color_boton_out, color_boton_up, tipo_fuente, tamaño_fuente)
        self.Valores_Posibles = {
            True : Valor_True,
            False : Valor_False
            }
        
        self.color_borde_true = Color_Borde_True
        self.Valor = Valor_Inicial   # Esto va a almacenar el valor booleano que va a tener, y si quisiera el valor tendría que buscarlo del diccionario.
    

    def EventosCheckButton(self):
        if self.mouse_up:
            self.CambiarValor()


    def InsertarBoton(self):
        self.MouseUp()
        if self.mouse_up:
            texto = self.font.render(self.text , True , self.color_texto_up)
            pg.draw.rect(self.win.ventana, self.color_boton_up, [self.poss_boton[0], self.poss_boton[1], self.dim_boton[0], self.dim_boton[1]])
        else:
            texto = self.font.render(self.text , True , self.color_texto_out)
            pg.draw.rect(self.win.ventana, self.color_boton_out, [self.poss_boton[0], self.poss_boton[1], self.dim_boton[0], self.dim_boton[1]])
        
        if self.Valor == True:  # Si el botón está marcado que dibuje un borde.
            pg.draw.rect(self.win.ventana, self.color_borde_true, [self.poss_boton[0], self.poss_boton[1], self.dim_boton[0], self.dim_boton[1]], 3)
        
        self.win.ventana.blit(texto, (self.pos_text[0], self.pos_text[1]))


    def CambiarValor(self):          # Esta función va a cambiar el valor del booleano, para asi acceder al otro elemento del diccionario.
        self.Valor = not(self.Valor)
        ############## HACER ALGO CON LA ANIMACIÓN QUE SE MUESTRA DEL BOTON CUANDO ESTÁ EN TRUE
    
    
    def GetValue(self):
        return self.Valores_Posibles[self.Valor]


class Button_RadioButton():     # Vamos a hacerla de cero copiando algunas funcionalidades, por q tenemos q trabajar con un grupo de objetos.
    '''poss_boton, y text van a ser listas, una para cada botón. Luego el resto de propiedades como, dim_texto, poss_texto, dim_boton, mouse_up también lo serán.
    El texto que van a almacenar cuando sean oprimidos estos botones, es el contenido del texto de cada botón.
    Cuando se quiera crear un conjunto de radiobuttons, crear una sub-clase de ésta para que Lista_Objetos sea única de ese conjunto de objetos.'''

    def __init__(self, juego, poss_boton, text, Indice_Inicial, color_borde_true=RED, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=15):
        self.juego = juego

        self.color_borde_true = color_borde_true
        self.poss_boton = poss_boton    #poss_boton = [[poss_boton_x_1, poss_boton_y_1] ,[poss_boton_x_2, poss_boton_y_2], ....., [poss_boton_x_n, poss_boton_y_n]] 
        self.text = text                #text = [text_1, text_2, ....., text_n]
        
        self.fuente = pg.font.Font(tipo_fuente, tamaño_fuente)  #La misma fuente para todos.
        

        margen = 5          #Margen entre el texto y los bordes del boton

        
        # Calculamos la cantidad de pixeles que va a ocupar el texto.
        self.dim_texto = []
        self.poss_texto = []
        self.dim_boton = []
        self.mouse_up = []
        
        for i in range(len(self.text)):
            self.dim_texto.append(self.fuente.size(self.text[i]))
            self.poss_texto.append( [poss_boton[i][0] + margen, poss_boton[i][1] + margen])
            self.dim_boton.append( [self.dim_texto[i][0] + 2*margen, self.dim_texto[i][1] + 2*margen] )      #dim = Lo voy a calcular como el Ancho y alto del texto, agregando algunos pixeles de margen
            self.mouse_up.append(False)     # Con esto vamos a saber si la persona tiene el mouse arriba del botón o no.
            
        


        self.color_texto_out = color_texto_out  #Color del texto cuando el mouse está FUERA del botón
        self.color_texto_up = color_texto_up    #Color del texto cuando el mouse está ENCIMA del botón
        self.color_boton_out = color_boton_out  #Color del boton cuando el mouse está FUERA del botón
        self.color_boton_up = color_boton_up    #Color del boton cuando el mouse está ENCIMA del botón

        self.Indice_Valor = Indice_Inicial
        self.Valor = self.text[self.Indice_Valor]


    def EventosRadioButtons(self):          # Este evento hay que ponerlo dentro del evento "MOUSEBUTTONDOWN"
        for i in range(len(self.text)):
            if self.mouse_up[i]:
                self.CambiarValor(i)


    def InsertarBoton(self):
        self.MouseUp()
        for i in range(len(self.text)):
            if self.mouse_up[i]:
                texto = self.fuente.render(self.text[i] , True , self.color_texto_up)
                pg.draw.rect(self.juego.ventana, self.color_boton_up, [self.poss_boton[i][0], self.poss_boton[i][1], self.dim_boton[i][0], self.dim_boton[i][1]])
            else:
                texto = self.fuente.render(self.text[i] , True , self.color_texto_out)
                pg.draw.rect(self.juego.ventana, self.color_boton_out, [self.poss_boton[i][0], self.poss_boton[i][1], self.dim_boton[i][0], self.dim_boton[i][1]])
            
            if self.Indice_Valor == i:  # Si el botón está marcado que dibuje un borde.
                pg.draw.rect(self.juego.ventana, self.color_borde_true, [self.poss_boton[i][0], self.poss_boton[i][1], self.dim_boton[i][0], self.dim_boton[i][1]], 3)

            self.juego.ventana.blit(texto, (self.poss_texto[i][0], self.poss_texto[i][1]))


    def MouseUp(self):
        '''Devuelve True si el mouse está arriba del botón.
        Devuelve False si el mouse está fuera del botón.'''
        for i in range(len(self.text)):
            if self.poss_boton[i][0] <= self.juego.mouse[0] <= self.poss_boton[i][0]+self.dim_boton[i][0] and self.poss_boton[i][1] <= self.juego.mouse[1] <= self.poss_boton[i][1]+self.dim_boton[i][1]: 
                self.mouse_up[i] = True
            else:
                self.mouse_up[i] = False
    




    def CambiarValor(self, i):
        self.Indice_Valor = i
        self.Valor = self.text[self.Indice_Valor]


class Button_ListaDesplegable():
    def __init__(self, juego, poss_boton, Listado, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=15):
        self.juego = juego
        self.Listado = Listado
        
        self.fuente = pg.font.Font(tipo_fuente, tamaño_fuente)
        Ancho_Max = 0
        Alto_Max = 0
        margen = 5
        self.mouse_up_contraido = False
        self.mouse_up_desplegado = []
        self.poss_botones = []
        self.poss_textos = []
        for i in range(len(self.Listado)):
            if self.fuente.size(Listado[i])[0]>Ancho_Max:
                Ancho_Max = self.fuente.size(Listado[i])[0]
            if self.fuente.size(Listado[i])[1]>Alto_Max:
                Alto_Max = self.fuente.size(Listado[i])[1]
            self.mouse_up_desplegado.append(False)

        
        self.dim_texto = [Ancho_Max, Alto_Max]
        self.dim_boton = [Ancho_Max + 2*margen, Alto_Max + 2*margen]    # La lista desplegable van a ser N botones, uno abajo del otro 

        for i in range(len(self.Listado)):
            self.poss_botones.append([poss_boton[0], poss_boton[1] + i*self.dim_boton[1]])
            self.poss_textos.append([poss_boton[0]+margen, poss_boton[1]+margen + i*self.dim_boton[1]])


        self.color_texto_out = color_texto_out
        self.color_texto_up = color_texto_up
        self.color_boton_out = color_boton_out
        self.color_boton_up = color_boton_up

        self.ListadoDesplegado = False  # Cuando sea True, se despliega el listado, y cuando es False se muestra el valor seleccionado en 1 solo botón.
        self.Valor = Listado[0]

        
    def EventosListaDesplegable(self):      # Este evento hay que ponerlo dentro del evento "MOUSEBUTTONDOWN"
        if not(self.ListadoDesplegado):
            if self.mouse_up_contraido:
                self.ListadoDesplegado = True
        else:
            for i in range(len(self.Listado)):
                if self.mouse_up_desplegado[i] == True:
                    self.Valor = self.Listado[i]
                    self.ListadoDesplegado = False
                    

    def InsertarBoton(self):
        self.MouseUp()
        if not(self.ListadoDesplegado):     # Cuando no esté el listado desplegado, tenemos que renderizar un botón con la opción seleccionada
            if self.mouse_up_contraido:
                texto = self.fuente.render(self.Valor, True, self.color_texto_up)
                pg.draw.rect(self.juego.ventana, self.color_boton_up, [self.poss_botones[0][0], self.poss_botones[0][1], self.dim_boton[0], self.dim_boton[1]])
            else:
                texto = self.fuente.render(self.Valor, True, self.color_texto_out)
                pg.draw.rect(self.juego.ventana, self.color_boton_out, [self.poss_botones[0][0], self.poss_botones[0][1], self.dim_boton[0], self.dim_boton[1]])
            self.juego.ventana.blit(texto, (self.poss_textos[0][0], self.poss_textos[0][1]))
        else:
            for i in range(len(self.Listado)):
                if self.mouse_up_desplegado[i]:
                    texto = self.fuente.render(self.Listado[i], True, self.color_texto_up)
                    btn = pg.draw.rect(self.juego.ventana, self.color_boton_up, [self.poss_botones[i][0], self.poss_botones[i][1], self.dim_boton[0], self.dim_boton[1]])
                else:
                    texto = self.fuente.render(self.Listado[i], True, self.color_texto_out)
                    btn = pg.draw.rect(self.juego.ventana, self.color_boton_out, [self.poss_botones[i][0], self.poss_botones[i][1], self.dim_boton[0], self.dim_boton[1]])
                self.juego.ventana.blit(texto, (self.poss_textos[i][0], self.poss_textos[i][1]))


    def MouseUp(self):
        if not(self.ListadoDesplegado):
            if self.poss_botones[0][0] <= self.juego.mouse[0] <= self.poss_botones[0][0]+self.dim_boton[0] and self.poss_botones[0][1] <= self.juego.mouse[1] <= self.poss_botones[0][1]+self.dim_boton[1]:
                self.mouse_up_contraido = True
            else:
                self.mouse_up_contraido = False
        else:
            for i in range(len(self.Listado)):
                if self.poss_botones[i][0] <= self.juego.mouse[0] <= self.poss_botones[i][0]+self.dim_boton[0] and self.poss_botones[i][1] <= self.juego.mouse[1] <= self.poss_botones[i][1]+self.dim_boton[1]:
                    self.mouse_up_desplegado[i] = True
                else:
                    self.mouse_up_desplegado[i] = False


class Button_Sprite():      # Es una imágen botón, cuando se presiona hará algo.
    def __init__(self, juego, poss_boton, dir_img_clara, dir_img_oscura):
        self.juego = juego
        self.poss_boton = poss_boton
        self.dir_img_clara = dir_img_clara
        self.dir_img_oscura = dir_img_oscura
        
        self.img_boton_clara = pg.image.load(self.dir_img_clara)
        self.img_boton_oscura = pg.image.load(self.dir_img_oscura)
        
        self.dim_boton = [self.img_boton_clara.get_width(), self.img_boton_clara.get_height()]

        self.mouse_up = False
    
    
    def InsertarBoton(self):
        self.MouseUp()
        if self.mouse_up:
            self.juego.ventana.blit(self.img_boton_clara, (self.poss_boton[0],self.poss_boton[1]))   #La introdusco en el origen de coordenadas.
        else:
            self.juego.ventana.blit(self.img_boton_oscura, (self.poss_boton[0],self.poss_boton[1]))   #La introdusco en el origen de coordenadas.

    def MouseUp(self):
        if self.poss_boton[0] <= self.juego.mouse[0] <= self.poss_boton[0]+self.dim_boton[0] and self.poss_boton[1] <= self.juego.mouse[1] <= self.poss_boton[1]+self.dim_boton[1]: 
            self.mouse_up = True
        else:
            self.mouse_up = False


class Button_SpriteCambiarVentana(Button_Sprite):
    def __init__(self,juego, poss_boton, dir_img_clara, dir_img_oscura, NuevaVentana):
        super().__init__(juego, poss_boton, dir_img_clara, dir_img_oscura)
        self.NuevaVentana = NuevaVentana
    
    def EventosCambiarVentana(self):
        if self.mouse_up:
            self.juego.CambiarDeVentana(self.NuevaVentana)


class Button_SpriteSalir(Button_Sprite):
    def __init__(self, juego, poss_boton, dir_img_clara, dir_img_oscura):
        super().__init__(juego, poss_boton, dir_img_clara, dir_img_oscura)

    def EventosSalirJuego(self):
        if self.mouse_up:
            self.juego.CerrarJuego()


class Button_SpriteTopLow10(Button_Sprite):
    def __init__(self, juego, bot, poss_boton, dir_img_clara, dir_img_oscura, Grafico_A_Mostrar):
        super().__init__(juego, poss_boton, dir_img_clara, dir_img_oscura)
        self.bot = bot
        self.Grafico_A_Mostrar = Grafico_A_Mostrar
    

    def CambiarGrafico_A_Mostrar(self):
        if self.mouse_up:
            self.bot.MostrarGrafico(self.Grafico_A_Mostrar)


class EntryText():
    def __init__(self, juego, poss_boton, ancho_boton, text_i="", color_texto_sin_escribir=GRIS_CLARO, color_texto_escribiendo=WHITE, color_boton_sin_escribir=GRIS_MUYOSCURO, color_boton_escribiendo=GRIS_OSCURO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=20):
        self.juego = juego
        self.poss_boton = poss_boton
        self.ancho_boton = ancho_boton      # El ancho va a ser fijo, por que es cuanto texto voy a querer yo mostrar.
        margen = 5                          # Margen entre el texto y los bordes del boton.
        self.poss_texto = [poss_boton[0] + margen, poss_boton[1] + margen]
        self.dim_boton = [ancho_boton, tamaño_fuente + margen]
        

        self.color_texto_sin_escribir = color_texto_sin_escribir  # Color del texto cuando no está escribiendo.
        self.color_texto_escribiendo = color_texto_escribiendo    # Color del texto cuando está escribiendo.
        self.color_boton_sin_escribir = color_boton_sin_escribir  # Color del texto cuando no está escribiendo.
        self.color_boton_escribiendo = color_boton_escribiendo    # Color del texto cuando está escribiendo.

        self.fuente = pg.font.Font(tipo_fuente, tamaño_fuente)
        self.text = text_i                      # Texto que va a contener el botón

        self.mouse_up = False
        self.esta_escribiendo = False


    def InsertarBoton(self):
        if not(self.esta_escribiendo):
            texto = self.fuente.render(self.text , True , self.color_texto_sin_escribir)
            pg.draw.rect(self.juego.ventana, self.color_boton_sin_escribir, [self.poss_boton[0], self.poss_boton[1], self.dim_boton[0], self.dim_boton[1]])
        else:
            texto = self.fuente.render(self.text , True , self.color_texto_escribiendo)
            pg.draw.rect(self.juego.ventana, self.color_boton_escribiendo, [self.poss_boton[0], self.poss_boton[1], self.dim_boton[0], self.dim_boton[1]])
        self.juego.ventana.blit(texto, (self.poss_texto[0], self.poss_texto[1]))


    def EventosClick_EntryText(self):   # Poner dentro del "if" cuando hay un evento de click.
        self.MouseUp()
        if self.mouse_up and not(self.esta_escribiendo):    # Si el mouse está arriba y no está escribiendo.
            self.esta_escribiendo = True
        elif self.esta_escribiendo:
            self.esta_escribiendo = False


    def EventosTeclas_EntryText(self, event):
        if self.esta_escribiendo and event.key == pg.K_RETURN:
            self.esta_escribiendo = False
        elif self.esta_escribiendo and event.key == pg.K_BACKSPACE:
            self.text = self.text[:-1]      # Le borro el último caracter
        elif self.esta_escribiendo:
            self.text += event.unicode


    def MouseUp(self):
        if self.poss_boton[0] <= self.juego.mouse[0] <= self.poss_boton[0]+self.dim_boton[0] and self.poss_boton[1] <= self.juego.mouse[1] <= self.poss_boton[1]+self.dim_boton[1]: 
            self.mouse_up = True
        else:
            self.mouse_up = False


class EntryText_SoloNum(EntryText):
    def __init__(self, juego, poss_boton, ancho_boton, text_i="", color_texto_sin_escribir=GRIS_CLARO, color_texto_escribiendo=WHITE, color_boton_sin_escribir=GRIS_MUYOSCURO, color_boton_escribiendo=GRIS_OSCURO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=20):
        super().__init__(juego, poss_boton, ancho_boton, text_i="", color_texto_sin_escribir=GRIS_CLARO, color_texto_escribiendo=WHITE, color_boton_sin_escribir=GRIS_MUYOSCURO, color_boton_escribiendo=GRIS_OSCURO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=20)

    def EventosTeclas_EntryText(self, event):
        if self.esta_escribiendo and event.key == pg.K_RETURN:
            self.esta_escribiendo = False
        elif self.esta_escribiendo and event.key == pg.K_BACKSPACE:
            self.text = self.text[:-1]      # Le borro el último caracter
        elif self.esta_escribiendo and (event.unicode in "0123456789"):
            if self.text == "":
                if event.unicode!="0":
                    self.text += event.unicode
            else:
                self.text += event.unicode


class RecuadroConTexto():
    def __init__(self, juego, poss_recuadro, ancho_recuadro, text_i="", color_texto=WHITE, color_recuadro=BLACK):
        self.juego = juego
        self.poss_recuadro = poss_recuadro
        self.ancho_recuadro = ancho_recuadro
        self.text = text_i
        self.color_texto = color_texto
        self.color_recuadro = color_recuadro


class Button_ReiniciarTrivia(Button):
    def __init__(self, juego, trivia, poss_boton, text, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=15):
        super().__init__(juego, poss_boton, text, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, font_path=FUENTE_MINECRAFT, font_size=15)
        self.trivia = trivia
    
    def EventosReiniciarTrivia(self):
        if self.mouse_up and not(self.trivia.Activa):
            self.trivia.ReiniciarTrivia()


class Button_TerminarTrivia(Button):
    def __init__(self, juego, trivia, poss_boton, text, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=15):
        super().__init__(juego, poss_boton, text, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, font_path=FUENTE_MINECRAFT, font_size=15)
        self.trivia = trivia


    def EventosTerminarTrivia(self):
        if self.mouse_up and self.trivia.Activa:
            self.trivia.TerminarTrivia()


class Button_FiltrarPkmn(Button):
        def __init__(self, juego, trivia, poss_boton, text, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, tipo_fuente=FUENTE_MINECRAFT, tamaño_fuente=15):
            super().__init__(juego, poss_boton, text, color_texto_out=GRIS_CLARO, color_texto_up=WHITE, color_boton_out=VIOLETA_OSCURO, color_boton_up=VIOLETA_CLARO, font_path=FUENTE_MINECRAFT, font_size=15)
            self.trivia = trivia


        def EventosFiltrarPkmn(self):
            if self.mouse_up and not(self.trivia.Activa):
                self.trivia.FiltrarBBDD()
"""