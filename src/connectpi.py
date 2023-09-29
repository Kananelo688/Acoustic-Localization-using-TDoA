#Adapted from https://github.com/RavoDavo/Acoustic-Triangulation-using-TDOA/blob/main/Record_Command.py

import multiprocessing
from time import sleep
import os
import sys
import sounddevice as sd
import soundfile as sf



#Define SSH record command for each Raspberry Pi 
def pi1():
    os.system("ssh eee3097s@192.168.137.138 sudo nice -n -20 arecord -D plughw:0 -c2 -r 48000 -f S32_LE -t wav -V stereo -v signal1.wav")
    
def pi2():
    os.system("ssh eee3097s@192.168.137.107 sudo nice -n -20 arecord -D plughw:0 -c2 -r 48000 -f S32_LE -t wav -V stereo -v signal2.wav")
    
    
if __name__ == '__main__':
    argumentList = sys.argv[1:]                       #Read in File name
    file_name = argumentList[0] 
    os.system("mkdir "+str(file_name))                #Create directory
    
    #Define parallel processes and target the ssh command
    process1 = multiprocessing.Process(target=pi1)
    process2 = multiprocessing.Process(target=pi2)
    

    #Execute parallel processes to begin recording
    process1.start()
    process2.start()
    
    sleep(5)                                           #Wait 5 seconds
    
    #Read in calibration signal
    #filename = 'chirp_0_15000_5s.wav' 

    #data, fs = sf.read(filename, dtype='float32')      # Extract data and sampling rate from file
    #sd.play(data, fs)                                  # Play calibration signal
    #status = sd.wait()                                 # Wait until file is done playing
    
    sleep(15)                                          #Wait until recordings fininsh
   

    #Collect recordings from Raspberry Pis
    os.system("scp eee3097s@192.168.137.240:signal1.wav "+file)
    os.system("scp eee3097s@192.168.137.71:signal2.wav "+file)
    
    
    exit
exit