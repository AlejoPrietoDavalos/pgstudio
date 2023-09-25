from pgstudio.geometry.datastore import Point

class TestPointHowInstanciate:
    def test_xy(self):
        xy = (3,2)
        p_from_xy = Point.from_xy(xy=xy)
        x, y = p_from_xy.x, p_from_xy.y
        assert x>=0 and y>=0
        assert x,y == p_from_xy.xy
        assert isinstance(p_from_xy, Point)
    
    
        