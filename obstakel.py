import pygame, random

pygame.init()

class Obstakel:
    # obstakel_list = []
    goal = 15
    
    def __init__(self, x, y, window, size, vel):
        self.x = x
        self.y = y
        self.window = window
        self.size = size
        self.color = (255, 0, 0)
        self.vel = vel
        self.count = 0
        self.rect = None
        # self.obstakel_list.append(self)


    @classmethod
    def update_class(cls):
        for obstakel in cls.obstakel_list:
            obstakel.update()


    def update(self):
        if self.x + round(self.size * 0.5) < 0:
            self.x = self.window.get_width() + random.randint(-50, 50)

        self.count += 1
        if self.count == 45 * 15:
            self.count = 0
            self.vel += 2
            self.goal += round(self.goal * 0,25)

        self.rect = pygame.Rect((self.x - round(self.size * 0.5), self.y - self.size, self.size, self.size))
        self.x -= self.vel
        self.draw()

    
    def draw(self):
        pygame.draw.polygon(self.window, self.color, self.triangle())


    def triangle(self):
        top = (self.x, self.y - self.size)
        left = (self.x - round(self.size * 0.5), self.y)
        right = (self.x + round(self.size * 0.5), self.y)
        return top, left, right