import pygame

pygame.init()

class Player:

    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.size = 35
        self.alive = True
        self.color = (192, 0, 192)  # PAARS, speciaal voor jou ;)
        self.jump = False
        self.neg = 1
        self.jumpCount = 17
        self.rect = None


    def update(self):
        if self.alive:
            if self.jump == True:
                self.spring()
            else:
                self.draw()


    def spring(self):
        if self.jumpCount >= -17:
            self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.09
            self.jumpCount -= 1
            self.draw()
        else:
            self.jumpCount = 17
            self.neg = 1
            self.jump = False
            self.draw()


    def draw(self):
        self.rect = pygame.Rect((self.x, self.y, self.size, self.size))
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.size, self.size))