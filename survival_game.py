import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Выживание: избегай врагов")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Игрок
player_size = 40
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
player_speed = 5

# Враги
enemy_size = 40
enemy_list = []
enemy_speed = 5

# Счёт
score = 0
font = pygame.font.SysFont("Arial", 24)

# Таймер появления врагов
SPAWNENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, 1000)  # каждые 1000 мс = 1 секунда

# Часы для FPS
clock = pygame.time.Clock()

# Игровой цикл
running = True
while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWNENEMY:
            x_pos = random.randint(0, WIDTH - enemy_size)
            enemy_list.append([x_pos, 0])

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Движение врагов
    for enemy in enemy_list[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy_list.remove(enemy)
            score += 1

    # Проверка столкновений
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    for enemy in enemy_list:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            running = False

    # Отрисовка игрока и врагов
    pygame.draw.rect(screen, GREEN, player_rect)
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Показ счёта
    text = font.render(f"Счёт: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
