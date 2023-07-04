import pygame
import os
import sys
import random

class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        super().__init__()
        self.loadImage(x, y, filename)

    def loadImage(self, x, y, filename):
        path = os.getcwd()
        filenames = [f for f in os.listdir(path) if f.endswith('.png')]
        imagelist = []
        for name in filenames:
            imagename = os.path.splitext(name)[0]
            imagelist.append(pygame.image.load(os.path.join(path, name)).convert_alpha())
            random.shuffle(imagelist)
        for img in imagelist:
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y - self.rect.height

    def moveBy(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class Card(ImageSprite):
    def __init__(self, suit, value, filename="", x=0, y=0):
        self.suit = suit[0].lower()
        self.value = value
        if filename == "":
            self._filename = str(value) + self.suit + ".gif"
        else:
            self._filename = filename
        super().__init__(x, y, self._filename)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def update(self):
        if self.dragging:
            # Update the card's position while dragging
            self.rect.x = pygame.mouse.get_pos()[0] - self.offset_x
            self.rect.y = pygame.mouse.get_pos()[1] - self.offset_y






    def getSuit(self):
        if self.suit == 'h':
            return "Hearts"
        elif self.suit == 's':
            return "Spades"
       
        elif self.suit == 'c':
            return "Clubs"
        elif self.suit == 'd':
            return "Diamonds"
        else:
            return ""

    def getValue(self):
        return self.value

    def getFilename(self):
        return self.filename

    def getWidth(self):
        return self.rect.width

    def getHeight(self):
        return self.rect.height

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def __gt__(self, card):
        if self.value == 1 and card.getValue() != 1:
            return True
        elif card.getValue() == 1 and self.value != 1:
            return False
        return self.value > card.getValue()

    def __lt__(self, card):
        if card.getValue() == 1 and self.value != 1:
            return True
        elif self.value == 1 and card.getValue() != 1:
            return False
        return self.value < card.getValue()

    def eq(self, card):
        return card.getValue() == self.value

    def __repr__(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = str(self.value)
        return val + " of " + self.getSuit()


# Initialize Pygame
pygame.init()

# Set the width and height of the screen
screen_width = 1800
screen_height = 800
x=0
y=0
# Create the screen surface
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Card Game")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define the path to the card images
path = os.getcwd()

# Create a list to hold the card sprites
card_sprites = []

# Load the card images and create card sprite objects
filenames = [f for f in os.listdir(path) if f.endswith('.png')]
for i, filename in enumerate(filenames):
    card_sprite = Card("suit", i+1, os.path.join(path, filename))
    card_sprite.getSuit()
    print(card_sprite)
    y+=20
    x+=15
    card_sprite.move(x + i*x, y)  # Set the position of each card sprite
   
    card_sprites.append(card_sprite)
    random.shuffle(card_sprites)
    
# Main game loop
loop = True
while loop:
    # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        loop = False

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button pressed
            for card_sprite in card_sprites:
                if card_sprite.rect.collidepoint(event.pos):
                    card_sprite.dragging = True
                    card_sprite.offset_x = event.pos[0] - card_sprite.rect.x
                    card_sprite.offset_y = event.pos[1] - card_sprite.rect.y

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:  # Left mouse button released
            for card_sprite in card_sprites:
                if card_sprite.dragging:
                    card_sprite.dragging = False
                    # Perform additional actions based on the drop position

    elif event.type == pygame.MOUSEMOTION:
        for card_sprite in card_sprites:
            if card_sprite.dragging:
                card_sprite.rect.x = event.pos[0] - card_sprite.offset_x
                card_sprite.rect.y = event.pos[1] - card_sprite.offset_y


    screen.fill((0, 155, 0))

  
    # Blit the card sprites onto the screen
    for card_sprite in card_sprites:
        screen.blit(card_sprite.image, card_sprite.rect)

       # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
