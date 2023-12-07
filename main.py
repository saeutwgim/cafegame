import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    screen_w = 800
    screen_h = 600
    
    pygame.init()
    pygame.display.set_caption("pygame")
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("malgungothic", 50)
    
    game1 = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit



        txt = font.render("스페이스바를 눌러 시작하시오",True, WHITE)
        text_rect = txt.get_rect(center=(screen_w/2, screen_h/2))
        screen.blit(txt, text_rect)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
