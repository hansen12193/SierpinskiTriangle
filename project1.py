#----------
#Fall 2013
#CSCI141
import pygame, random, math
pygame.init()

screenWidth = 800
screenHeight = 600

white = (255, 255, 255)
black = (0, 0, 0)

(width, height) = (screenWidth, screenHeight)
screen = pygame.display.set_mode((screenWidth, screenHeight))
array = pygame.PixelArray(screen)

numberOfIterations = 100000

corner1 = ((screenWidth // 2), 0) 
corner2 = (0, screenHeight) 
corner3 = (screenWidth, screenHeight) 

pygame.draw.lines(screen, black, True, [(corner1), (corner2), (corner3)], 1)

x = random.randrange(0, screenWidth)
y = random.randrange(0, screenHeight)

#x = screenWidth//2
#y = screenHeight//2

distance1 = math.sqrt(((screenWidth/2)**2)+(screenHeight)**2)
distance2 = screenWidth

if distance1 > distance2:
    distanceMax = distance1
else:
    distanceMax = distance2

for i in range(numberOfIterations):
    corners = [corner1, corner2, corner3]
    randomCorner = random.choice(corners)
    xOfRandomCorner = randomCorner [0]
    yOfRandomCorner = randomCorner [1]

    x = (x + xOfRandomCorner)//2
    y = (y + yOfRandomCorner)//2

    distanceToCorner1 = math.sqrt((x**2)+(screenHeight-y)**2)
    distanceToCorner2 = math.sqrt((((screenWidth/2)-x)**2)+(y**2))
    distanceToCorner3 = math.sqrt(((screenWidth-x)**2)+(screenHeight-y)**2)

    redColor = 255 * (distanceToCorner1 / distanceMax)
    greenColor = 255 * (distanceToCorner2/ distanceMax)
    blueColor = 255 * (distanceToCorner3/ distanceMax)
        
    array [x] [y] = (redColor, greenColor, blueColor)

pygame.display.flip()
