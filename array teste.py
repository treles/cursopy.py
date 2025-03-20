import Pygame

# Inicializar o Pygame
pygame.init()

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.5
JUMP_STRENGTH = -15

# Configurar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cubo Móvel")

# Definir a classe do jogador
class Player:
    def __init__(self):
        self.position = pygame.Vector2(400, 500)  # Posição inicial
        self.velocity = pygame.Vector2(0, 0)  # Velocidade inicial
        self.width = 50
        self.height = 50
        self.on_ground = True

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        else:
            self.velocity.x = 0

        if self.on_ground and keys[pygame.K_SPACE]:
            self.velocity.y = JUMP_STRENGTH
            self.on_ground = False

        # Aplicar gravidade
        self.velocity.y += GRAVITY

        # Atualizar a posição
        self.position += self.velocity

        # Verificar se o cubo está no chão
        if self.position.y >= SCREEN_HEIGHT - self.height:
            self.position.y = SCREEN_HEIGHT - self.height
            self.on_ground = True
            self.velocity.y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.position.x, self.position.y, self.width, self.height))

# Criar instância do jogador
player = Player()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar o jogador
    player.move()

    # Limpar a tela
    screen.fill((0, 0, 0))

    # Desenhar o jogador
    player.draw(screen)

    # Atualizar a tela
    pygame.display.flip()
    pygame.time.delay(30)  # Controlar a taxa de atualização

pygame.quit()