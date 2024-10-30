class Ship:
    def __init__(self, name, size, initial_pos, orientation="horizontal"):
        self.name = name
        self.size = size
        self.orientation = orientation
        self.sunk = False
        self.coordinates = self.generate_coordinates(initial_pos)
    
    def generate_coordinates(self, initial_pos):
        x, y = initial_pos
        coordinates = []
        for i in range(self.size):
            if self.orientation == "horizontal":
                new_y = y + i
                new_x = x
            elif self.orientation == "vertical":
                new_x = x + i
                new_y = y
            else:
                raise ValueError("Orientação inválida. Use 'horizontal' ou 'vertical'.")
            
            if 0 <= new_x < 10 and 0 <= new_y < 10:
                coordinates.append((new_x, new_y))
            else:
                return []
        return coordinates