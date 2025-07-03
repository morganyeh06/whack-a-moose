# Morgan Yeh
# October 29, 2021
# This is my Whack A Moose game for the final project

import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)

#change display name of pygame window    
pygame.display.set_caption('Whack A Moose')
mooseImg0 = pygame.image.load("Images/moose.png")
pygame.display.set_icon(mooseImg0)
#===============DRAW HERE====================
score = 0
highscore = 0
lives = 3
misses = 0
syrup_charge = 0
moose_kills = 0

def start_screen():
    screen.fill((0, 0, 0))
    
    #Title
    font = pygame.font.SysFont("Calibri", 60, True, False)
    titleImg = font.render("WHACK A MOOSE", True, (255, 255, 255))
    screen.blit(titleImg, [175, 50])
    
    #start and quit options
    pygame.draw.rect(screen, (0, 200, 0), [100, 400, 200, 100])
    pygame.draw.rect(screen, (255, 0, 0), [500, 400, 200, 100])
    
    playImg = font.render("PLAY", True, (255, 255, 255))
    quitImg = font.render("QUIT", True, (255, 255, 255))
    
    screen.blit(playImg, [138, 420])
    screen.blit(quitImg, [536, 420])
    
    #Images
    mooseImg = pygame.image.load("Images/moose.png")
    mooseImg = pygame.transform.scale(mooseImg, (230, 200))
    screen.blit(mooseImg, [300, 150])
    
    hammerImg = pygame.image.load("Images/hammer.png")
    hammerImg = pygame.transform.scale(hammerImg, (184, 176))
    screen.blit(hammerImg, [150, 160])
    
    syrupImg = pygame.image.load("Images/syrup.png")
    syrupImg = pygame.transform.scale(syrupImg, [111, 121])
    screen.blit(syrupImg, [540, 190])
    
    #made in canada stamp
    canadaImg = pygame.image.load("Images/canada.png")
    canadaImg = pygame.transform.scale(canadaImg, [125, 125])
    canadaImg = pygame.transform.rotate(canadaImg, 30)
    screen.blit(canadaImg, [0, 0])    
    
def game_screen():
    screen.fill((0,150,235))
    #making mouse cursor not visible
    pygame.mouse.set_visible(False)
    
    #ground
    pygame.draw.rect(screen, (104, 65, 50), [0, 300, 800, 300])
    
    #road
    pygame.draw.polygon(screen, (71,72,76), [[-100, 600], [100, 600], [450, 300], [400, 300]])    
    
    #forest
    forestImg = pygame.image.load("Images/forest.png")
    forestImg = pygame.transform.scale(forestImg, (800, 427))
    screen.blit(forestImg, [-625, 80])
    
    forest2Img = pygame.image.load("Images/forest.png")
    forest2Img = pygame.transform.scale(forest2Img, (800, 427))
    screen.blit(forestImg, [350, 80])    
    
    forest3 = pygame.image.load("Images/forest.png")
    forest3 = pygame.transform.scale(forestImg, (720, 384))
    screen.blit(forest3, [0, 30])
    
    #sun
    pygame.draw.circle(screen, (255, 255, 0), [0, 0], 75)
    
    #score
    font = pygame.font.SysFont("Calibri", 40, False, False)
    scoreImg = font.render(("Score: " + str(score)), True, (255, 255, 255))
    screen.blit(scoreImg, [80, 30])
    
    #lives
    heartx = 600
    emptyx = 673
    
    heartImg = pygame.image.load("Images/heart.png")
    heartImg = pygame.transform.scale(heartImg, (51,51))
    for i in range(lives):
        screen.blit(heartImg, [heartx, 25])
        heartx = heartx + 50
        
    emptyheart = pygame.image.load("Images/empty_heart.png")
    emptyheart = pygame.transform.scale(emptyheart, (100, 100))
    for i in range(misses):
        screen.blit(emptyheart, [emptyx, -3])
        emptyx = emptyx - 50
        
    #Syrup charge bar
    pygame.draw.rect(screen, (0, 0, 0), [325, 32, 200, 30])
    
    charge_barx = 325
    
    #bar starts off empty, fills up over time
    for i in range(syrup_charge):
        pygame.draw.rect(screen, (187, 147, 81), [charge_barx, 32, 40, 30])
        pygame.draw.rect(screen, (0, 0, 0), [charge_barx, 32, 40, 30], 1)
        charge_barx = charge_barx + 40
        
    if syrup_charge == 5:
        pygame.draw.rect(screen, (255, 255, 255), [325, 32, 200, 30], 3)    
    
    font = pygame.font.SysFont("Calibri", 20, True, True)
    syrup_bar_text = font.render("SYRUP CHARGE", True, (255, 255, 255))
    screen.blit(syrup_bar_text, [360, 38])   
    
def moose():
    mooseImg = pygame.image.load("Images/moose.png")
    mooseImg1 = pygame.transform.scale(mooseImg, (126,96))
    
    screen.blit(mooseImg1, [moosex1, moosey1])
    
def end_screen():
    #game over text
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("Calibri", 60, True, False)
    game_over = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over, [250, 100])
    
    #player's score
    font = pygame.font.SysFont("Calibri", 60, False, False)
    end_score = font.render(("Score: " + str(score)), True, (255,255,255))
    screen.blit(end_score, [306, 240])
        
#===============END DRAWING==================
done = False
gameover = False

start_game = False
syrup_drop = False

game_over_sound = False

tutorial_status = False

import random

#position of bird
birdx = 5000

#positions of all the moose
moosex1 = random.randrange(900, 1200)
moosey1 = random.randrange(350, 500)

moosex2 = random.randrange(900, 1200)
moosey2 = random.randrange(350, 500)

moosex3 = random.randrange(900, 1200)
moosey3 = random.randrange(350, 500)

moosex4 = random.randrange(900, 1200)
moosey4 = random.randrange(350, 500)
  
moose_move = 5

#sound effects
bonk_sfx = pygame.mixer.Sound("Sounds/bonk.wav")
whoosh_sfx = pygame.mixer.Sound("Sounds/whoosh.wav")
rubber_duck_sfx = pygame.mixer.Sound("Sounds/rubber_duck.wav")
boom_sfx = pygame.mixer.Sound("Sounds/boom.wav")
beep_sfx = pygame.mixer.Sound("Sounds/beep(1).wav")
beep2_sfx = pygame.mixer.Sound("Sounds/beep2.wav")
heart_loss_sfx = pygame.mixer.Sound("Sounds/losing_drums.wav")
game_over_sfx = pygame.mixer.Sound("Sounds/game_over.wav")

clock = pygame.time.Clock()
while not done:
        
    start_screen()
    
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    #display game screen if PLAY is pressed
    if start_game == True and gameover == False:
        game_screen()        
        moose()
        moosex1 = moosex1 - moose_move
        #lose life if moose exit screen
        if moosex1 <= -100:
            moosex1 = random.randrange(900, 1200)
            moosey1 = random.randrange(350, 500)
            pygame.mixer.Sound.play(heart_loss_sfx)
            lives = lives - 1
            misses = misses + 1
        if moosex2 <= -100:
            moosex2 = random.randrange(900, 1200)
            moosey2 = random.randrange(350, 500)
            pygame.mixer.Sound.play(heart_loss_sfx)
            lives = lives - 1
            misses = misses + 1
        if moosex3 <= -100:
            moosex3 = random.randrange(900, 1200)
            moosey3 = random.randrange(350, 500)
            pygame.mixer.Sound.play(heart_loss_sfx)
            lives = lives - 1
            misses = misses + 1
        if moosex4 <= -100:
            moosex4 = random.randrange(900, 1200)
            moosey4 = random.randrange(350, 500)
            pygame.mixer.Sound.play(heart_loss_sfx)
            lives = lives - 1
            misses = misses + 1        
            
    #Add second moose if more 8 or more killed.
    if moose_kills >= 8 and gameover == False:
        mooseImg2 = pygame.image.load("Images/moose.png")
        mooseImg2 = pygame.transform.scale(mooseImg2, (126,96))
                
        screen.blit(mooseImg2, [moosex2, moosey2])
                
        moosex2 = moosex2 - moose_move
    
    #Add third moose after 16 kills    
    if moose_kills >= 16 and gameover == False:
        mooseImg3 = pygame.image.load("Images/moose.png")
        mooseImg3 = pygame.transform.scale(mooseImg3, (126,96))
                    
        screen.blit(mooseImg3, [moosex3, moosey3])
                    
        moosex3 = moosex3 - moose_move
        
    #Add fourth moose after 30 kills    
    if moose_kills >= 30 and gameover == False:
        mooseImg4 = pygame.image.load("Images/moose.png")
        mooseImg4 = pygame.transform.scale(mooseImg4, (126,96))
                        
        screen.blit(mooseImg4, [moosex4, moosey4])
                        
        moosex4 = moosex4 - moose_move    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons = pygame.mouse.get_pressed()
            #Move to game screen if PLAY is pressed
            if buttons[0] == True and (x in range(100, 301) and y in range(400, 501)) and start_game == False:
                start_game = True
            #Close window if QUIT is pressed
            if buttons[0] == True and (x in range(500, 701) and y in range(400, 501)) and start_game == False:
                done = True
                
            #return to game screen if play again is pressed
            if buttons[0] == True and (x in range(100, 301) and y in range(400, 501)) and gameover == True:
                #reset variables
                score = 0
                lives = 3
                misses = 0
                syrup_charge = 0
                moose_kills = 0
                moose_move = 5
                
                #respawn all moose off screen
                moosex1 = random.randrange(900, 1200)
                moosey1 = random.randrange(350, 500)
                
                moosex2 = random.randrange(900, 1200)
                moosey2 = random.randrange(350, 500)
                
                moosex3 = random.randrange(900, 1200)
                moosey3 = random.randrange(350, 500)
                
                moosex4 = random.randrange(900, 1200)
                moosey4 = random.randrange(350, 500)                        
                
                start_game = True
                gameover = False
                game_over_sound = False
                             
            #Fill syrup bar to max if bird is clicked on, play sfx
            if buttons[0] == True and (x in range(birdx, birdx+51) and y in range(75, 119)):
                pygame.mixer.Sound.play(rubber_duck_sfx)
                pygame.mixer.Sound.play(beep_sfx)                
                
                syrup_charge = 5
                score = score + 10
                birdx = 5000
            
            #Whoosh sound effect if left clicked without hitting anything
            if buttons[0] == True and [(x not in range(moosex1, moosex1+127) and y not in range(moosey1, moosey1+97)) or (x not in range(moosex2, moosey2+127) and y not in range(moosey2, moosey2+97)) or (x not in range(moosex3, moosex3+127) and y not in range(moosey3, moosey3+97)) or (x not in range(moosex4, moosex4+127) and y not in range(moosey4, moosey4+97))] and start_game == True:
                pygame.mixer.Sound.play(whoosh_sfx)
             
            #Add one to score and respawn moose when clicked, play sound effect        
            if buttons[0] == True and (x in range(moosex1, moosex1+127) and y in range(moosey1, moosey1+97)):    
                pygame.mixer.Sound.play(bonk_sfx)
                
                score = score + 1
                moose_kills = moose_kills + 1
                
                mooseImg = pygame.image.load("Images/moose.png")
                mooseImg1 = pygame.transform.scale(mooseImg, (126,96))
                                  
                moosex1 = random.randrange(900, 1200)
                moosey1 = random.randrange(350, 500)
                
                #For every 5 moose, add one to the syrup charge (max 5)
                if score % 5 == 0 and score > 0:
                    if syrup_charge == 5:
                        syrup_charge = syrup_charge + 0
                    else:
                        syrup_charge = syrup_charge + 1
                    
                    #moose get faster    
                    moose_move = moose_move + 1
                    
                #beep sound fx when bar is full    
                if syrup_charge == 5:
                    pygame.mixer.Sound.play(beep_sfx)                
            
            #same thing happens to the second moose when clicked
            if buttons[0] == True and (x in range(moosex2, moosex2+127) and y in range(moosey2, moosey2+97)):    
                
                pygame.mixer.Sound.play(bonk_sfx)
                
                score = score + 1
                moose_kills = moose_kills + 1
                        
                mooseImg = pygame.image.load("Images/moose.png")
                mooseImg2 = pygame.transform.scale(mooseImg, (126,96))
                                          
                moosex2 = random.randrange(900, 1200)
                moosey2 = random.randrange(350, 500)
                        
                #For every 5 moose, add one to the syrup charge (max 5)
                if score % 5 == 0 and score > 0:
                    if syrup_charge == 5:
                        syrup_charge = syrup_charge + 0
                    else:
                        syrup_charge = syrup_charge + 1
                            
                    #moose get faster    
                    moose_move = moose_move + 1
                    
                #beep sound fx when bar is full    
                if syrup_charge == 5:
                    pygame.mixer.Sound.play(beep_sfx)                 
                    
            #same thing happens to the third moose when clicked
            if buttons[0] == True and (x in range(moosex3, moosex3+127) and y in range(moosey3, moosey3+97)):    
                
                pygame.mixer.Sound.play(bonk_sfx)
                
                score = score + 1
                moose_kills = moose_kills + 1
                                
                mooseImg = pygame.image.load("Images/moose.png")
                mooseImg3 = pygame.transform.scale(mooseImg, (126,96))
                                                  
                moosex3 = random.randrange(900, 1200)
                moosey3 = random.randrange(350, 500)
                                
                #For every 5 moose, add one to the syrup charge (max 5)
                if score % 5 == 0 and score > 0:
                    if syrup_charge == 5:
                        syrup_charge = syrup_charge + 0
                    else:
                        syrup_charge = syrup_charge + 1
                                    
                    #moose get faster    
                    moose_move = moose_move + 1
                
                #beep sfx when bar is full    
                if syrup_charge == 5:
                    pygame.mixer.Sound.play(beep_sfx)
                    
            #Same thing happens to fourth moose when clicked       
            if buttons[0] == True and (x in range(moosex4, moosex4+127) and y in range(moosey4, moosey4+97)):     
                
                pygame.mixer.Sound.play(bonk_sfx)
                score = score + 1
                moose_kills = moose_kills + 1
                        
                mooseImg = pygame.image.load("Images/moose.png")
                mooseImg4 = pygame.transform.scale(mooseImg, (126,96))
                                          
                moosex4 = random.randrange(900, 1200)
                moosey4 = random.randrange(350, 500)
                        
                #For every 5 moose, add one to the syrup charge (max 5)
                if score % 5 == 0 and score > 0:
                    if syrup_charge == 5:
                        syrup_charge = syrup_charge + 0
                    else:
                        syrup_charge = syrup_charge + 1
                            
                    #moose get faster    
                    moose_move = moose_move + 1    
                
                #beep sound fx when bar is full    
                if syrup_charge == 5:
                    pygame.mixer.Sound.play(beep_sfx)                
            
            #syrup bottle drops when right clicked as well        
            if buttons[2] == True and syrup_charge == 5:
                syrup_charge = 0 
                
                syrupx = random.randrange(400, 750)
                syrupy = random.randrange(400, 550)                
                
                pygame.draw.rect(screen, (0, 0, 0), [325, 32, 200, 30])
                
                font = pygame.font.SysFont("Calibri", 20, True, True)
                syrup_bar_text = font.render("SYRUP CHARGE", True, (255, 255, 255))
                screen.blit(syrup_bar_text, [360, 38])
                
                #play sound effect
                pygame.mixer.Sound.play(beep2_sfx)                
                
                syrup_drop = True                
            
        #Syrup bar reverts to 0 when space bar pressed, syrup bottle drops      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and syrup_charge == 5:
                syrup_charge = 0 
                
                syrupx = random.randrange(400, 750)
                syrupy = random.randrange(400, 550)                
                
                pygame.draw.rect(screen, (0, 0, 0), [325, 32, 200, 30])
                
                font = pygame.font.SysFont("Calibri", 20, True, True)
                syrup_bar_text = font.render("SYRUP CHARGE", True, (255, 255, 255))
                screen.blit(syrup_bar_text, [360, 38])
                
                #play sound effect
                pygame.mixer.Sound.play(beep2_sfx)
                
                syrup_drop = True
         
    if syrup_drop == True:
        #syrup bottle drops
        syrupImg = pygame.image.load("Images/syrup.png")
        syrupImg = pygame.transform.scale(syrupImg, (31,32))
        screen.blit(syrupImg, [syrupx, syrupy])  
        
        #hit box for syrup
        pygame.draw.rect(screen, (187, 147, 81), [syrupx-50, syrupy-50, 130, 130], 2)
    
        #Moose get hit if within syrup hitbox
        moose_rect1 = pygame.Rect([moosex1+50, moosey1-10, 126, 96])
        moose_rect2 = pygame.Rect([moosex2+50, moosey2-10, 126, 96])
        moose_rect3 = pygame.Rect([moosex3+50, moosey3-10, 126, 96])
        moose_rect4 = pygame.Rect([moosex4+50, moosey4-10, 126, 96])
        
        syrup_rect = pygame.Rect([syrupx-50, syrupy-50, 130, 130])
        
        #Scenarios if moose are within syrup hitbox
        #respawn moose and add to score
        if moose_rect1.colliderect(syrup_rect):
            pygame.mixer.Sound.play(boom_sfx)
            
            moosex1 = random.randrange(900, 1200)
            moosey1 = random.randrange(350, 500)
            score = score + 1
            syrup_drop = False
        
        if moose_rect2.colliderect(syrup_rect):
            pygame.mixer.Sound.play(boom_sfx)
            
            moosex2 = random.randrange(900, 1200)
            moosey2 = random.randrange(350, 500)
            score = score + 1
            syrup_drop = False
            
        if moose_rect3.colliderect(syrup_rect):
            pygame.mixer.Sound.play(boom_sfx)
            
            moosex2 = random.randrange(900, 1200)
            moosey3 = random.randrange(350, 500)
            score = score + 1
            syrup_drop = False 
            
        if moose_rect4.colliderect(syrup_rect):
            pygame.mixer.Sound.play(boom_sfx)
            
            moosex4 = random.randrange(900, 1200)
            moosey4 = random.randrange(350, 500)
            score = score + 1
            syrup_drop = False    
    
    #bird moves very quickly across screen    
    birdImg = pygame.image.load("Images/bird.png")
    birdImg = pygame.transform.scale(birdImg, (51,43))    
    screen.blit(birdImg, [birdx, 75])
              
    if start_game == True:
        birdx = birdx - 30
        if birdx <= -60:
            birdx = 5000          
        #hammer that follows mouse
        hammer = pygame.image.load("Images/hammer.png")
        hammer = pygame.transform.scale(hammer, (115, 110))
        screen.blit(hammer, [x-80, y-50])
        
    #game over screen if no more lives    
    if lives <= 0:
        if game_over_sound == False:
            #game over sound
            pygame.mixer.Sound.play(game_over_sfx)
            game_over_sound = True
        
        #Moose stop moving
        moose_move = 0
        
        start_game = False
        gameover = True
        
        end_screen()
        
        #Mouse becomes visible again
        pygame.mouse.set_visible(True)
        
        #setting user's highscore
        if score > highscore:
            highscore = score     
        
        #display user's score and highscore
        font = pygame.font.SysFont("Calibri", 60, False, False)    
        highscore_text = font.render(("Highscore: " + str(highscore)), True, (255,255,255))
        screen.blit(highscore_text, [200, 300])        
        
        #Play again or quit options
        font = pygame.font.SysFont("Calibri", 35, True, False)
        font2 = pygame.font.SysFont("Calibri", 60, True, False)
        
        pygame.draw.rect(screen, (0, 200, 0), [100, 400, 200, 100])
        pygame.draw.rect(screen, (0, 0, 0), [100, 400, 200, 100], 2)
        
        pygame.draw.rect(screen, (255, 0, 0), [500, 400, 200, 100])
        pygame.draw.rect(screen, (0, 0, 0), [500, 400, 200, 100], 2)
        
        playagainImg = font.render("PLAY AGAIN", True, (255, 255, 255))
        quitImg = font2.render("QUIT", True, (255, 255, 255))
        
        screen.blit(playagainImg, [115, 430])
        screen.blit(quitImg, [536, 420])        
    else:
        gameover = False
    
    #moose stop moving
    if gameover == True:
        moose_move = 0
    
    #add borders to buttons when mouse is hovering over them
    #Play button
    if (x in range(100, 301) and y in range(400, 501)) and start_game == False:
        pygame.draw.rect(screen, (255,255,255), [100, 400, 200, 100], 5)
        
    #Quit button    
    if (x in range(500, 701) and y in range(400, 501)) and (start_game == False or gameover == True):
        pygame.draw.rect(screen, (255, 255, 255), [500, 400, 200, 100], 5)
        
    #play again button (game over screen)    
    if (x in range(100, 301) and y in range(400, 501)) and gameover == True:
        pygame.draw.rect(screen, (255,255,255), [100, 400, 200, 100], 5)  
        
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()