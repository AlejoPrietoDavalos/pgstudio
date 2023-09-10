from PIL import ImageColor
import yaml
import os

class _Wallpapers():
    """ Cada escenario tiene asociado un conjunto de wallpapers. Cuando se
        ingresa a un escenario nuevo, el programa renderiza primero al wallpaper
        que aparece como default, el resto son wallpapers válidos para
        ese escenario, y pueden ser usados en cualquier momento."""
    
    _BASE_WALLPAPER_PATH = os.path.join("resources", "sprites", "wallpapers")
    _WALLPAPER_ROUTING_PATH = os.path.join(_BASE_WALLPAPER_PATH, "wallpaper_routing.yaml")
    

    def __init__(self):
        self.wallpapers_path = {}       # Se guardan solo los wallpapers del escenario en que estamos.
    
    def load_wallpaper_paths(self, scene:str):
        """ Implementar luego, la idea sería guardar todos los wallpapers de
            las escenas en un archivo .yaml, cuando se pasa de escena, se cargan
            los wallpapers de esa escena, y se guardan en memoria sus nombres
            para acceder a ellos mas adelante."""
        # Devolvemos solo los wallpapers pertenecientes a la escena en cuestión.
        self.wallpapers_path = yaml.load(open(self._WALLPAPER_ROUTING_PATH, 'r'), yaml.loader.SafeLoader)[scene]
        for key in self.wallpapers_path:
            self.wallpapers_path[key] = os.path.join(self._BASE_WALLPAPER_PATH, self.wallpapers_path[key])



class _Colors():
    """ Guardamos todos los colores que vayamos a utilizar en hexadecimal.
        Luego vamos a convertirlos a una tupla RGB por que es lo que usa pygame.
        Algunos nombres: https://htmlcolorcodes.com/color-names/"""
    def __init__(self):
        self._COLOR = {
            "Black":            "#000000",
            "White":            "#ffffff",
            "Red":              "#FF0000",
            "Orange":           "#FFA500",
            "Yellow":           "#FFFF00",
            "Pink":             "#FFC0CB",
            "Magenta":          "#FF00FF",
            "Violet":           "#EE82EE",
            "Purple":           "#800080",
            "Blue":             "#0000FF",
            "Green":            "#008000",
            "Turquoise":        "#40E0D0",
            "Brown":            "#A52A2A",
            "Gray":             "#808080",
        }
        self._COLOR.update({ #-----> Red
            "DarkRed":          "#8B0000",
            "FireBrick":        "#B22222",
            "Crimson":          "#DC143C",
            "IndianRed":        "#CD5C5C",
            "LightCoral:        "#F08080",
            "Salmon":           "#FA8072",
            "DarkSalmon:        "#E9967A",
            "LightSalmon":      "#FFA07A",
        })
        self._COLOR.update({ #-----> Orange
            "OrangeRed":        "#FF4500",
            "Tomato":           "#FF6347",
            "Coral":            "#FF7F50",
            "DarkOrange":       "#FF8C00",
            "LightSalmon":      "#FFA07A",
        })
        self._COLOR.update({ #-----> Yellow
            "DarkKhaki":        "#BDB76B",
            "Khaki":            "#F0E68C",
            "PaleGoldenrod":    "#EEE8AA",
            "PeachPuff":        "#FFDAB9",
            "Moccasin":         "#FFE4B5",
            "PapayaWhip":       "#FFEFD5",
            "LemonChiffon":     "#FFFACD",
            "LightYellow":      "#FFFFE0",
        })
        self._COLOR.update({ #-----> Pink
            "MediumVioletRed":  "#C71585",
            "DeepPink":         "#FF1493",
            "HotPink":          "#FF69B4",
            "PaleVioletRed":    "#DB7093",
            "LightPink":        "#FFB6C1",
        })
        self._COLOR.update({ #-----> Purple
            "Indigo":           "#4B0082",
            "DarkSlateBlue":    "#483D8B",
            "RebeccaPurple":    "#663399",
            "MediumPurple":     "#9370DB",
            "MediumSlateBlue":  "#7B68EE",
            "SlateBlue":        "#6A5ACD",
            "DarkMagenta":      "#8B008B",
            "DarkOrchid":       "#9932CC",
            "DarkViolet":       "#9400D3",
            "BlueViolet":       "#8A2BE2",
            "Fuchsia":          "#FF00FF",
            "MediumOrchid":     "#BA55D3",
            "Orchid":           "#DA70D6",
            "Plum":             "#DDA0DD",
            "Thistle":          "#D8BFD8",
            "Lavender":         "#E6E6FA",
        })
        self._COLOR.update({ #-----> Green
            "DarkGreen":        "#006400",
            "SeaGreen":         "#2E8B57",
            "MediumSeaGreen":   "#3CB371",
            "ForestGreen":      "#228B22",
            "DarkOliveGreen":   "#556B2F",
            "Olive":            "#808000",
            "OliveDrab":        "#6B8E23",
            "LimeGreen":        "#32CD32",
            "GreenYellow":      "#ADFF2F",
            "Chartreuse":       "#7FFF00",
            "LawnGreen":        "#7CFC00",
            "Lime":             "#00FF00",
            "SpringGreen":      "#00FF7F",
            "PaleGreen":        "#98FB98",
            "LightGreen":       "#90EE90",
            "DarkSeaGreen":     "#8FBC8B",
            "YellowGreen":      "#9ACD32",
            "DarkCyan":         "#008B8B",
            "Teal":             "#008080",
            "LightSeaGreen":    "#20B2AA",
            "MediumAquamarine": "#66CDAA",
        })
        self._COLOR.update({ #-----> Blue
            "MidnightBlue":     "#191970",
            "Navy":             "#000080",
            "DarkBlue":         "#00008B",
            "MediumBlue":       "#0000CD",
            "MediumSlateBlue":  "#7B68EE",
            "RoyalBlue":        "#4169E1",
            "CornflowerBlue":   "#6495ED",
            "DodgerBlue":       "#1E90FF",
            "SteelBlue":        "#4682B4",
            "CadetBlue":        "#5F9EA0",
            "DeepSkyBlue":      "#00BFFF",
            "DarkTurquoise":    "#00CED1",
            "MediumTurquoise":  "#48D1CC",
            "Aqua":             "#00FFFF",
            "Cyan":             "#00FFFF",
            "Aquamarine":       "#7FFFD4",
            "PaleTurquoise":    "#AFEEEE",
            "LightCyan":        "#E0FFFF",
            "LightSteelBlue":   "#B0C4DE",
            "PowderBlue":       "#B0E0E6",
            "LightBlue":        "#ADD8E6",
            "SkyBlue":          "#87CEEB",
            "LightSkyBlue":     "#87CEFA",
        })
        self._COLOR.update({ #-----> Brown
            "Maroon":           "#800000",
            "Sienna":           "#A0522D",
            "SaddleBrown":      "#8B4513",
            "RosyBrown":        "#BC8F8F",
            "Chocolate":        "#D2691E",
            "DarkGoldenrod":    "#B8860B",
            "Peru":             "#CD853F",
            "Goldenrod":        "#DAA520",
            "SandyBrown":       "#F4A460",
            "BurlyWood":        "#DEB887",
            "Tan":              "#D2B48C",
            "Cornsilk":         "#FFF8DC",
            "BlanchedAlmond":   "#FFEBCD",
            "Bisque":           "#FFE4C4",
            "NavajoWhite":      "#FFDEAD",
            "Wheat":            "#F5DEB3",
        })
        self._COLOR.update({ #-----> Gray
            "DarkSlateGray":    "#2F4F4F",
            "SlateGray":        "#708090",
            "LightSlateGray":   "#778899",
            "DimGray":          "#696969",
            "DarkGray":         "#A9A9A9",
            "Silver":           "#C0C0C0",
            "LightGray":        "#D3D3D3",
            "Gainsboro":        "#DCDCDC",
        })
        self._COLOR = {c_name: self._hex_to_rgb(self._COLOR[c_name]) for c_name in self._COLOR}

    def _hex_to_rgb(self, hex_color:str) -> tuple:
        return ImageColor.getcolor(hex_color, "RGB")

