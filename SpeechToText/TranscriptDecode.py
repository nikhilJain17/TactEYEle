from TestWatson import recordAndTranscribeAudio
import SendKeys
from time import sleep
import subprocess
import pyautogui


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
					SendKeys.SendKeys(transcriptSansTranscribe, with_spaces = True)
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

def determineIfMouseActivate():
	recordAndTranscribeAudio()

		f = open('WatsonSTTResult.txt', 'r')

		while True:
			text = f.readline()
			# text
			if '"transcript": ' in text:
				transcript = text[30:(len(text) - 3)]
				if "tactile enable" in transcript:
					return True
				return False

def executeFunctions(newTranscript):
    
    if newTranscript == "open chrome":
        subprocess.call(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
        
    # elif newTranscript == "open word":
    #     subprocess.call(["C:\\Program Files\\Microsoft Office\\Office14\\WINWORD.exe"])
        
    elif newTranscript == "alt tab":
        pyautogui.hotkey('alt','tab')
        
    elif newTranscript == "control tab":
        pyautogui.hotkey('ctrl','tab')
        
    elif newTranscript == "control delete":
        pyautogui.hotkey('ctrl','delete')
        
    elif newTranscript == "select all":
    	pyautogui.hotkey('ctrl', 'a')

    elif newTranscript == "windows search":
        pyautogui.hotkey('win','s')
        
    #must open chrome first to use these
    elif newTranscript == "chrome search":
        pyautogui.hotkey('ctrl','l')

    elif newTranscript == "control find":
        pyautogui.hotkey('ctrl','f')
    
    elif newTranscript == "chrome tab":
        pyautogui.hotkey('ctrl','t')
    
    elif newTranscript == "close tab":
        pyautogui.hotkey('ctrl','w')

    elif newTranscript == "page down":
    	pyautogui.press('pgdn')
    
    elif newTranscript == "page up":
    	pyautogui.press('pgup')
    
    elif newTranscript == "enter":
    	pyautogui.press('enter')

    elif newTranscript == "tab":
    	pyautogui.press('tab')
    
    else:
        print "Error: Try Again"
