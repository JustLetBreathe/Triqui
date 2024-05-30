import pygame
from pygame.locals import *
from PIL import Image, ImageDraw

#pantalla
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

#tablero del triqui
BOARD_SIZE = 3
CELL_SIZE = SCREEN_WIDTH // BOARD_SIZE

#colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Triqui con Pygame y Pillow")

def draw_board():
    #creación de imágenes
    image = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)

    #lineas verticales
    for i in range(1, BOARD_SIZE):
        x = CELL_SIZE * i
        y = CELL_SIZE * i
        draw.line([(x, 0), (x, SCREEN_HEIGHT)], fill=BLACK)
        draw.line([(0, y), (SCREEN_WIDTH, y)], fill=BLACK)

    #superficie de pygame
    pygame_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)

    #dibujar
    screen.blit(pygame_image, (0, 0))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        draw_board()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
    