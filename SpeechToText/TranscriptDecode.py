from TestWatson import recordAndTranscribeAudio
import SendKeys
from time import sleep

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
