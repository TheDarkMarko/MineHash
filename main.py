import pygame
import sys
import os

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MineHash")

FPS = 60
clock = pygame.time.Clock()

play = False

WHITE = (255, 255, 255)
GREY = (54, 61, 71)
BLACK = (0, 0, 0)
YELLOW = (230, 244, 9)

space = 90

sizew = 250
sizeh = 50

n = 5

x = (width - sizew) // 2
y = (height - sizeh) // 2 + sizeh*2

bg_image = pygame.image.load(os.path.join('assets', 'bg.png')).convert()
bg_image = pygame.transform.scale(bg_image, (width, height))

cave_image = pygame.image.load(os.path.join('assets', 'caveb.png')).convert()
cave_image = pygame.transform.scale(cave_image, (width//n+1, height//n+1))


font = pygame.font.Font('freesansbold.ttf', 20)

text1 = font.render('Play', True, GREY)
textRect1 = text1.get_rect()
textRect1.center = (x+sizew//2, y-space+sizeh//2)

text2 = font.render('Multiplayer', True, GREY)
textRect2 = text1.get_rect()
textRect2.center = (x+sizew//2.8, y+sizeh//2)

text3 = font.render('Setting', True, GREY)
textRect3 = text1.get_rect()
textRect3.center = (x+sizew//2-20, y+space+sizeh//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if play == False:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        screen.blit(bg_image, (0, 0))


        pygame.draw.rect(screen, WHITE, (x, y-space, sizew, sizeh))
        pygame.draw.rect(screen, GREY, (x, y-space, sizew, sizeh), 2)

        pygame.draw.rect(screen, WHITE, (x, y, sizew, sizeh))
        pygame.draw.rect(screen, GREY, (x, y, sizew, sizeh), 2)

        pygame.draw.rect(screen, WHITE, (x, y+space, sizew, sizeh))
        pygame.draw.rect(screen, GREY, (x, y+space, sizew, sizeh), 2)

        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)

        if (x < mouse_x < x + sizew and y - space < mouse_y < y-space//2):
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            pygame.draw.rect(screen, YELLOW, (x, y - space, sizew, sizeh), 3)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                play = True

        elif (x < mouse_x < x + sizew and y < mouse_y < y + sizeh):
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            pygame.draw.rect(screen, YELLOW, (x, y, sizew, sizeh), 3)

        elif (x < mouse_x < x + sizew and y+space < mouse_y < y+sizeh*2.8):
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            pygame.draw.rect(screen, YELLOW, (x, y+space, sizew, sizeh), 3)

        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
    else:
        pygame.draw.rect(screen, WHITE, (x, y-space, sizew, sizeh))

        for x in range(n):
            for y in range(n):
                screen.blit(cave_image, (x * width//n, y * height//n))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
