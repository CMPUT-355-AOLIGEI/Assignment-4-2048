from tkinter import Frame, Label, CENTER
import pygame
import gameModel
import view


def main():
   row,col = 0, 0
   '''while True:
      size = input("Please input the size of the game(rows+one single space+columns): ")
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
   pygame.display.set_caption('2048')   
   w_surface = pygame.display.get_surface() 
   w_surface.fill(pygame.Color(146, 135, 125))
   myfont = pygame.font.SysFont('Arial', 40)
   tTitle = myfont.render('2048', False, (0, 0, 0))
   screen.blit(tTitle,(150,30))

   button1 = pygame.Rect(100, 100, 200, 50)
   button2 = pygame.Rect(100, 170, 200, 50)
   button3 = pygame.Rect(100, 240, 200, 50)
   button4 = pygame.Rect(100, 310, 200, 50)
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
                     col = 6
                     row = 6
                     sflag = False
               if button3.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))
                     col = 8
                     row = 8
                     sflag = False
               if button4.collidepoint(mouse_pos):
                    # prints current location of mouse
                     print('button was pressed at {0}'.format(mouse_pos))
         tNormal = myfont.render('Normal', False, (0, 0, 0))
         tHard = myfont.render('Hard', False, (0, 0, 0))
         tExtereme = myfont.render('Extereme', False, (0, 0, 0))
         tHelper = myfont.render('Helper', False, (0, 0, 0))
         pygame.draw.rect(screen, [242, 177, 121], button1)  # draw button
         pygame.draw.rect(screen, [245, 149, 99], button2)  # draw button
         pygame.draw.rect(screen, [246, 124, 95], button3)  # draw button
         pygame.draw.rect(screen, [246, 94, 59], button4)  # draw button
         screen.blit(tNormal,(115,100))
         screen.blit(tHard,(115,170))
         screen.blit(tExtereme,(115,240))
         screen.blit(tHelper,(115,310))
         pygame.display.update()
   thisCol = 100 * col + ((col + 1) * 10)
   thisRow = 150 * col + ((row + 1) * 10)
   pygame.display.set_mode((thisRow, thisCol))
   game = Game(w_surface,row,col)
   game.play() 
   pygame.quit()


class Game:
   

   def __init__(self, surface, rows, cols):
      self.surface = surface
      self.bg_color = pygame.Color(146, 135, 125)
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
      pos=[0,0]#pos to display
      myfont=pygame.font.SysFont('a',72)      
      for r in self.model.getBoard():
         for c in r:
            tmp=myfont.render(str(c), True, [255, 255, 255])            
            self.surface.blit(tmp,pos)
            pos[0]+=72
         pos[1]+=72
         pos[0]=0
      pygame.display.update()
      
      
   def update(self):
      if self.isover():
         self.continue_game=False
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            self.close_clicked=True            
         elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_a]:
               self.model.move('a')
            if pygame.key.get_pressed()[pygame.K_s]:
               self.model.move('s')            
            if pygame.key.get_pressed()[pygame.K_d]:
               self.model.move('d')   
            if pygame.key.get_pressed()[pygame.K_w]:
               self.model.move('w')                 
            
   def decide_continue(self):
      if self.isover==True:
         self.continue_game = False
         
         
   def isover(self):
      if self.model.getAvailableMove()==[]:
         return True
      return False




   
main()