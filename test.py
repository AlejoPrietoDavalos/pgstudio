from pgstudio.geometry import shp, Point, LineString, Polygon, BBox


p1 = Point(shp.Point(3,5))
p2 = Point(shp.Point(1,2))
line = shp.LineString([
    shp.Point(1,7),
    shp.Point(2,6),
    shp.Point(3,5),
    shp.Point(4,4),
    shp.Point(5,3),
    shp.Point(6,2),
    shp.Point(7,1)
])

pol = shp.Polygon([
    shp.Point(1,7),
    shp.Point(2,6),
    shp.Point(3,5),
    shp.Point(4,4),
    shp.Point(5,3),
    shp.Point(6,2),
    shp.Point(7,1)
])


l = LineString(line)
pol = Polygon(pol)
box = BBox(p1, 6, 4)

box = BBox.from_box([5,2,10,20])

print(type(box))
print(box.pt_ref)
print(box.box)
print(box.coords)
print(box.xywh)
