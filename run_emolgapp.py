from emolgapp.main_app import EmolgApp
from pgstudio.config import ConfigApp


game_cfg = ConfigApp(**{
    "app_name": "EmolgApp",
    "res": (800, 600),
    "fps": 60
})

pgapp = EmolgApp(game_cfg)
pgapp.run_app()