#!/usr/bin/python
import sys
import argparse
import tty
import curses
from datetime import datetime
from time import time, sleep
from os import listdir
import pygame
from random import shuffle
from curses import wrapper

ENTER_KEY = 10
SPACE_KEY = 32

def main(stdscr):
    stdscr.nodelay(True)

    parser = argparse.ArgumentParser()
    parser.add_argument("hour", help="The number of the hour you want to wake up at from 1-24", type=int)
    parser.add_argument("minute", help="The minute you wish to wake up at from 0-59", type=int)

    args = parser.parse_args()

    seconds = calcTime(args.hour, args.minute)
    runAlarm(seconds, stdscr)

def calcTime(hour, minute):
    wake_seconds = hour * 3600 + minute * 60
    now_seconds = datetime.now().minute * 60 + datetime.now().hour * 3600

    seconds = wake_seconds - now_seconds

    if(seconds < 0):
        seconds = 3600 * 24 + seconds

    return seconds

def runAlarm(seconds, stdscr):
    print("Alarm starting")
    start = time()
    while(time() - start < seconds):
        pass
    playMusic(stdscr)

def playMusic(stdscr):
    songs = listdir('music')
    shuffle(songs)

    pygame.mixer.init()
    pygame.mixer.music.load('music/' + songs[0])
    pygame.mixer.music.play()

    i = 9
    while i:
        pygame.mixer.music.queue('music/' + songs[i])
        i -= 1

    print('Playing music')
    while pygame.mixer.music.get_busy():
        if (stdscr.getch() == SPACE_KEY or stdscr.getch() == ENTER_KEY):
            break

    pygame.mixer.music.stop()

    

if __name__ == '__main__':
    wrapper(main)

