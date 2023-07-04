def __init__(self, suit, value, filename="", x=0, y=0):
    # ...existing code...

    self.dragging = False
    self.offset_x = 0
    self.offset_y = 0

def update(self):
    if self.dragging:
        # Update the card's position while dragging
        self.rect.x = pygame.mouse.get_pos()[0] - self.offset_x
        self.rect.y = pygame.mouse.get_pos()[1] - self.offset_y
