import pygame
import image
from image import Image

class Ball:

    def __init__(self,width,height):
        self.mHeight = height/2
        self.mWidth = width/3
        self.mGravity = 1
        self.mGravityMultiplier = 1.2
        self.mMomentum = 0
        self.mWingCount = 0
        self.mImageUp = image.Image("bird_states/up_flap_bird.png")
        self.mImageNeutral = image.Image("bird_states/neutral_flap_bird.png")
        self.mImageDown = image.Image("bird_states/down_flap_bird.png")
        self.mCurrentImage = self.mImageDown
        self.mImageRotation = 0
        return

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getMomentum(self):
        return self.mMomentum

    def setWingCount(self):
        self.mWingCount += 1
        if self.mWingCount == 30:
            self.mWingCount = 0
        return True
    
    def flip(self,value):
        self.mCurrentImage.setRotation(value)

    def draw(self, surface):
        if self.mWingCount >= 20:
            self.mCurrentImage = self.mImageUp
        elif self.mWingCount >= 10:
            self.mCurrentImage = self.mImageNeutral
        elif self.mWingCount >= 0:
            self.mCurrentImage = self.mImageDown
        self.mCurrentImage.draw(surface, self.mWidth, self.mHeight-self.mMomentum)
        return

    def flap(self,value):
        self.mMomentum += value
        self.mImageRotation = 15
        self.mGravityMultiplier = 1
        self.mGravity = 1.2
        return

    def evolve(self):
        self.setWingCount()
        self.mGravity *= self.mGravityMultiplier
        self.mGravityMultiplier *= 1.01
        if self.mGravity > 8:
            self.mGravity = 8
        self.mMomentum -= self.mGravity
        self.mImageRotation -= 1.5
        self.flip(self.mImageRotation)
        return
