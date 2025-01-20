import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SPRITE_SIZE = 50
SPEED = 5

# Create the window
win = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT - SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)
        self.speed_x = SPEED
        self.lives = 3
        self.points = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed_x
        if keys[pygame.K_RIGHT] and self.x < WIDTH - SPRITE_SIZE:
            self.x += self.speed_x

def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

def main():
    clock = pygame.time.Clock()
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            # reset game state (for demonstration purposes)
            player.x = WIDTH / 2
            player.y = HEIGHT - SPRITE_SIZE
            player.lives = 3

        win.fill((0, 0, 0))
        draw_text('Lives: ' + str(player.lives), 24, (255, 255, 255), 10, 10)
        draw_text('Points: ' + str(player.points), 24, (255, 255, 255), WIDTH - 150, 10)

        player.move()
        pygame.draw.rect(win, (255, 0, 0), player)

        # boundary checking
        if player.x < 0:
            player.speed_x *= -1
            player.points += 10
        elif player.x > WIDTH - SPRITE_SIZE:
            player.speed_x *= -1
            player.points += 10

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()

