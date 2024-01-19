import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as constantes do jogo
WIDTH, HEIGHT = 600, 600  # Aumente o tamanho da janela
GRID_SIZE = 6  # Número de pontos em uma linha ou coluna

# Calcule o espaçamento entre os pontos para centralizá-los
GAP = WIDTH // GRID_SIZE

# Defina o tamanho e a cor dos pontos verdes
GREEN = (0, 255, 0)

# Defina as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Crie a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo dos Pontinhos")

# Função para desenhar a grade de pontos com pontos verdes entre eles
def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pygame.draw.circle(screen, BLACK, (x * GAP + GAP // 2, y * GAP + GAP // 2), 10)  # Pontos pretos centralizados

            # Desenhe pontos verdes nas linhas verticais e horizontais
            if x < GRID_SIZE - 1:
                pygame.draw.circle(screen, GREEN, (x * GAP + GAP, y * GAP + GAP // 2), 5)
            if y < GRID_SIZE - 1:
                pygame.draw.circle(screen, GREEN, (x * GAP + GAP // 2, y * GAP + GAP), 5)

# Função principal do jogo
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica do jogo aqui

        # Limpe a tela
        screen.fill(WHITE)

        # Desenhe a grade de pontos com pontos verdes
        draw_grid()

        # Atualize a tela
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()