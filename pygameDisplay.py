
import pygame
import gameModel


def main():
   row,col = 0, 0
   while True:
      size = input("Please input the size of the game(rows+one single space+columns): ")
      if len(size)==3 and '1'<size[0] and '1'<size[2]:
         row = int(size[0])
         col = int(size[2])
         break   
   
   pygame.init()
   pygame.display.set_mode((505, 405))
   pygame.display.set_caption('2048')   
   w_surface = pygame.display.get_surface() 
   game = Game(w_surface,row,col)
   game.play() 
   pygame.quit() 


class Game:
   

   def __init__(self, surface, rows, cols):
      self.surface = surface
      self.bg_color = pygame.Color('black')
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