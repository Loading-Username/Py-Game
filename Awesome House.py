import pygame
import math

# Initialize Game Engine
pygame.init()


# Window
SIZE = (800,600)
TITLE = "First Drawing"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (9, 234, 28)
BLUE = (106, 162, 252)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 123, 0)
YELLOW = (255, 250, 0)
PINK = (255, 0, 144)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])



# Game Loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game Logic (Check for collisions, update points, etc.)


    # Drawing Code (Describe the picture.)
    ''' sky '''
    screen.fill(BLUE)
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]
        pygame.draw.polygon(screen, WHITE, post)
    
    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])
    ''' house '''
    pygame.draw.rect(screen, RED, [400, 400, 400, 400])
    ''' roof '''
    pygame.draw.rect(screen, BLACK, [400, 300, 400, 100])

    ''' clouds '''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)

    
