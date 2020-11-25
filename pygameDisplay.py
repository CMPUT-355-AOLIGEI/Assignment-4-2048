from tkinter import Frame, Label, CENTER
import pygame
import gameModel
import view


def main():
   row,col = 0, 0
   '''while True:
      size = input("Please input the size of the game (rows + one single space + columns): ")
      if len(size)==3 and '1'<size[0] and '1'<size[2]:
         row = int(size[0])
         col = int(size[2])
         break'''
   
   pygame.init()
   pygame.font.init()
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

   # img1 = pygame.image.load(
   #     "/Users/yueling/Desktop/Assignment-4-2048/source_image/extreme.bmp")
   # screen.blit(img1, (0, 0))
   # header1_rect = img1.get_rect()
   # header1_rect.centerx = screen_rect.centerx
   # header1_rect.centery = screen_rect.centery
   # screen.blit(img1, screen_rect)
   # pygame.display.update()

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

               if button2.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))
                     col = 4
                     row = 4
                     sflag = False

               if button3.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))
                     col = 4
                     row = 4
                     sflag = False

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
   thisRow = 110 * col + ((row + 1) * 10)
   pygame.display.set_mode((thisRow, thisCol))
   game = Game(w_surface,row,col)
   game.play() 
   pygame.quit()


class Game:
   

   def __init__(self, surface, rows, cols):
      self.surface = surface
      self.bg_color = pygame.Color(128, 159, 255)
      self.FPS = 10000000000
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      self.model = gameModel.Model(rows,cols)
      
      
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
      myfont=pygame.font.SysFont('a',72)  
      for r in self.model.getBoard():
         for c in r:
            tmp=myfont.render(str(c), True, [255, 255, 255])            
            self.surface.blit(tmp,pos)
            pos[0]+=72
         pos[1] += 72
         pos[0] = 30
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
            
   def decide_continue(self):
      if self.isover==True:
         self.continue_game = False
         
         
   def isover(self):
      if self.model.getAvailableMove()==[]:
         return True
      return False
      
main()
