import pygame
import sys

WHITE = (255, 255, 255)#색깔
BLACK = (0, 0, 0)#색깔
SCREEN_W = 800#디스플레이 가로
SCREEN_H = 600#디스플레이 세로

pygame.init()#pygame 초기화
pygame.display.set_caption("pygame")#타이틀
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))#디스플레이 크기
font = pygame.font.SysFont("malgungothic", 30)#폰트,글자크기

    
def start():
    screen_mode = 0
    while True:
        for event in pygame.event.get():#이벤트 받기
            if event.type == pygame.QUIT:#pygame 종료
                pygame.quit()
                sys.exit
            
            if screen_mode == 0:#시작 화면  
                txt = font.render("스페이스바를 눌러 시작하시오",True, WHITE)
                text_rect = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2))
                screen.blit(txt, text_rect)
                pygame.display.update()
            
            elif screen_mode == 1:#스페이스바를 눌러 시작하기
                screen.fill(BLACK)
                txt = font.render("당신은 돌아가신 조부로 부터 커피집을 물려받았습니다",True, WHITE)
                text_rect = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2 ))
                screen.blit(txt, text_rect)                
                pygame.display.update()
            
            elif screen_mode == 2:#스페이스바를 눌러 시작하기
                screen.fill(BLACK)
                txt = font.render("가게를 유지하기위해 커피를 판매하십시오.",True, WHITE)
                text_rect = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2 ))
                screen.blit(txt, text_rect)                
                pygame.display.update()

            elif screen_mode == 3:#스페이스바를 눌러 시작하기
                screen.fill(BLACK)
                txt = font.render("커피를 만드는 법을 배우십시오.",True, WHITE)
                text_rect = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2 ))
                screen.blit(txt, text_rect)                
                pygame.display.update()

            if event.type == pygame.KEYDOWN:#키보드 이벤트 받기
                if event.key == pygame.K_SPACE:
                    screen_mode += 1    
        
if __name__ == '__main__':
    start()


        
        
        