import pygame
from random import randint
GREEN = (0, 255, 0)
BLACK = (0,0,0)
DARK_GREEN = (0, 153, 0)
MEDIUM_GREEN = (128, 255, 128)
LIGHT_GREEN = (179, 255, 179)

class Bar:

    def __init__(self,width,height):
        self.mHeight = height
        self.mWidth = width
        self.mShift = 0
        self.mVariation = randint(-100,100)
        return

    def getHeight(self):
        return self.mHeight

    def getWidth(self):
        return self.mWidth

    def getShift(self):
        return self.mShift

    def getVariation(self):
        return self.mVariation

    def draw(self, surface):
        topRect = pygame.Rect(self.mWidth+self.mShift, -4, 40, 200-self.mVariation)
        botRect = pygame.Rect(self.mWidth+self.mShift, self.mHeight, 40, -200-self.mVariation)
        topRectDarkShadow = pygame.Rect(self.mWidth+self.mShift+30, -4, 10, 200-self.mVariation)
        botRectDarkShadow = pygame.Rect(self.mWidth+self.mShift+30, self.mHeight, 10, -200-self.mVariation)
        topRectMediumShadow = pygame.Rect(self.mWidth+self.mShift, -4, 10, 200-self.mVariation)
        botRectMediumShadow = pygame.Rect(self.mWidth+self.mShift, self.mHeight, 10, -200-self.mVariation)
        topRectLightShadow = pygame.Rect(self.mWidth+self.mShift, -4, 5, 200-self.mVariation)
        botRectLightShadow = pygame.Rect(self.mWidth+self.mShift, self.mHeight, 5, -200-self.mVariation)
        pygame.draw.rect(surface, GREEN, topRect, 0)
        pygame.draw.rect(surface, GREEN, botRect, 0)
        pygame.draw.rect(surface, DARK_GREEN, topRectDarkShadow, 0)
        pygame.draw.rect(surface, DARK_GREEN, botRectDarkShadow, 0)
        pygame.draw.rect(surface, MEDIUM_GREEN, topRectMediumShadow, 0)
        pygame.draw.rect(surface, MEDIUM_GREEN, botRectMediumShadow, 0)
        pygame.draw.rect(surface, LIGHT_GREEN, topRectLightShadow, 0)
        pygame.draw.rect(surface, LIGHT_GREEN, botRectLightShadow, 0)
        pygame.draw.rect(surface, BLACK, topRect, 2)
        pygame.draw.rect(surface, BLACK, botRect, 2)
        topRectBarrel = pygame.Rect(self.mWidth+self.mShift-2, 180-self.mVariation, 44, 20)
        botRectBarrel = pygame.Rect(self.mWidth+self.mShift-2, self.mHeight-180-self.mVariation, 44, -20)
        topRectDarkShadowBarrel = pygame.Rect(self.mWidth+self.mShift+32, 180-self.mVariation, 10, 20)
        botRectDarkShadowBarrel = pygame.Rect(self.mWidth+self.mShift+32, self.mHeight-180-self.mVariation, 10, -20)
        topRectMediumShadowBarrel = pygame.Rect(self.mWidth+self.mShift-2, 180-self.mVariation, 10, 20)
        botRectMediumShadowBarrel = pygame.Rect(self.mWidth+self.mShift-2, self.mHeight-180-self.mVariation, 10, -20)
        topRectLightShadowBarrel = pygame.Rect(self.mWidth+self.mShift-2, 180-self.mVariation, 5, 20)
        botRectLightShadowBarrel = pygame.Rect(self.mWidth+self.mShift-2, self.mHeight-180-self.mVariation, 5, -20)
        pygame.draw.rect(surface, GREEN, topRectBarrel, 0)
        pygame.draw.rect(surface, GREEN, botRectBarrel, 0)
        pygame.draw.rect(surface, DARK_GREEN, topRectDarkShadowBarrel, 0)
        pygame.draw.rect(surface, DARK_GREEN, botRectDarkShadowBarrel, 0)
        pygame.draw.rect(surface, MEDIUM_GREEN, topRectMediumShadowBarrel, 0)
        pygame.draw.rect(surface, MEDIUM_GREEN, botRectMediumShadowBarrel, 0)
        pygame.draw.rect(surface, LIGHT_GREEN, topRectLightShadowBarrel, 0)
        pygame.draw.rect(surface, LIGHT_GREEN, botRectLightShadowBarrel, 0)
        pygame.draw.rect(surface, BLACK, topRectBarrel, 2)
        pygame.draw.rect(surface, BLACK, botRectBarrel, 2)
        return

    def evolve(self):
        self.mShift -= 2
        return
        
