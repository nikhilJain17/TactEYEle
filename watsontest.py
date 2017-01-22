import pyaudio
import requests
import wave
import json
# from playsound import playsound
 
def recordAndTranscribeAudio():

	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 3
	WAVE_OUTPUT_FILENAME = "file.wav"

	 
	audio = pyaudio.PyAudio()
	 
	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	print "recording..."
	frames = []
	 
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)): 
	    data = stream.read(CHUNK)
	    frames.append(data)
	print "finished recording"
	 
	 
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()
	  
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

	#playsound('file.wav') 

	USERNAME = '873ad08e-6793-4434-86c0-4f9b035b77cc'
	PASSWORD = 'tHQHT4nH5JMX'

	url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'

	headers={'Content-Type': 'audio/wav'}

	audio = open('file.wav', 'rb')

	r = requests.post(url, data=audio, headers=headers, auth=(USERNAME, PASSWORD))

	text_file = open("WatsonSTTResult.txt", "w")
	text_file.write(r.text)
	text_file.close()

