import pygame, sys
from assets.player import Player
from assets.obstakel import Obstakel

def terminate():
    pygame.quit()
    sys.exit()



CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 750, 500
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RAY IS AMAZING")


def main():
    player = Player(WIN, 10, HEIGHT - 35)
    obstakel = Obstakel(WIDTH, HEIGHT, WIN, 35, 5)

    while True:
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump = True

        if player.alive:
            obstakel.update()
            player.update()
            if player.rect.colliderect(obstakel.rect):
                player.alive = False
        else:
            restart()

        CLOCK.tick(FPS)

        pygame.display.update()


def restart():
    while True:
        WIN.fill((192, 0, 192))
        font = pygame.font.SysFont(None, 40)
        img = font.render('U NOOB, U DIED', True, (0, 0, 0))
        WIN.blit(img, (WIDTH / 2 - 100, HEIGHT / 2))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                main()

        CLOCK.tick(FPS)

        pygame.display.update()

main()