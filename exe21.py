#CODE SCRIPT THAT OPEN MUSIC AND PLAY WITH SOME MODULE

import pygame, time

pygame.init()
pygame.mixer.music.load('./music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
time.sleep(5)