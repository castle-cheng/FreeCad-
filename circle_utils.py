# circle_utils.py
import FreeCAD as App
import Part

def create_circle(center=(0, 0, 0), radius=10.0, name="Circle"):
    circle_geom = Part.Circle()
    circle_geom.Center = App.Vector(*center)
    circle_geom.Radius = radius
    circle_shape = circle_geom.toShape()
    obj = App.ActiveDocument.addObject("Part::Feature", name)
    obj.Shape = circle_shape
    App.ActiveDocument.recompute()
    return obj