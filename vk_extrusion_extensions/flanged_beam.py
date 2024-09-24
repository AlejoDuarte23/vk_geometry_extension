from mock_viktor import Extrusion, Point, Line, Material


class IBeamExtrusion(Extrusion):
    def __init__(
        self,
        web_height: float,
        flange_width: float,
        web_thickness: float,
        flange_thickness: float,
        line: Line,
        profile_rotation=float,
        material=Material | None,
        identifier=str | None,
    ) -> Extrusion:
        # Generate the profile points
        profile_points = self._generate_i_shape_profile(
            web_height, flange_width, web_thickness, flange_thickness
        )
        # Initialize the Extrusion with the generated profile
        super().__init__(
            profile_points,
            line,
            profile_rotation=profile_rotation,
            material=material,
            identifier=identifier,
        )

    @staticmethod
    def _i_shape_polygon(web_height, flange_width, web_thickness, flange_thickness):
        """
        Generates the coordinates for an I-shaped beam profile.
        """
        # Calculate key x and y positions
        x1 = -flange_width / 2
        x2 = -web_thickness / 2
        x3 = web_thickness / 2
        x4 = flange_width / 2

        y1 = web_height / 2 + flange_thickness
        y2 = web_height / 2
        y3 = -web_height / 2
        y4 = -web_height / 2 - flange_thickness

        # Define the points in clockwise order
        points = [
            Point(x=x1, y=y1),  # Top left corner of top flange
            Point(x=x4, y=y1),  # Top right corner of top flange
            Point(x=x4, y=y2),  # Right edge of top flange
            Point(x=x3, y=y2),  # Top right of web
            Point(x=x3, y=y3),  # Bottom right of web
            Point(x=x4, y=y3),  # Right edge of bottom flange
            Point(x=x4, y=y4),  # Bottom right corner of bottom flange
            Point(x=x1, y=y4),  # Bottom left corner of bottom flange
            Point(x=x1, y=y3),  # Left edge of bottom flange
            Point(x=x1, y=y4),  # Bottom left corner of bottom flange
            Point(x=x1, y=y3),  # Left edge of bottom flange
            Point(x=x2, y=y3),  # Bottom left of web
            Point(x=x2, y=y2),  # Top left of web
            Point(x=x1, y=y2),  # Left edge of top flange
            Point(x=x1, y=y1),  # Close the loop
        ]
        return points
