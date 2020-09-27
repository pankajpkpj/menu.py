import webbrowser
import speech_recognition as sr
import pyttsx3
print("welcome to my tools\n\n")
pyttsx3.speak("welcome to my tools")

while 1 :
	print("Enter your requirements.......we r listening.....", end='')	
	pyttsx3.speak("Enter your requirements.......we r listening.....")
	#ch=input()
	r = sr.Recognizer()
	with sr.Microphone() as source :
    		print('start saying......')
    		pyttsx3.speak('start saying......')
    		audio  =r.listen(source)
    		print('we got it,plz wait.....')
    		pyttsx3.speak('we got it,plz wait.....')
	ch=r.recognize_google(audio)
	if  ('date'in ch)and ('run' in ch) or ('execute' in ch): 
		pyttsx3.speak("Running the date command")			
		webbrowser.open("http://192.168.43.229/cgi-bin/iiec.py?x=date&p=") 
		input()
	elif ('calender' in ch) and ('run' in ch)or ('execute' in ch): 
		pyttsx3.speak('Running the cal command')
		webbrowser.open("http://192.168.43.229/cgi-bin/iiec.py?x=cal&p=")
		input()  
	elif('exit' in ch):
		pyttsx3.speak('Exiting')
		break
     
	else:
		print("not uderstand")
		pyttsx3.speak('not understand')
		input()
