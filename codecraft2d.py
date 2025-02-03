import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CodeCraft 2D")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRASS_GREEN = (34, 139, 34)
DIRT_BROWN = (139, 69, 19)

# Tamaño de los bloques
BLOCK_SIZE = 40

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Clase para el jugador
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.velocity = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def move(self, dx, dy):
        self.x += dx * self.velocity
        self.y += dy * self.velocity

# Clase para los bloques
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE), 1)

# Función para dibujar la cuadrícula
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Función para dibujar el suelo
def draw_ground():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(HEIGHT // 2, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, DIRT_BROWN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Función principal del juego
def main():
    running = True
    player = Player(WIDTH // 2, HEIGHT // 2)
    blocks = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Colocar un bloque (clic izquierdo)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                x = x // BLOCK_SIZE * BLOCK_SIZE
                y = y // BLOCK_SIZE * BLOCK_SIZE
                blocks.append(Block(x, y, GRASS_GREEN))

            # Destruir un bloque (clic derecho)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                x, y = event.pos
                x = x // BLOCK_SIZE * BLOCK_SIZE
                y = y // BLOCK_SIZE * BLOCK_SIZE
                blocks = [block for block in blocks if block.x != x or block.y != y]

        # Capturar las teclas presionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            player.move(1, 0)
        if keys[pygame.K_UP]:
            player.move(0, -1)
        if keys[pygame.K_DOWN]:
            player.move(0, 1)

        # Limpiar la pantalla
        screen.fill(WHITE)

        # Dibujar el suelo
        draw_ground()

        # Dibujar la cuadrícula
        draw_grid()

        # Dibujar los bloques
        for block in blocks:
            block.draw(screen)

        # Dibujar al jugador
        player.draw(screen)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de actualización
        clock.tick(30)

    pygame.quit()
    sys.exit()

# Ejecutar el juego
if __name__ == "__main__":
    main()