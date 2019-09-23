import pygame, Classes as func

pygame.init()                                    

highScore = 0
width = 750                                      #Default width of window
height = 675                                     #Default height of the window

window = pygame.display.set_mode((width, height))  
pygame.display.set_caption("Snake Game")
font = pygame.font.Font('freesansbold.ttf', 42)
score_font = pygame.font.Font('freesansbold.ttf', 24)
text = font.render('Snake Game', True, (255,255,255))
textRect = text.get_rect()
textRect.center = (width // 2, 20)


def restart():                                          #function to restart the game
    pygame.display.quit()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")
    return startGame(window)

def startGame(window):                                  #function to start the game
    global highScore
    snake = func.Snake()
    food = func.food()
    running = True

    #mainloop
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        score = score_font.render(f"Current Score : {snake.getScore()}", True, (255, 255, 255))
        scoreRect = score.get_rect()
        scoreRect.center = (110, 20)
        highScore = highScore if highScore > snake.getScore() else snake.getScore()
        high_score = score_font.render(f"High Score : {highScore}", True, (255, 255, 255))
        high_scoreRect = score.get_rect()
        high_scoreRect.center = (660, 20)

        pygame.time.Clock().tick(15)                #Frame rate
        
        window.fill((0,0,0))                        #Background color
        
        func.boardDraw(window, width, height)       #Draws the lines on the board

        window.blit(text, textRect)
        window.blit(high_score, high_scoreRect)
        window.blit(score, scoreRect)

        snake.keyPressed()                          #Checks for if any arrow key pressed
        snake.moveSnake()                           #To change the cordinates of the head
        snake.drawSnake(window)                     #Draws snake on screen
        #snake.mousePressed()
        food.drawFood(window, snake.isEaten(food.returnFood())) #Checks if food eaten
        if snake.death(width, height):
            running = restart()
        pygame.display.update()                     #Refresh screen
    return False


startGame(window)                                   
pygame.quit()
