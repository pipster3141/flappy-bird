import pygame
import image
from image import Image

class Background:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mImage = image.Image("background_image.png")
        return

    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, (0,0,0), rect, 0)
        self.mImage.draw(surface, 300, 250)
        return
