from tkinter import Frame, Label, CENTER
import pygame
import gameModel
import constant as c
from pygame.locals import *

def main():
   row,col = 0, 0
   #initialize the difficulty level at 0
   diff_level = 0
   '''while True:
      size = input("Please input the size of the game (rows + one single space + columns): ")
      if len(size)==3 and '1'<size[0] and '1'<size[2]:
         row = int(size[0])
         col = int(size[2])
         break'''
   
   pygame.init()
   pygame.font.init()

   #add load the bgm when the game starts
   pygame.mixer.music.load('source/music/bg_music.wav')
   pygame.mixer.music.play(-1)
   screen = pygame.display.set_mode((400, 400))
   #thisCol = 100 * col + ((col + 1) * 10)
   #thisRow = 150 * col + ((row + 1) * 10)
   #pygame.display.set_mode((thisCol, thisRow))
   pygame.display.set_caption('2 0 4 8')
   w_surface = pygame.display.get_surface() 
   w_surface.fill(pygame.Color(234, 234, 250))

   myfont = pygame.font.Font(
       "./source/font/fofbb_reg.ttf", 20)
   title_font = pygame.font.Font(
       "./source/font/alphabetized cassette tapes.ttf", 50)
   special_font = pygame.font.Font(
       "./source/font/FAZINGSONE.ttf", 20)
   tTitle = title_font.render('Choose A Level', False, (0, 0, 0))
   tTitle_emoji = special_font.render('Cdsbdwu', False, (0, 26, 102))

   screen.blit(tTitle,(110,30))
   screen.blit(tTitle_emoji, (120, 20))

   button1 = pygame.Rect(100, 100, 200, 50)
   button2 = pygame.Rect(100, 170, 200, 50)
   button3 = pygame.Rect(100, 240, 200, 50)
   button4 = pygame.Rect(300, 335, 100, 50)

   sflag = True
   while sflag:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
               mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

               if button1.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))
                     col = 4
                     row = 4
                     sflag = False
                     diff_level = 16

               if button2.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))
                     col = 4
                     row = 4
                     sflag = False
                     diff_level = 4096

               if button3.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))
                     col = 4
                     row = 4
                     sflag = False
                     diff_level = 8192

               if button4.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))

         tNormal = myfont.render('Normal', False, (255, 255, 255))
         tHard = myfont.render('Hard', False, (255, 255, 255))
         tExtereme = myfont.render('Extereme', False, (255, 255, 255))
         tHelper = myfont.render('Helper', False, (0, 92, 179))
         pygame.draw.rect(screen, [179, 198, 255], button1)  # draw button
         pygame.draw.rect(screen, [128, 159, 255], button2)  # draw button
         pygame.draw.rect(screen, [77, 121, 255], button3)  # draw button
         pygame.draw.rect(screen, [153, 204, 255], button4)  # draw button
         screen.blit(tNormal,(165,110))
         screen.blit(tHard, (175, 180))
         screen.blit(tExtereme, (160, 250))
         screen.blit(tHelper, (320, 350))
         pygame.display.update()

   thisCol = 100 * col + ((col + 1) * 10)
   thisRow = 150 * col + ((row + 1) * 10)
   print("You choose difficulty level:", diff_level)
   pygame.display.set_mode((c.size, c.size))
   game = Game(w_surface,row,col,screen,diff_level)
   game.play() 

   #print the goodbye message before exit 
   myfont = pygame.font.SysFont("Verdana", 35, bold=True)
   screen.blit(myfont.render("Good Bye!", 1, (0, 0, 102)), (150, 225))
   pygame.display.update()
   pygame.time.wait(500)

   pygame.quit()


class Game:
   

   def __init__(self, surface, rows, cols, screen, difficulty):
      self.surface = surface
      self.bg_color = pygame.Color(c.colour["background"])
      self.FPS = 10000000000
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      self.model = gameModel.Model(rows,cols)
      self.screen = screen
      #not sure
      self.difficulty = difficulty
      
      
   def play(self):
      while not self.close_clicked: 
         self.handle_events()
         self.draw() 
         if self.continue_game:
            self.update()
            self.decide_continue()

         self.game_Clock.tick(self.FPS) 


   def handle_events(self):
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True


   def draw(self):
      self.surface.fill(self.bg_color)
      pos=[30,100]#pos to display
      myfont=pygame.font.SysFont("Verdana", 35, bold = True)
      bcol = 0
      brow = 0
      boxsize = c.size//4
      for r in self.model.getBoard():
         for s in r:
            if int(str(s)) != 0:
               tmp=myfont.render(str(s), True, [255, 255, 255])
               boxcolor = c.colour[str(s)]
               pygame.draw.rect(self.screen, boxcolor, (bcol * boxsize + c.padding,
                                              brow * boxsize + c.padding,
                                              boxsize - 2 * c.padding,
                                              boxsize - 2 * c.padding), 0)
               pos = (bcol * boxsize + c.dpadding[str(s)] * c.padding, brow * boxsize + 8 * c.padding)
               bcol += 1
               if bcol > 3:
                  bcol = 0
               self.surface.blit(tmp,pos)
            else:
               pygame.draw.rect(self.screen, c.colour[str(s)], (bcol * boxsize + c.padding,
                                 brow * boxsize + c.padding,
                                 boxsize - 2 * c.padding,
                                 boxsize - 2 * c.padding), 0)
               #pos = (bcol * boxsize + 4 * c.padding, brow * boxsize + 8 * c.padding)
               bcol += 1
               if bcol > 3:
                  bcol = 0
         #pos[1] += 72
         #pos[0] = 30
         brow += 1
         if brow > 3:
            brow = 0
      pygame.display.update()
      
      
   def update(self):
      if self.isover():
         self.continue_game=False
         return
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            self.close_clicked=True            
         elif event.type == pygame.KEYDOWN:
            available = self.model.getAvailableMove()
            if available ==[]:break
            if pygame.key.get_pressed()[pygame.K_a]:
                if 'a' in available:
                    self.model.move('a')
            elif pygame.key.get_pressed()[pygame.K_s]:
                if 's' in available:
                    self.model.move('s')            
            elif pygame.key.get_pressed()[pygame.K_d]:
                if 'd' in available:
                    self.model.move('d')   
            elif pygame.key.get_pressed()[pygame.K_w]:
                if 'w' in available:
                    self.model.move('w')           
            # add a exit game choice by press "q" 
            elif pygame.key.get_pressed()[pygame.K_q]:
                  pygame.quit()
            
   def decide_continue(self):
      if self.isover == True:
         myfont = pygame.font.SysFont("Verdana", 35, bold=True)
         screen.blit(myfont.render("Game Over!",
                                   1, (255, 255, 255)), (85, 225))
         pygame.display.update()
         pygame.time.wait(500)
         pygame.display.update()
         self.continue_game = False
         pygame.display.update()
         
         
   def isover(self):
      # fix here 

      print("current score: ", self.model.getScore())
      print("difficulty: ", self.difficulty)
      #if the ideal level is achieved, game over
      if self.model.getScore() == self.difficulty:
         return True

      #if no available move, game over
      elif self.model.getAvailableMove()==[]:
         return True
      return False
      
main()
