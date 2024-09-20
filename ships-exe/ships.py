class GameBoard:
  def __init__(self,size):
    self.size = size
    self.game_board = []
    self.copy_game_board = []
    self.guess_game_board = []
  def create_board(self):
    for i in range(0,self.size):
      self.game_board.append([' '] * self.size)
      self.copy_game_board.append([' '] * self.size)
      self.guess_game_board.append([' '] * self.size)
  def display(self,n):
    for i in range(0,n):
      print(self.game_board[i])
  def display_copy(self,n):
    for i in range(0,n):
      print(self.copy_game_board[i])
  def display_guess_copy(self,n):
    for i in range(0,n):
      print(self.guess_game_board[i])


class Ship:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.count = 0
    self.pos = []
  def create_ship(self,size,position):# przód statku
    x_ = self.x
    y_ = self.y 
    self.count = size
    for i in range(0,size):
      if position == 'vertical':
        self.pos.append((x_,y_))
        x_ = x_ + 1
      elif position == 'horizontal':
        self.pos.append((x_,y_))
        y_ = y_ + 1
      else:
        pass
  def set_ships(self,obj,value):
    for x,y in self.pos:
      obj.game_board[x][y] = 'o'
      obj.copy_game_board[x][y] = 'o'
      self.surroundX(value,obj,x,y)
    
  def check_borders(self,x,y,n):
    return ((x < 0) or (y < 0) or (x > n - 1) or (y > n - 1))


  def surroundX(self,value,obj,x,y):
    n = len(obj.game_board)
   
   # horizontal
    if value == "horizontal":
      if not Ship.check_borders(self,x-1,y-1,n) and obj.copy_game_board[x][y-1] != 'o':
        obj.copy_game_board[x-1][y-1] = 'x'
        obj.copy_game_board[x-1][y] = 'x'
        obj.copy_game_board[x][y-1] = 'x'
      if not Ship.check_borders(self,y+1,x-1,n) and obj.copy_game_board[x][y+1] != 'o':
        obj.copy_game_board[x-1][y+1] = 'x'
        obj.copy_game_board[x-1][y] = 'x'
        obj.copy_game_board[x][y+1] = 'x'
      if not Ship.check_borders(self,x+1,x+1,n): 
        obj.copy_game_board[x+1][y] = 'x'
      if not Ship.check_borders(self,x-1,x-1,n): 
        obj.copy_game_board[x-1][y] = 'x'
      if not Ship.check_borders(self,x+1,y-1,n) and obj.copy_game_board[x][y-1] != 'o':
        obj.copy_game_board[x+1][y-1] = 'x'
        obj.copy_game_board[x+1][y] = 'x'
        obj.copy_game_board[x][y-1] = 'x'
      if not Ship.check_borders(self,y+1,x+1,n) and obj.copy_game_board[x][y+1] != 'o':
        obj.copy_game_board[x][y+1] = 'x'
        obj.copy_game_board[x+1][y] = 'x'
        obj.copy_game_board[x+1][y+1] = 'x'
    # vertical
    elif value == "vertical":
      if not Ship.check_borders(self,x-1,y-1,n) and obj.copy_game_board[x-1][y] != 'o':
        obj.copy_game_board[x-1][y-1] = 'x'
        obj.copy_game_board[x-1][y] = 'x'
        obj.copy_game_board[x][y-1] = 'x'
      if not Ship.check_borders(self,y+1,x-1,n) and obj.copy_game_board[x-1][y] != 'o':
        obj.copy_game_board[x-1][y+1] = 'x'
        obj.copy_game_board[x-1][y] = 'x'
        obj.copy_game_board[x][y+1] = 'x'
      if not Ship.check_borders(self,y+1,y+1,n): 
        obj.copy_game_board[x][y+1] = 'x'
      if not Ship.check_borders(self,y-1,y-1,n): 
        obj.copy_game_board[x][y-1] = 'x'
      if not Ship.check_borders(self,x+1,y-1,n) and obj.copy_game_board[x+1][y] != 'o':
        obj.copy_game_board[x+1][y-1] = 'x'
        obj.copy_game_board[x+1][y] = 'x'
        obj.copy_game_board[x][y-1] = 'x'
      if not Ship.check_borders(self,y+1,x+1,n) and obj.copy_game_board[x+1][y] != 'o':
        obj.copy_game_board[x][y+1] = 'x'
        obj.copy_game_board[x+1][y] = 'x'
        obj.copy_game_board[x+1][y+1] = 'x'
      
class Player(GameBoard):
  def __init__(self,n):
    super().__init__(n)
    self.tab_obj_ships = []
    self.ships = [4]
    self.len = len(self.ships)
  
  def selectField(self,obj_opposite):
    x = int(input("wybierz x :"))
    y = int(input("wybierz y :"))
    if obj_opposite.game_board[x][y] == 'o':
      self.guess_game_board[x][y] == 'o'
      self.decreaseRate(obj_opposite,x,y)
      self.display_guess_copy(n)
      print("\n")
    else:
      self.display_guess_copy(n)
      print("\n")
    
    
  def decreaseRate(self,obj_opposite,x_,y_):
    for obj in obj_opposite.tab_obj_ships:
      for x,y in obj.pos:
        if x == x_ and y == y_:
          obj.count = obj.count - 1
          self.guess_game_board[x][y] = obj_opposite.copy_game_board[x][y]
          obj_opposite.game_board[x][y] = "#"
          if obj.count == 0:
            self.surroundShip(obj_opposite,obj)
            self.len = self.len - 1

  def minXY(self,obj):
    minX = 100
    minY = 100
    for x,y in obj.pos:
      if minX > x:
        minX = x
      if minY > y:
        minY = y
    return (minX,minY)
  
  def maxXY(self,obj):
    maxX = -100
    maxY = -100
    for x,y in obj.pos:
      if maxX < x:
        maxX = x
      if maxY < y:
        maxY = y
    return (maxX,maxY)
  
  def surroundShip(self,obj,ship):
    minX,minY = self.minXY(ship)
    maxX,maxY = self.maxXY(ship)
    minX_ = minX # 0
    maxX_ = maxX # 2
    minY_ = minY # 0
    maxY_ = maxY # 0
    if minY - 1 >= 0:
      minY_ = minY - 1
    if maxY + 1 < n:
      maxY_ = maxY + 1
    if minX - 1 >= 0:
      minX_ = minX - 1
    if maxX + 1 < n:
      maxX_ = maxX + 1

    print(minX_)
    print(maxX_)
    print(minY_)
    print(minY_)
    for i in range(minX_,maxX_+1):
      for j in range(minY_,maxY_+1):
        
        self.guess_game_board[i][j] = obj.copy_game_board[i][j]
  
  def init_table(self):
    self.create_board()
    for ix,key in enumerate(self.ships):
      value = "vertical"
      if key != 1:
        value = input("Choose vertical or horizontal")
      print(f"Wprowadz wsp {ix+1} statku o rozmiarze {key}")
      x = 0
      y = 0
      while True:
        x = int(input(f"Wprowadz x dla {ix+1} statku o wymiarze {key}:"))
        y = int(input(f"Wprowadz y dla {ix+1} statku o wymiarze {key}:"))

        if self.copy_game_board[x][y] == 'o' or self.copy_game_board[x][y] == 'x':
          continue
        elif (value == "horizontal") and (y + key - 1 > n - 1):
          continue
        elif (value == "vertical") and (x + key - 1 > n - 1):
          continue
        elif (x < 0) or (y < 0) or (x > n - 1) or (y > n - 1):
          continue
        break

      ship = Ship(x,y)
      ship.create_ship(key,value)
      ship.set_ships(self,value)
      self.tab_obj_ships.append(ship)
      self.display(n)
      #print(self.tab_obj_ships)

n = 10
player1 = Player(n)
print("Player 1 choose position of board")
player1.init_table()
print("Player 2 choose position of board")
player2 = Player(n)
player2.init_table()

while True:
# logika gry zgaduje player1 na zmiane z player2 
  player1.selectField(player2)

  player2.selectField(player1)
  

  if player1.len == 0:
    print("Win player1")
    break
  if player2.len == 0:
    print("Win player2")
    break



