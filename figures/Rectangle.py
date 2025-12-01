class Rectangle():
    def __init__(self, width_value, height_value):
        self.width = width_value
        self.height = height_value
    figure = "rectangle"
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width_value):
        if width_value < 0:
            self._width = 1
        else:
            self._width = width_value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height_value):
        if height_value < 0:
            self._height = 1
        else:
            self._height = height_value

    def get_outer_rect(self):
        return [float(self.width), float(self.height)]