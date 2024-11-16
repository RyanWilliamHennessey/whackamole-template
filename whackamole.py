#Ryan Hennessey
#Note: took some concepts from the tic-tac-toe prograam form this one, liked it quite a bit despite how little is actually being done.
import pygame
import random

global screen
screen = pygame.display.set_mode((640, 512))

WIDTH = 640
HEIGHT = 512
LINE_WIDTH = 2
BOARD_ROWS = 16
BOARD_COLS = 20
SQUARE_SIZE = 32
RED = (255, 0, 0)
LINE_COLOR = (0, 0, 0)

def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE , HEIGHT),
            LINE_WIDTH
        )

def initialize_board():
    return [["-" for col in range(BOARD_COLS)] for row in range(BOARD_ROWS)]

def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()

def main():
    try:
        pygame.init()
        initialize_board()
#        print_board(initialize_board())

        mole_image = pygame.image.load("mole.png")
        x = 0
        y = 0
        screen.blit(mole_image, mole_image.get_rect(topleft=(x*SQUARE_SIZE, y*SQUARE_SIZE)))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    (a, b) = event.pos
                    a_square = a // 32
                    b_square = b // 32
                    position = (a_square, b_square)
                    if position == (x, y):
                        x = random.randrange(0, 20)
                        y = random.randrange(0, 16)

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(x * SQUARE_SIZE, y * SQUARE_SIZE)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
