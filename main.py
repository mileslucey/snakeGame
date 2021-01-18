import sys, pygame, random
from pygame.math import Vector2



right = Vector2(1, 0)
left = Vector2(-1, 0)
up = Vector2(0, -1)
down = Vector2(0, 1)
cellSize = 40
cellNumber = 20

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = right
    def drawSnake(self):
        for block in self.body: # Create for loop to draw the snake utilizing two dimensional vectors for readability
            block_rect = pygame.Rect(int(block.x * cellSize), int(block.y * cellSize), cellSize, cellSize)
            pygame.draw.rect(screen, (100, 0, 0), block_rect)
    def moveSnake(self):
        bodyCopy = self.body[:-1] 
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]
    def addBlock(self):
        bodyCopy = self.body[:] 
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]       

class Apple: 
    def __init__(self):
        self.x = random.randrange(0, cellNumber)
        self.y = random.randrange(0, cellNumber)
        self.position = Vector2(self.x, self.y) # Use two dimensional vector to establish position on the grid. This will make the code more readable and make this program easier to work with

    def drawFood(self):
        food = pygame.Rect(int(self.position.x * cellSize), int(self.position.y * cellSize), cellSize, cellSize)
        # pygame.draw.rect(screen, (126, 166, 140), food)
        # pygame.draw.rect(screen, (126, 166, 140), appleImg)
        screen.blit(appleImg, food)
    
    def randomize(self):
        self.x = random.randrange(0, cellNumber)
        self.y = random.randrange(0, cellNumber)
        self.position = Vector2(self.x, self.y) # Use two dimensional vector to establish position on the grid. This will make the code more readable and make this program easier to work with




class Main():
    def __init__(self):
        self.snake = Snake()
        self.food = Apple()
    
    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFail()

    def drawElements(self):
        self.food.drawFood()
        self.snake.drawSnake()
    
    def checkCollision(self):
        if self.food.position == self.snake.body[0]:
            self.food.randomize()
            self.snake.addBlock()
    def checkFail(self):
        if not 0 <= self.snake.body[0].x < cellNumber or not 0 <= self.snake.body[0].y < cellNumber:
            self.gameOver()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver()
    def gameOver(self):
        pygame.quit()
        sys.exit()



pygame.init() # Initialize the pygame library

mainGame = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) # Trigger event every 150 milliseconds


screen = pygame.display.set_mode((cellSize * cellNumber, cellSize * cellNumber)) # Establish the height and width of the screen
clock = pygame.time.Clock() # Create clock object to limit how fast while loop will run -- this enables the game to run more consistently on different computers

# appleImg = pygame.transform.scale(pygame.image.load('images/apple.png'), (40, 40)).convert_alpha() # Define icon for the apple
appleImg = pygame.transform.scale(pygame.image.load('images/apple.png'), (40, 40)).convert_alpha()




running = True # Set running = True to create infinite loop to keep program going




while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Enable program to quit
            running = False
            sys.exit()
        if event.type == SCREEN_UPDATE:
            mainGame.update()

        if event.type == pygame.KEYDOWN: # Create if statements to determine which arrow key was last clicked; the last clicked arrow key will trigger which direction the snake moves
            if event.key == pygame.K_LEFT:
                if mainGame.snake.direction != right:
                    mainGame.snake.direction = left
            if event.key == pygame.K_RIGHT:
                if mainGame.snake.direction != left:
                    mainGame.snake.direction = right
            if event.key == pygame.K_UP:
                if mainGame.snake.direction != down:  
                    mainGame.snake.direction = up
            if event.key == pygame.K_DOWN:
                if mainGame.snake.direction != up:
                    mainGame.snake.direction = down
    screen.fill((14, 124, 123)) # Establish the fill color of the background
    mainGame.drawElements()

    pygame.display.update() #Update display
    clock.tick(60) # Ensures game will never run faster than 60 frames/second