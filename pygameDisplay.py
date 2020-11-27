from tkinter import Frame, Label, CENTER
from numpy.core.numeric import isclose
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
   button5 = pygame.Rect(300, 30, 100, 50)
   block_helper = pygame.Rect(90, 100, 230, 230)

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
   checking = False
   
   sflag = True
   while sflag:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
               mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
               if not checking:
                  if button1.collidepoint(mouse_pos):
                     # prints current location of mouse
                        print('button was pressed at {0}'.format(mouse_pos))
                        col = 4
                        row = 4
                        sflag = False
                        diff_level = 2048

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
                     checking = True
                     print('button was pressed at {0}'.format(mouse_pos))
                     w_surface.fill(c.colour["over"])

                     pygame.draw.rect(
                         screen, [204, 153, 102], block_helper)  # draw button
                     font1 = pygame.font.Font(
                         "./source/font/fofbb_reg.ttf", 20)
                     font2 = pygame.font.Font(
                         "./source/font/fofbb_reg.ttf", 30)
                     screen.blit(font2.render(
                         "Game Rules!", 1, (96, 64, 32)), (110, 50))
                     rule1 = font1.render("Use 'w,a,s,d' to move", False, (242, 242, 242))
                     screen.blit(rule1, (101, 100))
                     rule2 = font1.render(
                         "the tiles. Tiles with", False, (242, 242, 242))
                     screen.blit(rule2, (101, 140))
                     rule3 = font1.render(
                         "the same number will", False, (242, 242, 242))
                     screen.blit(rule3, (101, 180))
                     rule4 = font1.render("merge into one when", False, (242, 242, 242))
                     screen.blit(rule4, (101, 220)) 
                     rule5 = font1.render(
                         "they collide. Add them", False, (242, 242, 242))
                     screen.blit(rule5, (101, 260))                      
                     rule6 = font1.render(
                         "up to reach the goal!", False, (242, 242, 242))
                     screen.blit(rule6, (101, 300))
                     
                     pygame.draw.rect(screen, [153, 204, 255], button5)  # draw button
                     resume = myfont.render('Resume', False, (0, 92, 179))
                     screen.blit(resume, (320, 45))
                     
               if button5.collidepoint(mouse_pos):
                  checking = False
                  return True
         pygame.display.update()
         
   thisCol = 100 * col + ((col + 1) * 10)
   thisRow = 150 * col + ((row + 1) * 10)
   print("You choose difficulty level:", diff_level)
   pygame.display.set_mode((c.size, c.size))
   game = Game(w_surface,row,col,screen,diff_level)
   return game.play()


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
      self.difficulty = difficulty
      self.isreturn = False
      
   def play(self):
      isLose = False
      while not self.close_clicked and not isLose:
         self.handle_events()
         isWin = self.draw()
         # display the winning message when player wins, game ends.
         if isWin:
            score = self.model.getScore()
            self.surface.fill(c.colour["over"])
            myfont = pygame.font.SysFont("Verdana", 35, bold=True)
            self.screen.blit(myfont.render("You Win!", 1, (0, 0, 102)), (150, 150))
            self.screen.blit(myfont.render(
               "Score: " + str(score), 1, (0, 153, 204)), (150, 200))
               
            exit_button = pygame.Rect(150, 300, 120, 60)
            pygame.draw.rect(self.screen, [153, 204, 255], exit_button)
            self.screen.blit(myfont.render(
               "EXIT", 1, (0, 0, 102)), (155, 300))
            pygame.display.update()
            
            for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_pos = event.pos
                  if exit_button.collidepoint(mouse_pos):
                     return True

         if self.continue_game:
            self.update()
            self.decide_continue()
            continue

         # display the losing message when player loses, game ends
         elif not self.continue_game:
            isLose = True
         #fix here
         self.game_Clock.tick(self.FPS)

      #print the goodbye message before exit 
      # self.surface.fill(c.colour["over"])
      # myfont = pygame.font.SysFont("Verdana", 35, bold=True)
      # self.screen.blit(myfont.render("Good Bye!", 1, (0, 0, 102)), (150, 225))
      # pygame.display.update()
      # pygame.time.wait(500)
      if isLose == True:
         #isClick = True
         while True:
            score2 = self.model.getScore()
            self.surface.fill(c.colour["over"])
            myfont = pygame.font.SysFont("Verdana", 35, bold=True)
            self.screen.blit(myfont.render("You Lose!", 1, (0, 0, 102)), (150, 150))
            self.screen.blit(myfont.render(
               "Score: " + str(score2), 1, (0, 153, 204)), (150, 200))

            exit_button2 = pygame.Rect(150, 300, 120, 60)
            pygame.draw.rect(self.screen, [153, 204, 255], exit_button2)
            self.screen.blit(myfont.render(
               "EXIT", 1, (0, 0, 102)), (155, 300))
            pygame.display.update()

            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  return True
               if event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_pos = event.pos
                  if exit_button2.collidepoint(mouse_pos):
                     return True
      return False


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
      if self.difficulty in self.model.getBoard():
         self.surface.fill(c.colour["over"])
         return True
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
         self.continue_game = False
         return False
      return True

   def isover(self):
      #if no available move, game over
      if self.model.getAvailableMove()==[]:
         return True
      return False


loop = True
while loop:      
      loop = main()
