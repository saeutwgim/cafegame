import pygame
import sys
import random

pygame.init()#pygame 초기화
pygame.font.init()

pygame.display.set_caption("pygame")#타이틀

global screen
WHITE = (255, 255, 255)#색깔
BLACK = (0, 0, 0)#색깔
SCREEN_W = 800#디스플레이 가로
SCREEN_H = 600#디스플레이 세로
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))#디스플레이 크기
font = pygame.font.SysFont("malgungothic", 30)#폰트,글자크기

global cafe_out
cafe_out = pygame.image.load("cafe_out.png")
cafe_out = pygame.transform.scale(cafe_out, (800, 600))

global cafe_in
cafe_in = pygame.image.load("cafe_in.png")
cafe_in = pygame.transform.scale(cafe_in, (800, 600))
'''
global Espresso
Espresso = pygame.image.load("Espresso.png")
Espresso = pygame.transform.scale(Espresso, (50, 50))

global water
water = pygame.image.load("water.png")
water = pygame.transform.scale(water, (50, 50))

global milk
milk = pygame.image.load("milk.png")
milk = pygame.transform.scale(milk, (50, 50))

global ice
ice = pygame.image.load("ice.png")
ice = pygame.transform.scale(ice, (50, 50))

global lipton
lipton = pygame.image.load("lipton.png")
lipton = pygame.transform.scale(lipton, (50, 50))

global maxim
maxim = pygame.image.load("maxim.png")
maxim = pygame.transform.scale(maxim, (50, 50))
'''
global button
button1 = pygame.Rect(150, 380, 150, 60)
button2 = pygame.Rect(350, 380, 150, 60)
button3 = pygame.Rect(550, 380, 150, 60)
button4 = pygame.Rect(150, 470, 150, 60)
button5 = pygame.Rect(350, 470, 150, 60)
button6 = pygame.Rect(550, 470, 150, 60)
button_make = pygame.Rect(330, 250, 150, 60)
game_set =0

global text
text_order = 0
f = open('story.txt','r',encoding="UTF8")
story_txt = f.readlines()

global tutorial
tutorial_order = 0
g = open('tutorial.txt','r',encoding="UTF8")
tutorial_txt = g.readlines()
 
global limit
limit = 0

global menu_limit
menu_limit = 0

global menu_order
menu_order = 0

global repeat
repeat = 0

global number
number = 3

global coffee
coffee = 0
You_coffee = 0

global hp
hp = 3

global money
money = 0

global txet_bg_c
txet_bg_c = (255, 255, 255)

def game_t():    
    
    global coffee 
    global menu_order
    global button
    global screen

    
    screen.fill(BLACK)
    screen.blit(cafe_in, (0, 0))
    pygame.draw.rect(screen, WHITE, [150, 380, 150, 60])
    txt1 = font.render("물", True, BLACK)
    screen.blit(txt1,(210,390))
    pygame.draw.rect(screen, WHITE, [350, 380, 150, 60])
    txt2 = font.render("에스프레소", True, BLACK)
    screen.blit(txt2,(410,390))
    pygame.draw.rect(screen, WHITE, [550, 380, 150, 60])
    txt3 = font.render("우유", True, BLACK)
    screen.blit(txt3,(610,390))
    pygame.draw.rect(screen, WHITE, [150, 470, 150, 60])
    txt4 = font.render("얼음", True, BLACK)
    screen.blit(txt4,(210,480))
    pygame.draw.rect(screen, WHITE, [350, 470, 150, 60])
    txt5 = font.render("아이스티", True, BLACK)
    screen.blit(txt5,(410,480))
    pygame.draw.rect(screen, WHITE, [550, 470, 150, 60])
    txt6 = font.render("믹스커피", True, BLACK)
    screen.blit(txt6,(610,480)) 
    txt7 = font.render(str(repeat),True, WHITE)
    screen.blit(txt7,(SCREEN_W,150))


    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
            
        if button1.collidepoint(pos):
            coffee += 1
            

        elif button2.collidepoint(pos):
            coffee += 2
            

        elif button3.collidepoint(pos):
            coffee += 4
            

        elif button4.collidepoint(pos):
            coffee += 8
            

        elif button5.collidepoint(pos):
            coffee += 15
            

        elif button6.collidepoint(pos):
            coffee += 28
            

    if You_coffee == 1 and You_coffee < 2:
        if coffee == menu_order:
            screen.fill(BLACK)
            screen.blit(cafe_in, (0, 0))
            txt = font.render("성공(돈을 얻는다)", True, BLACK, txet_bg_c)
            text_rect  = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2))
            screen.blit(txt,text_rect)  
            
        else:   
            screen.fill(BLACK)
            screen.blit(cafe_in, (0, 0))
            txt = font.render("실패(hp를 소모한다 전부 소모하면 게임오버)", True, BLACK, txet_bg_c)
            text_rect  = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2))
            screen.blit(txt,text_rect)

def game_main():    
    
    global coffee 
    global menu_order
    global button
    global screen
    global hp
    global money
    global limit
    global number
    global Espresso
    global water
    global milk

    screen.fill(BLACK)
    screen.blit(cafe_in, (0, 0))
    pygame.draw.rect(screen, WHITE, [150, 380, 150, 60])
    txt1 = font.render("물", True, BLACK)
    screen.blit(txt1,(200,390))
    pygame.draw.rect(screen, WHITE, [350, 380, 150, 60])
    txt2 = font.render("에스프레소", True, BLACK)
    screen.blit(txt2,(350,390))
    pygame.draw.rect(screen, WHITE, [550, 380, 150, 60])
    txt3 = font.render("우유", True, BLACK)
    screen.blit(txt3,(610,390))
    pygame.draw.rect(screen, WHITE, [150, 470, 150, 60])
    txt4 = font.render("얼음", True, BLACK)
    screen.blit(txt4,(200,480))
    pygame.draw.rect(screen, WHITE, [350, 470, 150, 60])
    txt5 = font.render("아이스티", True, BLACK)
    screen.blit(txt5,(380,480))
    pygame.draw.rect(screen, WHITE, [550, 470, 150, 60])
    txt6 = font.render("믹스커피", True, BLACK)
    screen.blit(txt6,(570,480)) 
    txt7 = font.render("남은 재료  개", True, BLACK, txet_bg_c)
    screen.blit(txt7,(50,100))
    if number > 0 :
        txt = font.render(str(number),True, BLACK, txet_bg_c)
        screen.blit(txt,(185,100))

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
                
            if button1.collidepoint(pos):
                coffee += 1
                number -= 1
                #screen.blit(water,(SCREEN_W/2,SCREEN_W/2))

            elif button2.collidepoint(pos):
                coffee += 2
                number -=1
                #screen.blit(water,(SCREEN_W/2-5,SCREEN_W/2-5))

            elif button3.collidepoint(pos):
                coffee += 4
                number -= 1
                #screen.blit(milk,(SCREEN_W/2+5,SCREEN_W/2-5))

            elif button4.collidepoint(pos):
                coffee += 8
                number -= 1
                #screen.blit(milk,(SCREEN_W/2+5,SCREEN_W/2+5))

            elif button5.collidepoint(pos):
                coffee += 15
                number -=1
                #screen.blit(lipton,(SCREEN_W/2+10,SCREEN_W/2+5))

            elif button6.collidepoint(pos):
                coffee += 28
                number -= 1
                #screen.blit(maxim,(SCREEN_W/2-5,SCREEN_W/2+10))

    if number <= 0 :
        txt = font.render("0",True, BLACK, txet_bg_c)
        screen.blit(txt,(185,100))
        number = 0

    if You_coffee == 1 and You_coffee < 2:
        
        if coffee == menu_order and limit == 0:
            money += 100
        
        if coffee == menu_order:
            screen.fill(BLACK)
            screen.blit(cafe_in, (0, 0))
            txt = font.render("+100$ 현재 돈:", True, BLACK,txet_bg_c)
            text_rect  = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2))
            txt1 = font.render(str(money), True, BLACK,txet_bg_c)
            text_rect1  = txt1.get_rect(center=(SCREEN_W/2, 400))
            screen.blit(txt,text_rect)
            screen.blit(txt1,text_rect1)  
            limit +=1
            number = 3
        
        if not coffee == menu_order and limit == 0:
            hp -= 1

        if not coffee == menu_order:   
            screen.fill(BLACK)
            screen.blit(cafe_in, (0, 0))
            txt = font.render("실패 hp가 감소합니다 (현재 hp:", True, BLACK, txet_bg_c)
            txt1 = font.render(str(hp), True, BLACK, txet_bg_c)
            text_rect  = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2))
            text_rect1  = txt1.get_rect(center=(SCREEN_W/2, 400))
            screen.blit(txt,text_rect)
            screen.blit(txt1,text_rect1)
            limit +=1
            number = 3
            
def order():
    
    global screen
    global menu_order 
    global menu_limit
    
    c = open('menu1.txt','r',encoding="UTF8")
    menu1_txt = c.readlines()
    text_limit = 0
    menu_limit  == 0
    a = 0
    repeat = random.randrange(1,4)

    while a < repeat: 
        b = random.randrange(0,5)
        menu_category = random.sample(range(0,6),3) 
        menu = [1,2,4,8,15,28]    
        menu_a = menu[menu_category[a]]
        menu_order += menu_a
        a += 1
        
        if a >= repeat:
            if  menu_order == 1: #물
                text_limit = 0
                text_limit += b

            elif  menu_order == 2: #에스프레소
                text_limit = 5
                text_limit += b

            elif  menu_order == 4: #우유
                text_limit = 10
                text_limit += b
            
            elif  menu_order == 3: #아메리카노
                text_limit = 15
                text_limit += b

            elif  menu_order == 9: #얼음물
                text_limit = 20
                text_limit += b
                
            elif  menu_order == 16: # 미지근 아이스티 
                text_limit = 25
                text_limit += b
                
            elif  menu_order == 29: #믹스 커피
                text_limit = 30
                text_limit += b
                
            elif  menu_order == 6: #라떼
                text_limit = 35
                text_limit += b

            elif  menu_order == 10: #아이스 에스프레소
                text_limit = 40
                text_limit += b

            elif  menu_order == 32: # 커피우유
                text_limit = 45
                text_limit += b
    
            elif  menu_order == 11: # 아이스 아메리카노
                text_limit = 50
                text_limit += b

            elif  menu_order == 18: # 아샷추
                text_limit = 55
                text_limit += b

            elif  menu_order == 24: # 아이스티
                text_limit = 60
                text_limit += b

            elif  menu_order == 37: # 아이스 믹스커피
                text_limit = 65
                text_limit += b

            elif  menu_order == 14: # 아이스 라떼
                text_limit = 70
                text_limit += b

            elif  menu_order == 40: # 아이스 커피우유
                text_limit = 75 
                text_limit += b

            
            else:
                a = 0
                menu_order = 0

            screen.fill(BLACK)
            screen.blit(cafe_in, (0, 0))
            txt = font.render(menu1_txt[text_limit], True, BLACK ,txet_bg_c)
            text_rect  = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2))
            screen.blit(txt,text_rect)
        

        
    

def count():
    
    global screen
    global money
    global hp
    
    txt = font.render("money:", True, BLACK,txet_bg_c)
    screen.blit(txt,(600,60)) 
    txt1 = font.render("hp:", True, BLACK,txet_bg_c)
    screen.blit(txt1,(660,100))
    txt2 = font.render(str(money), True, BLACK,txet_bg_c)
    screen.blit(txt2,(700,60))
    txt3 = font.render(str(hp), True, BLACK,txet_bg_c)
    screen.blit(txt3,(700,100)) 
 


is_running = True
while is_running:
    for event in pygame.event.get():#이벤트 받기   
        if event.type == pygame.QUIT:#pygame 종료              
            is_running = False
        elif event.type == pygame.KEYDOWN:#키보드 이벤트 받기
            if event.key == pygame.K_SPACE:
                text_order += 1
            if event.key == pygame.K_t: 
                tutorial_order += 1
                text_order = 5
            if event.key == pygame.K_RETURN:
                You_coffee += 1
                text_order = 10

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if button_make.collidepoint(pos):
                game_set = 1
                text_order = 7

        if text_order < 5 and tutorial_order == 0:
            screen.fill(BLACK)            
            txt = font.render(story_txt[text_order], True, BLACK, txet_bg_c)
            text_rect = txt.get_rect(center=(SCREEN_W/2, 530))
            screen.blit(cafe_out,(0, 0))
            screen.blit(txt, text_rect)
            

        if tutorial_order == 1:
            if text_order > 4 and game_set == 0 and tutorial_order == 1:
                screen.fill(BLACK)
                screen.blit(cafe_in, (0, 0))
                txt = font.render(tutorial_txt[text_order-5], True, BLACK,txet_bg_c)
                text_rect = txt.get_rect(center=(SCREEN_W/2, 530))
                screen.blit(txt, text_rect)
                pygame.draw.rect(screen, BLACK, [330, 250, 150, 60])
                txt2 = font.render("주문", True, BLACK)
                screen.blit(txt2,(370,265))

            
            if game_set == 1 and text_order == 7 and tutorial_order == 1:
                while menu_limit == 0:
                    order() 
                    menu_limit  += 1

            if  text_order == 8 and game_set >= 1:
                screen.fill(BLACK)
                screen.blit(cafe_in, (0, 0))
                txt = font.render(tutorial_txt[text_order-4], True, BLACK,txet_bg_c)
                text_rect  = txt.get_rect(center=(SCREEN_W/2, 400))
                screen.blit(txt,text_rect)
                
            if  text_order >= 9 and game_set >= 1:
                game_t()

            if text_order == 11 and tutorial_order == 1:
                text_order = 4
                tutorial_order = 0
                coffee = 0
                menu_order = 0 
                You_coffee = 0
                limit = 0
                game_set = 0
                menu_limit = 0
                money = 0
                hp = 3
        
        if hp == 0:
            screen.fill(BLACK)            
            txt = font.render("game over", True, WHITE)
            txt1 = font.render(str(money), True, WHITE)
            text_rect = txt.get_rect(center=(SCREEN_W/2, SCREEN_H/2))
            text_rect1 = txt.get_rect(center=(SCREEN_W/2, 400))
            screen.blit(txt, text_rect)
            screen.blit(txt1, text_rect1)
            text_order = -1

        if text_order == 5 and tutorial_order == 0:
            screen.fill(BLACK)            
            screen.blit(cafe_in, (0, 0))
            txt = font.render("주문을 받으시오", True, BLACK,txet_bg_c)
            text_rect = txt.get_rect(center=(SCREEN_W/2, 400))
            screen.blit(txt, text_rect) 
            count()

        elif text_order == 6:
            screen.fill(BLACK)
            screen.blit(cafe_in, (0, 0))
            pygame.draw.rect(screen, BLACK, [330, 250, 150, 60])
            txt2 = font.render("주문", True, BLACK,txet_bg_c)
            screen.blit(txt2,(370,265))
            count()

        elif game_set == 1 and text_order == 7:  
            while menu_limit == 0:
                order()
                menu_limit  += 1

        elif text_order >= 8 and text_order <= 10 and tutorial_order == 0:
            game_main()
        
        elif text_order == 11 and tutorial_order == 0:
            game_set = 0
            b = 0
            coffee = 0
            menu_order = 0 
            text_order = 5
            You_coffee = 0
            limit = 0
            game_set = 0
            menu_limit = 0

        
    pygame.display.update()
                
pygame.quit()