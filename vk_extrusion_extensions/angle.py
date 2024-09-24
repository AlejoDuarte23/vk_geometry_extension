from mock_viktor import Extrusion, Line, Material


class AngleExtrusion(Extrusion):
    def __init__(
        self,
        vertical_leg_length: float,
        horizontal_leg_length: float,
        thickness: float,
        line: Line,
        profile_rotation=float,
        material=Material | None,
        identifier=str | None,
    ) -> Extrusion:
        profile_points = self._angle_polygon(
            vertical_leg_lenght=vertical_leg_length,
            horizontal_leg_length=horizontal_leg_length,
            thickness=thickness,
        )
        super().__init__(
            profile=profile_points,
            line=line,
            profile_rotation=profile_rotation,
            material=material,
            identifier=identifier,
        )

    @classmethod
    def _angle_polygon(self, vertical_leg_lenght, horizontal_leg_length, thickness):
        """
        Generates the coordinates for an Unequal Angle (L-shaped) profile.
        """
        x0, y0 = 0, 0  # Origin
        points = [
            {"x": x0, "y": y0},  # Origin
            {"x": x0, "y": vertical_leg_lenght},
            {"x": thickness, "y": vertical_leg_lenght},
            {"x": thickness, "y": thickness},
            {"x": horizontal_leg_length, "y": thickness},
            {"x": horizontal_leg_length, "y": y0},
            {"x": x0, "y": y0},
        ]
        return points
