class Rook:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def can_move_to(self, row, col):
        return (
            0 <= row < 8
            and 0 <= col < 8
            and (row == self.row or col == self.col)
        )

    def move_to(self, row, col):
        if not self.can_move_to(row, col):
            return False
        self.row, self.col = row, col
        return True


rook = Rook(0, 0)
print(rook.move_to(0, 5))  # True
print(rook.move_to(2, 3))  # False