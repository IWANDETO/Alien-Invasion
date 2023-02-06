import sys

import pygame

class Alieninvasion:
    """"Overall class to manage game assests and behaviour"""

    def __init__(self):
        """Initialize the game, and create the game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Setting the Background Color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the main loop of the game"""
        while True:
            #Watch out for the keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    sys.exit()

                    # Redraw the screen during each pass through the loop
                    self.screen.fill(self.bg_color)

                    # Make the most recently drawn screen visible
                    pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Alieninvasion()
    ai.run_game()
    
