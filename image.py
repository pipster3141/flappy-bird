import pygame
import os

class Image:

    def __init__(self, image_file_name):
        if os.path.exists(image_file_name):
            self.mImage = pygame.image.load(image_file_name)
            self.mWidth = self.mImage.get_width()
            self.mHeight = self.mImage.get_height()
            self.mRotation = 0.0
            self.mDisplayImage = self.mImage
        else:
            self.mImage = None
        return

    def getWidth(self):
        return self.mWidth
    
    def getHeight(self):
        return self.mHeight

    def getRotation(self):
        return self.mRotation

    def resize(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mImage = pygame.transform.scale(self.mImage, (self.mWidth, self.mHeight))
        return
        
    def setRotation(self, degrees):
        self.mDisplayImage = pygame.transform.rotate(self.mImage, degrees)
        self.mRotation = degrees
        self.mWidth  = self.mDisplayImage.get_width()
        self.mHeight = self.mDisplayImage.get_height()
        return
    
    def draw(self, surface, x, y):
        if self.mImage:
            surface.blit(self.mDisplayImage, (int(x-self.mWidth/2.), int(y-self.mHeight/2.)))
        return
