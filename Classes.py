import pygame, math, random

class food:

    def __init__(self):
        self.food = [random.randint(0, 50)*15, random.randint(3, 40)*15]

    def drawRect(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.food[0], self.food[1], 15, 15))

    def drawFood(self,window,flag):
        if flag:
            self.food[0] = random.randint(0, 50)*15
            self.food[1] = random.randint(3, 40)*15
        self.drawRect(window)

    def returnFood(self):
        return self.food


class Snake:

    def __init__(self):
        self.coor = [45, 45]
        self.count = 1
        self.direction = ""
        self.coordinates = []
        self.food = food()

    def drawRect(self, window, coordinate):
        pygame.draw.rect(window, (0,255,0), (coordinate[0], coordinate[1], 15, 15))

    def moveSnake(self):
        if self.direction == "left":
            self.coor[0]-=15
        elif self.direction == "right":
            self.coor[0]+=15
        elif self.direction == "up":
            self.coor[1]-=15
        elif self.direction == "down":
            self.coor[1]+=15

    def drawSnake(self, window):
        self.coordinates.append(tuple(self.coor))
        while (len(self.coordinates) > self.count):
            self.coordinates.pop(0)
        for i in self.coordinates:
            self.drawRect(window, i)

    def isEaten(self, food):
        if self.coor[0] == food[0] and self.coor[1] == food[1]:
            self.count+=1
            return True
        else:
            return False

    def death(self, width, height):
        if self.coor[0] == width or self.coor[1] == height or self.coor[0] < 0 or self.coor[1] < 45:
            return True
        else:
            for i in range(0, len(self.coordinates)-1):
                if self.coordinates[i] == tuple(self.coor):
                    return True
            return False

    def getScore(self):
        return self.count

    # def mousePressed(self):
    #     if pygame.mouse.get_pressed()[0]:
    #         self.count+=1

    def keyPressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not(keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            self.direction = "left"
        elif keys[pygame.K_RIGHT] and not(keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            self.direction = "right"
        elif keys[pygame.K_UP] and not(keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_DOWN]):
            self.direction = "up"
        elif keys[pygame.K_DOWN] and not(keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_LEFT]):
            self.direction = "down"

def boardDraw(window, width, height):
    for i in range(0, width, 15):
        pygame.draw.line(window, (255, 255, 255), (i, 45), (i, height))
    for i in range(0, height, 15):
        if i>=45:
            pygame.draw.line(window, (255, 255, 255), (0, i), (width, i))
