import pygame
from random import *
import math
from background import Background
from ball import Ball
from bar import Bar
from text import Text
from sound import Sound

class Collector:
    
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mBackground = Background(width, height)
        self.mBall = Ball(width, height)
        self.mBars = []
        self.mBars.append(Bar(width, height))
        self.mBars[0].evolve()
        self.mScore = 0
        self.mGameStart = False
        self.mEZGame = False
        self.mEZText = Text("EZ MODE",self.mWidth/2,40)
        self.mGameStartTextTop = Text("Press 'W' to flap",self.mWidth/2,self.mHeight/3)
        self.mGameStartTextBot = Text("Press 'E' for EZ Mode",self.mWidth/2,self.mHeight/3+35)
        self.mScoreText = Text(str(self.mScore),self.mWidth/10-20,self.mHeight/10-20)
        self.mGameOverTextTop = Text("GAME OVER NERD",self.mWidth/2,self.mHeight/3)
        self.mGameOverTextBot = Text("Press 'A' to play again",self.mWidth/2,self.mHeight/3+35)
        self.mGameOver = False
        self.mFlapSound = Sound("sounds/flap.wav")
        self.mPipeSound = Sound("sounds/pipe_sound.wav")
        self.mHitSound = Sound("sounds/hit.wav")
        self.mThemeSong = Sound("sounds/theme_song.wav")
        self.mThemePlaying = False
        self.mThemeSong.setVolume(.5)
        self.mWings = 0
        return

    def getGameOver(self):
        return self.mGameOver

    def getGameStart(self):
        return self.mGameStart

    def setEZGame(self):
        self.mEZGame = True
        return True

    def stopMusic(self):
        self.mThemeSong.stop()

    def draw(self, surface):
        self.mBackground.draw(surface)
        if not self.mGameStart:
            self.mGameStartTextTop.draw(surface)
            self.mGameStartTextBot.draw(surface)
        if self.mEZGame:
            self.mEZText.draw(surface)
        for bar in self.mBars:
            bar.draw(surface)

        self.mBall.draw(surface)
        self.mScoreText.draw(surface)
        if self.mGameOver:
            self.mGameOverTextTop.draw(surface)
            self.mGameOverTextBot.draw(surface)
        return

    def flap(self):
        self.mGameStart = True
        self.mBall.flap(30)
        if self.mEZGame:
            self.mBall.flap(10)
        self.mFlapSound.play()
        return

    def EZGame(self):
        self.mEZGame = True

    def groundCollide(self):
        if self.mBall.getHeight() - self.mBall.getMomentum() > 490 or self.mBall.getHeight() - self.mBall.getMomentum() < 5:
            return True
        return False

    def barCollide(self):
        for bar in self.mBars:
            if abs(bar.getWidth() + bar.getShift() + 20 - self.mBall.getWidth()) <= 34:
                if abs(self.mHeight - (self.mHeight - (210+bar.getVariation()))) >= abs(self.mHeight - (self.mHeight/2 - self.mBall.getMomentum())):
                    return True
                elif abs(0 - (0 - (200-bar.getVariation()))) >= abs(0 - (self.mHeight/2 - self.mBall.getMomentum())):
                    return True
        return False

    def evolve(self):
        if self.mThemePlaying == False:
            self.mThemeSong.play()
            self.mThemePlaying = True
        for bar in self.mBars:
            if bar.getWidth() + bar.getShift() - self.mBall.getWidth() == 0:
                self.mPipeSound.play()
                self.mScore += 1
                self.mScoreText = Text(str(self.mScore),self.mWidth/10-20,self.mHeight/10-20)

        if self.groundCollide() or self.barCollide():
            self.mGameOver = True
            self.mHitSound.play()
            self.mThemeSong.stop()
            self.mBall.flip(180)
            
        if not self.mGameOver:
            self.mBall.evolve()
            for bar in self.mBars:
                bar.evolve()

        lastBar = self.mBars[len(self.mBars)-1]
        if lastBar.getShift() <= -150:
            newBar = Bar(self.mWidth, self.mHeight)
            self.mBars.append(newBar)
        return


