#! /usr/bin/env python

import os, sys
import pygame
import level001
import basicSprite
import pygame.mixer
import time
from pygame.locals import *
from helpers import *
from pacSprite import *
from basicMonster import Monster
import level001

pygame.init()
#pac_sound=pygame.mixer.Sound('game.wav')
#pygame.mixer.music.load("game.wav")

BLOCK_SIZE = 30
red=(255,0,0)
gameDisplay=pygame.display.set_mode((800,600))
font=pygame.font.SysFont(None,100)

class PyManMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
    def message_to_screen(self,msg,colour):
	screen_text=font.render(msg,True,colour)
	gameDisplay.blit(screen_text,[200,200])
                                                     
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        
        """Load All of our Sprites"""
        self.LoadSprites();
        
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        """Draw the blocks onto the background, since they only need to be 
        drawn once"""
        self.block_sprites.draw(self.screen)
        self.block_sprites.draw(self.background)
        #self.pellet_sprites.draw(self.screen)
        #self.pellet_sprites.draw(self.background)
        
        pygame.display.flip()
        while 1:
            #pygame.mixer.music.play(-1)
            #pac_sound.play()
            self.pacman_sprites.clear(self.screen,self.background)
            self.monster_sprites.clear(self.screen,self.background)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.pacman.MoveKeyDown(event.key)
                elif event.type == KEYUP:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.pacman.MoveKeyUp(event.key)
                elif event.type == SUPER_STATE_OVER:
                    self.pacman.superState = False
                    """Stop the timer"""
                    pygame.time.set_timer(SUPER_STATE_OVER,0)
                    for monster in self.monster_sprites.sprites():
                        monster.SetScared(False)
                elif event.type == SUPER_STATE_START:
                    for monster in self.monster_sprites.sprites():
                        monster.SetScared(True)
                elif event.type == PACMAN_EATEN:
             	    
		    
		    self.message_to_screen("GAME OVER",red)
		    pygame.display.update()
		    time.sleep(2)       
                    sys.exit()
                
            """Update the pacman sprite"""        
            self.pacman_sprites.update(self.block_sprites
                                       , self.pellet_sprites
                                       , self.super_pellet_sprites
                                       , self.monster_sprites)
            self.monster_sprites.update(self.block_sprites)
                        
            
                
            textpos = 0          
            self.screen.blit(self.background, (0, 0))     
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("Pellets %s" % self.pacman.pellets
                                    , 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.background.get_width()/2)
                self.screen.blit(text, textpos)
            
            reclist = [textpos]  
            reclist += self.pellet_sprites.draw(self.screen)
            reclist += self.super_pellet_sprites.draw(self.screen)
            reclist += self.pacman_sprites.draw(self.screen)
            reclist +=  self.monster_sprites.draw(self.screen)
            #reclist += (self.block_sprites.draw(self.screen))
            
            pygame.display.update(reclist)
           # pygame.display.flip()
                    
    def LoadSprites(self):
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        x_offset = (BLOCK_SIZE/2)
        y_offset = (BLOCK_SIZE/2)
        """Load the level"""        
        level1 = level001.level()
        layout = level1.getLayout()
        img_list = level1.getSprites()
        
        """Create the Pellet group"""
        self.pellet_sprites = pygame.sprite.RenderUpdates()
        self.super_pellet_sprites = pygame.sprite.RenderUpdates()
        """Create the block group"""
        self.block_sprites = pygame.sprite.RenderUpdates()
        self.monster_sprites = pygame.sprite.RenderUpdates()
        
        for y in xrange(len(layout)):
            for x in xrange(len(layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                if layout[y][x]==level1.BLOCK:
                    block = basicSprite.Sprite(centerPoint, img_list[level1.BLOCK])
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.PACMAN:
                    self.pacman = Pacman(centerPoint,img_list[level1.PACMAN])
                elif layout[y][x]==level1.PELLET:
                    pellet = basicSprite.Sprite(centerPoint, img_list[level1.PELLET])
                    self.pellet_sprites.add(pellet) 
                elif layout[y][x]==level1.MONSTER:
                    monster = Monster(centerPoint, img_list[level1.MONSTER]
                                       , img_list[level1.SCARED_MONSTER])
                    self.monster_sprites.add(monster) 
                    """We also need pellets where the monsters are"""
                    pellet = basicSprite.Sprite(centerPoint, img_list[level1.PELLET])
                    self.pellet_sprites.add(pellet) 
                elif layout[y][x]==level1.SUPER_PELLET:
                    super_pellet = basicSprite.Sprite(centerPoint, img_list[level1.SUPER_PELLET])
                    self.super_pellet_sprites.add(super_pellet) 
                     
        """Create the Pacman group"""            
        self.pacman_sprites = pygame.sprite.RenderUpdates(self.pacman)                                  

if __name__ == "__main__":
    MainWindow = PyManMain(1000,1100)
    MainWindow.MainLoop()
       
