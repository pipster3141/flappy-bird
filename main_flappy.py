#
# Draw picture
#

import pygame
import math
import game_mouse
from collector import Collector

class PygameFlappyBird(game_mouse.Game):

    def __init__(self, width, height):

        game_mouse.Game.__init__(self, "Flappy Bird",width,height,50)
        
        self.font_height = 12
        self.font = pygame.font.SysFont("arial", self.font_height)
        self.mCollector = Collector(width, height)
        return
        
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_w  in newkeys or pygame.K_UP in newkeys:
            if not self.mCollector.getGameOver():
                self.mCollector.flap()

        if pygame.K_e in newkeys and not self.mCollector.getGameStart():
            self.mCollector.setEZGame()
        
        if 1 in newbuttons:
            print("button clicked")

        if pygame.K_a in newkeys:
            if self.mCollector.getGameOver():
                main()

        if not self.mCollector.getGameOver() and self.mCollector.getGameStart():
            self.mCollector.evolve()
        return
    
    def paint(self, surface):
        self.mCollector.draw(surface)
        return

def main():
    pygame.font.init()
    game = PygameFlappyBird(600, 500)
    game.main_loop()
    
if __name__ == "__main__":
    main()
