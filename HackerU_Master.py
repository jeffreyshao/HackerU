#Imported libraries

#Import Raspberry Pi GPIO library and set it as 'GPIO'
import RPi.GPIO as GPIO
#Allows for using operating system dependent functionality. Basically, it opens files
import os
import sys
#Allows for running of different processes. It's what triggers the video player
from subprocess import Popen

GPIO.setmode(GPIO.BCM)

#------------- TO DO -----------------#
#------------ Set up the pins ------------#
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#------------- TO DO -----------------#
#-----Set up the movies variables-----#

movie1 = ("/home/pi/Videos/movie1.mp4")
movie2 = ("/home/pi/Videos/movie2.mp4")

#---------------- TO DO ------------------#
#-----Set all state variables as true-----#

#This assumes that all states are true, meaning you have a closed complete circuit
last_state1 = True
last_state2 = True

input_state1 = True
input_state2 = True
quit_video = True


player = False

#Always running
while True:

#------------- TO DO -----------------#
#-------Read states of inputs---------#
    input_state1 = GPIO.input(17)
    input_state2 = GPIO.input(18)
    quit_video = GPIO.input(24)

    #------------- TO DO -----------------#
    #If GPIO(17) is shorted to Ground
    #If the input_state isn't the last state, we have a short circuit. In which case we trigger the command
    if input_state1 != last_state1:

        #If the video playing isn't video1, kill the video and play video1
        if (player and not input_state1):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True
        #Otherwise, just play video1
        elif not input_state1:
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True

    #------------- TO DO -----------------#
    #---------Repeat for 2nd GPIO---------#
    #If GPIO(18) is shorted to Ground
    elif input_state2 != last_state2:
        if (player and not input_state2):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie2])
            player = True
        elif not input_state2:
            omxc = Popen(['omxplayer', '-b', movie2])
            player = True

    #------------- TO DO -----------------#
    #If omxplayer is running and GIOP(17) and GPIO(18) are not shorted to Ground
    elif (player and input_state1 and input_state2):
        os.system('killall omxplayer.bin')
        player = False


    #GPIO(24) to close omxplayer manually - used during debug
    if quit_video == False:
        os.system('killall omxplayer.bin')
        player = False

    #Set last_input states
    last_state1 = input_state1
    last_state2 = input_state2
