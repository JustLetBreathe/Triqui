import pygame
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont

#pantalla
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

#tablero del triqui
BOARD_SIZE = 3
CELL_SIZE = SCREEN_WIDTH // BOARD_SIZE

#colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Triqui con Pygame y Pillow")

class Player:
    def _init_(self, symbol, is_computer=False):
        self.symbol = symbol
        self.is_computer = is_computer
        
class Board:
    def _init_(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.winning_line = None

    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.winning_line = None

    def draw(self, screen):
        screen.fill(WHITE)
        for x in range(1, 3):
            pygame.draw.line(screen, BLACK, (x * 100 + 150, 150), (x * 100 + 150, 450), 5)
            pygame.draw.line(screen, BLACK, (150, x * 100 + 150), (450, x * 100 + 150), 5)
        self.draw_symbols(screen)

    def draw_symbols(self, screen):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] != "":
                    color = RED if self.board[y][x] == 'X' else BLUE
                    text = font.render(self.board[y][x], True, color)
                    screen.blit(text, (x * 100 + 165, y * 100 + 165))
    def handle_click(self, x, y, symbol):
        if self.board[y][x] == "":
            self.board[y][x] = symbol
            return True
        return False               

class Game:
    def _init_(self):
        self.screen = pygame.display.set_mode((1100, 600))  
        pygame.display.set_caption("Tic Tac Toe")
        self.board = Board()
        self.player = Player('X')
        self.computer = Player('O', is_computer=True)


    def run(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            elif self.current_player == self.player:
                mouse_x, mouse_y = event.pos
                clicked_row = (mouse_y - 150) // 100
                clicked_col = (mouse_x - 150) // 100
                if 0 <= clicked_row < 3 and 0 <= clicked_col < 3:
                    if self.board.handle_click(clicked_col, clicked_row, self.player.symbol):
                            self.board.draw(self.screen)  
                            pygame.display.flip()
         pygame.quit()
        

        
if __name__ == "__main__":
    main()
    
