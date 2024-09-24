viktor_available = False
try:
    from viktor.geometry import Point, Line, Material, Extrusion, TransformableObject
except ImportError:

    class Point:
        def __init__(self, x: float, y: float, z: float = 0):
            pass

    class Line:
        def __init__(self, start: Point, end: Point):
            pass

            pass

    class Material:
        pass

    class Extrusion:
        def __init__(
            self,
            profile: list[Point],
            line: Line,
            profile_rotation: float = 0,
            Material: Material | None = None,
            identifier: None | str = None,
        ):
            pass

    class TransformableObject:
        pass
