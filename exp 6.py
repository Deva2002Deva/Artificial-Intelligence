class VacuumCleaner:
    def __init__(self, grid, start_position):
        self.grid = grid
        self.position = start_position
        self.cleaned_rooms = 0

    def is_dirty(self, position):
        x, y = position
        return self.grid[x][y] == "Dirty"

    def clean(self, position):
        x, y = position
        if self.grid[x][y] == "Dirty":
            self.grid[x][y] = "Clean"
            self.cleaned_rooms += 1
            print(f"Cleaned room at position {position}")

    def move(self, direction):
        x, y = self.position
        if direction == "up" and x > 0:
            self.position = (x - 1, y)
        elif direction == "down" and x < len(self.grid) - 1:
            self.position = (x + 1, y)
        elif direction == "left" and y > 0:
            self.position = (x, y - 1)
        elif direction == "right" and y < len(self.grid[0]) - 1:
            self.position = (x, y + 1)
        print(f"Moved {direction} to position {self.position}")

    def run(self):
        directions = ["up", "down", "left", "right"]
        while self.cleaned_rooms < len(self.grid) * len(self.grid[0]):
            if self.is_dirty(self.position):
                self.clean(self.position)
            for direction in directions:
                self.move(direction)
                if self.is_dirty(self.position):
                    self.clean(self.position)

if __name__ == "__main__":
    grid = [
        ["Dirty", "Dirty", "Clean"],
        ["Clean", "Dirty", "Dirty"],
        ["Dirty", "Clean", "Clean"]
    ]
    start_position = (1, 1)
    vacuum = VacuumCleaner(grid, start_position)
    vacuum.run()

    print("Final state of the grid:")
    for row in grid:
        print(row)
