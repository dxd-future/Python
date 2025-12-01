class Circle():
    def __init__(self, radius_value):
        self.radius = radius_value
    figure = "circle"
    def get_outer_rect(self):
        return [self.radius, self.radius]