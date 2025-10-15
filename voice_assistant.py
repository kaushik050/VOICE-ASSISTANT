from selenium_web import info
import pyttsx3 as p #module to convert text to speech
import speech_recognition as sr #module to convert speech to text
from send_email import *
from YT_automation import *
import datetime #module to give date and time updates
import randfacts #module for random and interesting facts
import yagmail

engine = p.init() #instance of p.init class inside the pyttsx3 module; used to initiate the pyttsx3 used to convert text to speech
rate = engine.getProperty('rate') #adjust speed of the voice, default is 200
engine.setProperty('rate', 170) #to change it to slower speed
voices = engine.getProperty('voices') #to have a look at the range of voices my OS offers
engine.setProperty('voice', voices[1].id) #to listen to the 1st of 2 voices offered
# print(voices)

#for computer to say something from the user instead of typing it out in the code
def speak(text):
    engine.say(text)
    engine.runAndWait() #computer to wait until the sentence gets finished

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

r = sr.Recognizer() #create instance of the recogniser class, which creates an instance that helps us retrive info (audio) from a source (microphone)

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio) #using Google API from the speech recognition library to convert audio-my voice into text to do any task I say
    print(text)

greetings = ["hello", "hi", "hey"]  # List of acceptable greetings

if any(greeting in text for greeting in greetings): #The any function checks the list if my greeting exist
    speak("Hi Eunice, good " + wish_me() + ". My name is Asiri and I'm your Voice Assistant.")
else:
    # User didn't say the activation phrase, continue listening
    speak("Sorry, I didn't catch that but no worries")

#strftime() method takes one parameter 'format' to specify the format of the returned string
def get_date_and_time():
    today_date = datetime.datetime.now()

    # Announce date in a natural format (avoiding separate letter pronunciation)
    date_announcement = today_date.strftime("%A, %B %d, %Y")

    time_announcement = today_date.strftime("%I:%M %p")

    #add seconds
    seconds_announcement = today_date.strftime("%S")

    speak(f"Today is {date_announcement} and it's currently {time_announcement} with {seconds_announcement} seconds.")
get_date_and_time()

speak("How are you doing today?")

with sr.Microphone() as source:
    r.energy_threshold = 10000 #background property that increases spectrum of a voice. If increased, will capture even low voices
    r.adjust_for_ambient_noise(source, 1.2) #background property that cancels all the noise around you and captures your voice only
    print("listening...")
    audio = r.listen(source) #listens to what we say, captures it in a mic and saves the audio in the audio variable
    text = r.recognize_google(audio) #send the audio to the Google API engine which will convert it to a text
    print(text)

if "what" and "about" and "you" in text:
    speak("Thanks for asking, I am doing just fine!")
speak("What can I do for you at the moment?") #mandatory line

#add automation - search online sites for info I say - using Selenium WebDrive to scrape data (collecting specific information from websites.)
with sr.Microphone() as source:
    r.energy_threshold = 10000 #background property that increases spectrum of a voice. If increased, will capture even low voices
    r.adjust_for_ambient_noise(source, 1.2) #background property that cancels all the noise around you and captures your voice only
    print("listening...")
    audio = r.listen(source) #listens to what we say, captures it in a mic and saves the audio in the audio variable
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("What exactly do you need information about?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    print("Searching {} on Google".format(infor))
    speak("Searching {} on Google".format(infor))

    assist = info()
    assist.get_info(infor)

#add automation to play video on YouTube
elif "play" and "video" in text2:
    speak("Which video do you want me to play for you?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    
    print("Playing {} on YouTube".format(vid))
    speak("Playing {} on YouTube".format(vid))
 
    assist = poem()
    assist.play(vid)

#add automation to send emails
elif "send" and "email" in text2:
    speak("I am happy to send the email for you")

    with sr.Microphone() as source:
        print("clearing background noise...")
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        try:
            email_content = r.recognize_google(audio)
            print(f"Email content: {email_content}")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    print("Sending e-mail now via Gmail".format(text2))
    speak("Sending e-mail now via Gmail".format(text2))

    # Now call send_email() after capturing email content
    send_email(email_content)  # Pass the captured email content

#add automation to tell random and interesting facts
elif "fact" or "facts" in text2:
    speak("Sure Eunice," )
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " + x)

# Print exit message before exiting
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

speak("You're welcome. Anything else?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

exit_response = ["no", "not at all", "not at the moment"]  # List of acceptable exit responses

if any(response in text for response in exit_response):
    print("Alrighty, I'm going to sleep now. Bye!")
    speak("Alrighty, I'm going to sleep now. Bye!")
else:
    # User didn't say the activation phrase, continue listening
    print ("Bye!")
    speak("I didn't hear you but I'm going to sleep anyways. Bye!")

exit(0)  # Exit with code 0 (success)