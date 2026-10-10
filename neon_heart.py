import pygame
import math
import random
import sys

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Love Heart Animation")

BLACK = (0, 0, 0)
RED = (255, 75, 65)

font = pygame.font.SysFont("Arial", 13, bold=True)
clock = pygame.time.Clock()

phrases = [
    "I love you", "Ti amo", "Je t'aime",
    "Te amo", "Ich liebe dich",
    "Seni seviyorum", "Aku cinta kamu",
    "Kocham cie", "Anh yeu em",
    "Я тебя люблю", "사랑해"
]

# Check whether a point is inside the heart
def inside_heart(x, y):
    a = x*x + y*y - 1
    return a*a*a - x*x*y*y*y <= 0

# Generate text positions inside the heart
items = []

for y in [i / 100 for i in range(-100, 135, 5)]:
    for x in [i / 100 for i in range(-125, 126, 7)]:
        if inside_heart(x, y):
            text = random.choice(phrases)
            px = WIDTH // 2 + int(x * 230)
            py = HEIGHT // 2 - int(y * 210)

            items.append((px, py, text))

random.shuffle(items)

# Animate the heart
index = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Reveal more text every frame
    index = min(index + 3, len(items))

    for px, py, text in items[:index]:
        image = font.render(text, True, RED)
        screen.blit(image, (px, py))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()