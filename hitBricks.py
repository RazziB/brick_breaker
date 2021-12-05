import pygame
import math


# Width of window:
windowX = 900
# Height of window:
windowY = 900

# Space between blocks. set at 10
spaceBetween = 10
# Number of blocks. never more than: (to be continued) **** 
maxBlocks = 50
# List of bricks
brickList = []
pygame.init()


pygame.display.set_caption('BRICK BREAKER')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Press Space To Start', True, 'green', 'blue')
textRect = text.get_rect()
textRect.center = (windowX // 2, windowY // 2)


angle = 0.2
window = pygame.display.set_mode((windowX,windowY))

color = (255, 0, 0)

#######################
playerX = windowX/2 - 100 
player = pygame.Rect(playerX, windowY - 40, 200, 30)
ballX = windowX/2
ballY = windowY/2
ball = pygame.Rect(ballX, ballY, 10,10)
#############################################
# Number of line in loop:
line = 1
counter = 0

for i in range(maxBlocks):
    if counter > int((windowX - 30- counter * 10) / 90):
        line = line + 1
        counter = 0
    brickList.append(pygame.Rect(30 + 90 * counter,30*line,80, 20))
    pygame.draw.rect(window, color, brickList[i])
    counter = counter + 1

originalList = brickList.copy()

startedGame = False
dirShiftY = 1
dirShiftX = 1
col = 0
colorSet = ['red', 'yellow', 'green', 'blue', 'cyan', 'orange']
colorNum = 0
run = True


while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False

    keys=pygame.key.get_pressed()


    window.fill(0)
    window.blit(text, textRect)

    
  
   

   
    for i in range (maxBlocks):
        pygame.draw.rect(window, color, brickList[i])


    

    # pygame.draw.rect(window, (0, 255, 0), rect2, 6, 1)
    
    pygame.draw.rect(window, (0,0,255), player, 0,0)
    

    

    if keys[pygame.K_LEFT]:
        if player.left > 0:
            player.left = player.left - 1

 
    
    if keys[pygame.K_RIGHT]:
        if player.right < windowX:
            player.right = player.right + 1
    
    ball.center = (ballX, ballY)
    
    # Draw circle
    pygame.draw.rect(window, colorSet[colorNum % len(colorSet)], ball)
    colorNum += 1
    brickCollided = pygame.Rect.collidelist(ball, brickList)
    if brickCollided != -1:
        print("Hit! " + str(col))
        col+=1
        if ballY > brickList[brickCollided].bottom or ballY < brickList[brickCollided].top:
            dirShiftY *= -1
        if ball.left < brickList[brickCollided].left or ball.right > brickList[brickCollided].right:
            dirShiftX *= -1
        brickList[brickCollided] = pygame.Rect(0,0,0,0)
        
    if pygame.Rect.colliderect(ball, player):
        if ball.left < player.left + ((player.right - player.left) / 2):
            dirShiftX = -1
            if ball.left < player.left + ((player.right - player.left) / 2) - 50:
                angle = 0.4
            else:
                angle = 0.2
        else:
            dirShiftX = 1
            if ball.left >  player.left + ((player.right - player.left) / 2) + 50:
                angle = 0.4
            else:
                angle = 0.2
        dirShiftY *= -1
    

    #########

    if keys[pygame.K_SPACE]:
        startedGame = True
    
    if ball.left < 0:
        dirShiftX = 1
    if ball.right > windowX:
        dirShiftX = -1
    if ballY < 0:
        dirShiftY *= -1
    # RESTART GAME! ########
    if ballY > windowY:
        startedGame = False
        text = font.render('Press Space To Start', True, 'green', 'blue')
        ballX, ballY, playerX, dirShiftY, dirShiftX = windowX/2, windowY/2, windowX/2+100, 1,1
        brickList, col = originalList.copy(), 0
    # ###### ##### #########

    if startedGame:
        ballY -= 0.5*dirShiftY
        ballX += angle*dirShiftX
        text = font.render('Score : ' + str(col), True, 'green', 'blue')


    

    pygame.display.flip()

pygame.quit()


