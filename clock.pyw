from datetime import datetime
from playsound import playsound
import time
import os
from threading import  Thread
import pygame



now = datetime.now()
H = now.strftime("%I")
M = now.strftime("%M")
Ses = now.strftime("%p")

def alert():

    pygame.init()

    running = True
    GREY = (150,150,150)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    font = pygame.font.SysFont('sans', 25)

    # text = font.render('Bây giờ là ' + str(Time))

    screen = pygame.display.set_mode((500,200))


    while running:
        screen.fill(WHITE)

        text = font.render('Bây giờ là ' + str(datetime.now().strftime("%I:%M:%p")), True, BLACK)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        Time = font.render(datetime.now().strftime("%I:%M:%p"), True, BLACK)

        screen.blit(text, (110,40))
        screen.blit(text, (110,40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

thread1 = Thread(target = alert)




while True:

    now = datetime.now()
    H = now.strftime("%I")
    M = now.strftime("%M")
    Ses = now.strftime("%p")

    Time = datetime.now().strftime("%I:%M:%p")
    
    # if M != "%M":
    #   print(Time)

    if M == "04":
        print(Time)
        thread1.start()
        # playsound('D:/AlarmClock.mp3')
        time.sleep(60)
        continue