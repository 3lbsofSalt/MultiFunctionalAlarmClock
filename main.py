#!/usr/bin/python
import sys
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hour", help="The number of the hour you want to wake up at from 1-24", type=int)
    parser.add_argument("minute", help="The minute you wish to wake up at from 0-59", type=int)

    args = parser.parse_args()

    seconds = calcTime(args.hour, args.minute)
    runAlarm(seconds)

def calcTime(hour, minute):
    wake_seconds = hour * 3600 + minute * 60
    now_seconds = datetime.now().minute * 60 + datetime.now().hour * 3600

    seconds = wake_seconds - now_seconds

    if(seconds < 0):
        seconds = 3600 * 24 + seconds

    return seconds

def runAlarm(seconds):
    start = datetime.timestamp()
    while(datetime.timestamp() - start < seconds):
        pass
    print("Yay! It made it to the right time!")


if __name__ == '__main__':
    main()
