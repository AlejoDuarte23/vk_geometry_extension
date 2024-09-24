def generate_pfc_coordinates(web_height, flange_width, web_thickness, flange_thickness):
    """
    Generates the coordinates for a PFC (C-shaped) profile.
    """
    # Calculate key positions
    x0 = 0
    x1 = web_thickness
    x2 = flange_width + web_thickness

    y0 = 0
    y1 = flange_thickness
    y2 = web_height - flange_thickness
    y3 = web_height

    # Define the points in clockwise order
    points = [
        {"x": x0, "y": y0},  # Bottom left corner
        {"x": x2, "y": y0},  # Bottom right corner
        {"x": x2, "y": y1},  # Up to bottom flange thickness
        {"x": x1, "y": y1},  # Left to web thickness
        {"x": x1, "y": y2},  # Up along web
        {"x": x2, "y": y2},  # Right to top flange
        {"x": x2, "y": y3},  # Up to top
        {"x": x0, "y": y3},  # Left to top left corner
        {"x": x0, "y": y2},  # Down to top flange thickness
        {"x": x1, "y": y2},  # Right to web thickness
        {"x": x1, "y": y1},  # Down along web
        {"x": x0, "y": y1},  # Left to bottom flange
        {"x": x0, "y": y0},  # Close the loop
    ]

    return points
