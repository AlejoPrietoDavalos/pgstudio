
'''
class BBox(ABC):
    def __init__(self, bbox: BBoxList):
        assert isinstance(bbox, list) and len(bbox)==4 \
            and all(isinstance(c, int) for c in bbox)
        self.bbox = bbox
    
    @property
    def x(self) -> int: return self.bbox[0]
    @property
    def y(self) -> int: return self.bbox[1]
    @property
    def w(self) -> int: return self.bbox[2]
    @property
    def h(self) -> int: return self.bbox[3]

    def is_point_inside(self, x_y: tuple[int, int]) -> bool:
        """ True si el punto se encuentra dentro."""
        print(x_y)
        return (self.x <= x_y[0] <= self.x + self.w) and \
               (self.y <= x_y[1] <= self.y + self.h)


class BoxDrawable(BBox, Drawable):
    # FIXME: Chequear 3 ints.
    def __init__(self, bbox: BBoxList, color_fill: tuple[int, int, int]):
        super().__init__(bbox)
        self.color_fill = color_fill
    
    def draw(self) -> None:
        pg.draw.rect(self.win, self.color_fill, self.bbox)
    
    def move(self, bbox_delta: BBoxList) -> None:
        self.bbox = [c+c_delta for c, c_delta in zip(self.bbox, bbox_delta)]


class BoxClickable(BBox, Clickable, ABC):
    @property
    def is_mouse_up(self) -> bool:
        return self.is_point_inside(pg.mouse.get_pos())


class BoxPrinter(BoxClickable):
    def __init__(self, bbox: BBoxList):
        super().__init__(bbox)
    
    @if_mouse_up
    def on_click(self) -> None:
        print("algo.")
    
    def draw(self) -> None:
        pg.draw.rect(self.win, self.color_fill, self.bbox)
'''
