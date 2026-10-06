import pygame
import sys

# 1. Inicialização do PyGame
pygame.init()

# 2. Configurações da Janela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Primeiros Pasos no PyGame")

# 3. Configurações de Cores (RGB)
PRETO = (0, 0, 0)
AZUL = (0, 120, 255)

# 4. Posição e Tamanho do Objeto (Quadrado)
x, y = 375, 275
tam_quadrado = 50
velocidade = 5

# 5. Controle de Taxa de Quadros (FPS)
relogio = pygame.time.Clock()

# 6. Loop Principal do Jogo
rodando = True
while rodando:
    # --- Processamento de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # --- Leitura de Teclas ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # --- Desenho/Renderização ---
    tela.fill(PRETO)  # Limpa a tela pintando de preto
    
    # Desenha o quadrado azul na posição atual (x, y)
    pygame.draw.rect(tela, AZUL, (x, y, tam_quadrado, tam_quadrado))

    pygame.display.flip()  # Atualiza a tela com as novas informações

    # Limita o jogo a 60 FPS
    relogio.tick(60)

# 7. Finalização
pygame.quit()
sys.exit()