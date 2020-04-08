# importing modules
import speech_recognition
from Phygital import Phygital

# initializing microcontroller COM port
Phygital.init('COM3')

# starting the recognizer
r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    # waking up the assistant
    print('Listening: ')
    wake = r.listen(source)

try:
    print(r.recognize_google(wake))
    # speak JARVIS to start the LED control
    if r.recognize_google(wake) == 'jarvis' or r.recognize_google(wake) == 'Jarvis':
        while True:
            # initializing the led control
            with speech_recognition.Microphone() as source2:
                command = r.listen(source2)
        
            try:
                # speak the following to get the desired output
                print(r.recognize_google(command))
                if r.recognize_google(command) == 'LED 1 on':
                    Phygital.dWrite(1,1)
                    print('LED 1 is on')
                if r.recognize_google(command) == 'LED 1 off':
                    Phygital.dWrite(1,0)
                    print('LED 1 is off')
                if r.recognize_google(command) == 'LED 2 on':
                    Phygital.dWrite(2,1)
                    print('LED 2 is on')
                if r.recognize_google(command) == 'LED 2 off':
                    Phygital.dWrite(2,0)
                    print('LED 2 is off')
                if r.recognize_google(command) == 'all on':
                    Phygital.dWrite(1,1)
                    Phygital.dWrite(2,1)
                    print('All LED on')
                if r.recognize_google(command) == 'all off':
                    Phygital.dWrite(1,0)
                    Phygital.dWrite(2,0)
                    print('All LED off')
                if r.recognize_google(command) == 'stop':
                    # condition for stopping the led control
                    print('exit')
                    break
                else:
                    print('Try again')

            except speech_recognition.UnknownValueError:
                print('Unable to understand.')
except speech_recognition.UnknownValueError:
    print('Unable to Understand.')