import pygame
import random
import time


reset = True
high_score = 0

while reset:
    reset = True
    lose = False
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Flappy Bird")
    icon = pygame.image.load('flappibird_icon.png')
    pygame.display.set_icon(icon)

    player_image = pygame.image.load('flappibird.png')
    player_x = 60
    player_y = 300
    playerY_change = 200

    font = pygame.font.Font('freesansbold.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf', 64)

    background_image = pygame.image.load('flappi_background.png')

    score = 0

    def can_score(x1, y1, x2, y2):
        if x2 <= x1 and x1 + 10 <= x2+80 and (y2+ 320 < y1 < y2+ 410):
            return True
        else:
            return False

    def is_collision(x1, y1, x2, y2):
        if x2 <= x1 and x1 +10 <= x2+80 and (y1 <= y2 + 320 or y1 >= y2+ 410):
            return True
        else:
            return False

    def show_score():
        scoring = font.render(str(score), True, (255, 255, 255))
        screen.blit(scoring, (400, 20))

    def gameover(score, high_score):
        if score < high_score:
            gameover1 = font2.render("Game Over!", True, (255, 255, 255))
            gameover2 = font2.render("Score :" + str(score), True, (255, 255, 255))
            screen.blit(gameover1, (220,200))
            screen.blit(gameover2, (260,270))
            return False
        if score >= high_score:
            gameover1 = font2.render("Game Over!", True, (255, 255, 255))
            gameover2 = font.render("New High Score! " + str(score), True, (255, 255, 255))
            screen.blit(gameover1, (220,200))
            screen.blit(gameover2, (260,270))
            return True

    tuyau_image = pygame.image.load('tuyau.png')
    tuyau_x = []
    tuyau_y = []
    tuyauX_change = -0.8
    num_tuyau = 3

    lose = False

    for i in range(num_tuyau):
        tuyau_x.append(800 + 200*i)
        tuyau_y.append(random.randrange(-300, -50))

    def show_tuyau(x, y):
        screen.blit(tuyau_image, (x,y))

    def background():
        screen.blit(background_image, (0,0))

    def show_player(x,y):
        screen.blit(player_image, (x,y))

    reset = True

    ti = time.time()

    running = True
    while running:
        player_x = 60
        player_y = 300
        playerY_change = 120
        tuyauX_change = -0.8
        for i in range(num_tuyau):
            tuyau_x[i] = 800 + 200*i
            tuyau_y[i] = random.randrange(-300, -50)         
        running = True
        while running:
            reset = False
            background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    reset = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        playerY_change = -450
                    if event.key == pygame.K_SPACE and lose:
                        running = False
                        reset = True
                        break
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        playerY_change = 200
            
            show_score()
            for i in range(num_tuyau):
                show_tuyau(tuyau_x[i], tuyau_y[i])
                tuyau_x[i] += tuyauX_change
                if tuyau_x[i] < 0:
                    tuyau_x[i] = 800
                    tuyau_y[i] = random.randrange(-300, -50)   
                if player_y > 600 or is_collision(player_x, player_y, tuyau_x[i], tuyau_y[i]):
                    tuyauX_change = 0
                    playerY_change = 0
                    gameover(score, high_score)
                    if gameover(score, high_score):
                        high_score = score
                    lose = True
                    
                    
            show_score()
            if player_y < 0:
                player_y = 0
            
            for i in range(num_tuyau):
                if can_score(player_x, player_y, tuyau_x[i], tuyau_y[i]):
                    score += 1
            tf = time.time()
            dt = (tf-ti)
            ti = tf
            player_y += playerY_change * dt
            show_player(player_x, player_y)
            pygame.display.update()
