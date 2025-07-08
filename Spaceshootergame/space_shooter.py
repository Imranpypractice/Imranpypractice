import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Shooter")

# Load assets
PLAYER_IMG = pygame.image.load("player.png")
ENEMY_IMG = pygame.image.load("enemy.png")
BULLET_IMG = pygame.image.load("bullet.png")

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("comicsans", 30)

# Classes
class Player:
    def __init__(self):
        self.img = PLAYER_IMG
        self.x = WIDTH // 2 - 32
        self.y = HEIGHT - 70
        self.speed = 5
        self.bullets = []

    def draw(self):
        win.blit(self.img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw()

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 64:
            self.x += self.speed

    def shoot(self):
        self.bullets.append(Bullet(self.x + 25, self.y))

class Bullet:
    def __init__(self, x, y):
        self.img = BULLET_IMG
        self.x = x
        self.y = y
        self.speed = 7

    def draw(self):
        win.blit(self.img, (self.x, self.y))
        self.y -= self.speed

    def collide(self, enemy):
        return pygame.Rect(self.x, self.y, 16, 32).colliderect(pygame.Rect(enemy.x, enemy.y, 64, 64))

class Enemy:
    def __init__(self):
        self.img = ENEMY_IMG
        self.x = random.randint(0, WIDTH - 64)
        self.y = random.randint(-1000, -40)
        self.speed = random.randint(2, 5)

    def draw(self):
        win.blit(self.img, (self.x, self.y))
        self.y += self.speed

# Game loop
def main():
    run = True
    player = Player()
    enemies = [Enemy() for _ in range(5)]
    score = 0

    while run:
        clock.tick(FPS)
        win.fill((0, 0, 0))

        keys = pygame.key.get_pressed()
        player.move(keys)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Shooting bullets
        if keys[pygame.K_SPACE]:
            if len(player.bullets) < 5:
                player.shoot()

        # Update bullets
        for bullet in player.bullets[:]:
            bullet.draw()
            for enemy in enemies[:]:
                if bullet.collide(enemy):
                    try:
                        player.bullets.remove(bullet)
                        enemies.remove(enemy)
                        enemies.append(Enemy())
                        score += 10
                    except:
                        pass
            if bullet.y < 0:
                player.bullets.remove(bullet)

        # Draw and update enemies
        for enemy in enemies:
            enemy.draw()
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                enemies.append(Enemy())

        # Draw player and score
        player.draw()
        score_text = FONT.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (10, 10))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
