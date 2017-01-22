from TestWatson import recordAndTranscribeAudio
import SendKeys
from time import sleep

Set WshShell = WScript.CreateObject("WScript.Shell")


def determineAndWriteTranscript():

	while True:
		recordAndTranscribeAudio()

		f = open('WatsonSTTResult.txt', 'r')

		while True:
			text = f.readline()
			# text
			if '"transcript": ' in text:
				transcript = text[30:(len(text) - 3)]
				newTranscript = ''
				
				for c in transcript:
					if (c == ' '):
						newTranscript += "{SPACE}"
					else:
						newTranscript += c
				# insert code for calling where you want to write the code
				sleep(3)
				SendKeys.SendKeys(newTranscript)
				break
			elif f.readline() == '':
				break
                
def executeFunctions():
    
    if newTranscript == "Open Explorer":
        subprocess.call(["C:\\Windows\\explorer.exe"])
    
    elif newTranscript == "Open Chrome":
        subprocess.call(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
        
    elif newTranscript == "Open Notepad":
        subprocess.call(["C:\\WINDOWS\\system32\\notepad.exe"])
        
    elif newTranscript == "Alt Tab":
        SendKeys(%{TAB})
        
    elif newTranscript == "Control Tab":
        SendKeys(^{TAB})
        
    elif newTranscript == "Control Delete":
        SendKeys(^{DEL})
        
    elif newTranscript == "Windows Search":
        WshShell.SendKeys "({LWIN}(s))"
        
    elif newTranscript == "Chrome Search":
        SendKeys(^(l))

    elif newTranscript == "Control Find":
        SendKeys(^(f))
    
    elif newTranscript == "Chrome Tab":
        SendKeys(^(t))
        
    elif newTranscript == "Chrome Window":
        SendKeys(^(n))
    
    elif newTranscript == "Close Tab":
        SendKeys(^(w))
        
    else:
        print "DHRUV"

            
determineAndWriteTranscript()
determineAndWriteTranscript()