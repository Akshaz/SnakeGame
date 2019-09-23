import pygame, Classes as func

pygame.init()

highScore = 0
width = 750
height = 675

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font('freesansbold.ttf', 42)
score_font = pygame.font.Font('freesansbold.ttf', 24)
text = font.render('Snake Game', True, (255,255,255))
textRect = text.get_rect()
textRect.center = (width // 2, 20)


def restart():
    pygame.display.quit()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")
    return startGame(window)

def startGame(window):
    global highScore
    snake = func.Snake()
    food = func.food()
    running = True

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
        pygame.time.Clock().tick(15)
        window.fill((0,0,0))
        func.boardDraw(window, width, height)
        window.blit(text, textRect)
        window.blit(high_score, high_scoreRect)
        window.blit(score, scoreRect)
        snake.keyPressed()
        snake.moveSnake()
        snake.drawSnake(window)
        #snake.mousePressed()
        food.drawFood(window, snake.isEaten(food.returnFood()))
        if snake.death(width, height):
            running = restart()
        pygame.display.update()
    return False


startGame(window)
pygame.quit()
