import pygame

"""
This class serves to draw the hand selection button for the player
"""

REF_POSITION = (307, 392)
SPACE_BTW_BUTTON = 80

class Rock:
    def __init__(self, screen):
        self.screen = screen
        self.position = (REF_POSITION[0]-2*SPACE_BTW_BUTTON, REF_POSITION[1])
        
        # load image
        self.image = pygame.image.load(
            r"./images/b1.png")
        self.rect = self.image.get_rect(topleft=self.position)

    def draw_rock(self):
        # draw hands in screen
        self.screen.blit(self.image, self.position)


class Paper:
    def __init__(self, screen):
        self.screen = screen
        self.position = (REF_POSITION[0]-SPACE_BTW_BUTTON, REF_POSITION[1])
        
        # load image
        self.image = pygame.image.load(
            r"./images/b2.png")
        self.rect = self.image.get_rect(topleft=self.position)

    def draw_paper(self):
        # draw hands in screen
        self.screen.blit(self.image, self.position)


class Scissors:
    def __init__(self, screen):
        self.screen = screen
        self.position = (REF_POSITION[0], REF_POSITION[1])
    
        # load image
        self.image = pygame.image.load(
            r"./images/b3.png")
        self.rect = self.image.get_rect(topleft=self.position)

    def draw_scissors(self):
        # draw hands in screen
        self.screen.blit(self.image, self.position)

class Well :
    def __init__(self, screen):
        self.screen = screen
        self.position = (REF_POSITION[0]+SPACE_BTW_BUTTON, REF_POSITION[1])
        
        # load image
        self.image = pygame.image.load(
            r"./images/b10.png")
        self.rect = self.image.get_rect(topleft=self.position)

    def draw_well(self):
        # draw hands in screen
        self.screen.blit(self.image, self.position)
