import pygame
import time
from helpers import load_image
import PyMan 

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (150,0,0)
light_red = (255,0,0)
yellow = (255,255,0)
green = (10,157,10)
light_green = (0,255,0)
blue = (10,10,150) 
light_blue = (10,10,255)
orange = (255,100,0)
display_width = 800
display_height = 600
smallfont = pygame.font.SysFont("Comic Sans MS",25)
mediumfont = pygame.font.SysFont("Comic Sans MS",50)
largefont = pygame.font.SysFont("Comic Sans MS",80)
clock = pygame.time.Clock()
pygame.mixer.music.load("game.wav")
pygame.mixer.music.play(-1)





gameDisplay = pygame.display.set_mode((display_width,display_height))

gameDisplay.fill(white)
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True , color)
    elif size == "medium":
        textSurface = mediumfont.render(text,True , color)
    elif size == "large":
        textSurface = largefont.render(text,True , color)
    return textSurface, textSurface.get_rect()
def text_toButton(msg,color,buttonx,buttony,buttonwidth,buttonheight,size ="small"):
        textSurf,textRect = text_objects(msg,color,size)
        textRect.center =((buttonx+(buttonwidth/2)),buttony +(buttonheight/2))
        gameDisplay.blit(textSurf, textRect)
def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width / 2),(display_height / 2)+ y_displace

    gameDisplay.blit(textSurf, textRect)

def button(text,x,y,width,height,inactive_color, active_color,action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+width > cur[0] > x and y + height > cur[1] > y):
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
          
            if action == "play":
            	obj = PyMan.PyManMain(1000,1100)
                obj.MainLoop()
                #pass

          		
            #print "button clicked"
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))
    text_toButton(text,black,x,y,width,height)
bg = pygame.image.load("pacmanbg.png")

    
def game_intro():
    intro= True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    quit()
                    
        gameDisplay.fill(black)
        gameDisplay.blit(bg,(0,0))
        
        message_to_screen("Pac-Man", light_red, -250, "large")
        message_to_screen("The Objective of the game is to Eat all the fruits",yellow,-150)
        message_to_screen("Try to keep away from the ghosts",orange,-120)
        message_to_screen("To finish the game eat all the fruits",light_blue,155)
        #message_to_screen("Press C to play or Q to quit", yellow, 80)
        
      
        
        
        button("Play",150,500,100,50,green,light_green,"play")
        
        button("Quit",550,500,100,50,red,light_red,"quit")       

        pygame.display.update()
        clock.tick(15)
        
        

        

game_intro()
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()

    
 
