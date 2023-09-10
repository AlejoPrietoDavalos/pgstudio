from src.interface.ui import UI
from .router import Router
from src.interface.buttons import Buttons, Events
import pygame as pg

def loop_main_menu(scene:str, ui:UI, ROUTER:Router):
    ui.btns.load_scene_buttons(scene, [
        Buttons.Simple(False, "prueba", Events.change_scene, 30, 30, ui.win, ui.ctrls, "1er boton"),
        Buttons.Simple(True, "prueba2", Events.change_scene, 30, 60, ui.win, ui.ctrls, "2do boton"),
        Buttons.Simple(False, "prueba3", Events.change_scene, 30, 90, ui.win, ui.ctrls, "3er boton"),
        Buttons.Simple(True, "prueba4", Events.change_scene, 30, 120, ui.win, ui.ctrls, "4to boton")
    ])

    while ROUTER.is_active_scene(scene):
        ui.ctrls.update_controls()
        ui.wallpaper.draw_wallpaper()
        ui.btns.draw_all_btns()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ROUTER.close_the_game()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                for btn in ui.btns.get():
                    btn.event()
                    


        ui.update_screen()




        