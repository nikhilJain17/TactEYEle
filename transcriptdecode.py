from watsontest import recordAndTranscribeAudio
from time import sleep
from subprocess import *
import pyautogui
import webbrowser
import os
from threading import Thread
import signal
# import headtracker

global trusttheprocess 
 
def determineAndWriteTranscript():

	while True:
		recordAndTranscribeAudio()

		f = open('WatsonSTTResult.txt', 'r')

		while True:
			text = f.readline()
			# text
			if '"transcript": ' in text:
				transcript = text[30:(len(text) - 3)]
				transcriptSansTranscribe = ''
				if (determineIfWrite(transcript)):	
					transcriptSansTranscribe = transcript[11:(len(transcript))]
					pyautogui.typewrite(transcriptSansTranscribe)
					break
				else:
					executeFunctions(transcript)
			elif f.readline() == '':
				break
                
def determineIfWrite(newTranscript):
	if "transcribe" in newTranscript:
		return True
	else:
		return False

def determineIfMouseActivate(bo=False):
	return bo

def executeFunctions(newTranscript):
    
    print  " _____________" + newTranscript + " _____________"



    if newTranscript == "open chrome":
        print 'chrome caller'
        webbrowser.open('http://www.google.com', new=2)
        # Popen(['google-chrome'])
        
    # elif newTranscript == "open word":
    #     subprocess.call(["C:\\Program Files\\Microsoft Office\\Office14\\WINWORD.exe"])
    elif newTranscript == "command tab":
        pyautogui.hotkey('command','tab')
        
    elif newTranscript == "control tab":
        pyautogui.hotkey('ctrl','tab')
        
    elif newTranscript == "command delete":
        pyautogui.hotkey('command','del')
        
    elif newTranscript == "select all":
    	pyautogui.hotkey('command', 'a')

    elif newTranscript == "global search":
        pyautogui.hotkey('command',' ')
        
    #must open chrome first to use these
    elif newTranscript == "chrome search":
        pyautogui.hotkey('command','l')

    elif newTranscript == "command find":
        pyautogui.hotkey('command','f')
    
    elif newTranscript == "new tab":
        pyautogui.hotkey('command','t')
    
    elif newTranscript == "close tab":
        pyautogui.hotkey('command','w')

    elif newTranscript == "page down":
    	pyautogui.press('pgdn')
     
    elif newTranscript == "page up":
    	pyautogui.press('pgup')
    
    elif newTranscript == "enter":
    	pyautogui.press('enter')

    elif newTranscript == "tab":
    	pyautogui.press('tab')  

    elif newTranscript == 'tactile enable' or "enable" in newTranscript:
    	# determineIfMouseActivate(True)
        # headtracker.main() 
        # start in new shell
        c = 'python headtracker.py'
        trusttheprocess = Popen(c, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)



    elif newTranscript == 'tactile disable' or 'disable' in newTranscript:
        # stop the headtracker
        # headtracker.kill() 
        print 'kill bill'
        global trusttheprocess
        trusttheprocess.send_signal(signal.SIGINT)
    
    else:
        print "Error: Try Again"


def tactileEnable():
    c = 'python headtracker.py'
    Popen(c, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True) 



determineAndWriteTranscript()