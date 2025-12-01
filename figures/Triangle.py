class Triangle():
    def __init__(self, len1_value, len2_value, len3_value):
        self.len1 = len1_value
        self.len2 = len2_value
        self.len3 = len3_value
    figure = "triangle"
    def get_semiPerimetr(self):
        return (self.len1 + self.len2 + self.len3) / 2
    def get_height(self):
        return (2/self.len1)*(self.get_semiPerimetr()*(self.get_semiPerimetr() - self.len1)*(self.get_semiPerimetr() - self.len2)*(self.get_semiPerimetr() - self.len3))**0.5
    def get_outer_rect(self):
        return [float(self.len1), float(self.get_height())]