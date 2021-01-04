import speech_recognition as sr               #importing library for speech to text
from selenium import webdriver                #importing library for web automation
from translate import Translator              #importing library for translate text
from gtts import gTTS                         #importing library for hindi speech
import win32com.client as wincl               #importing library for text to speech
import os                                  
import time

path="c://selenium/msedgedriver.exe"          #specifying path of browser webdriver
speak = wincl.Dispatch("SAPI.SpVoice")        #storing a library function

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)          #specifying input device

def speech_to_text():                        #function to covert speech into a text
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)    #storing surrounding noise
        print_speak("Waiting for your response")
        audio = r.listen(source, timeout=5)               #storing voice
        print_speak("Thank you for your response")
    try:                                                    
        voice_text=r.recognize_google(audio)              #storing and coverting voice into text
        return voice_text.lower()
    except:                                               
        print_speak("Unable to understand, please speak again")
        voice_text=speech_to_text()         #recalling same function again in case got any error so that programm does not get stop
        return voice_text.lower()
    
def print_speak(strings):                   #function to print and convert text into speech simultaneously
    print(strings)
    speak.Speak(strings)                    #for speaking statements passed in it
print_speak("Hii, this is your personal mini assistant, let's get started")
print_speak("To give me command use 'music' for playing music or 'translate' for translating english to hindi")
response=speech_to_text()                   #calling function to convert speech into text
print_speak("You choose for " + response)
if "music" in response:                     #checking if "music" keyword is present in my speech and if it is then play a song
    print_speak("Name a song")
    song_name=speech_to_text()              #calling function to get song name from speech
    print_speak("Playing " + song_name)
    
    driver=webdriver.Edge(path)
    driver.get("https://www.youtube.com")                                   #opening youtube in browser
    driver.find_element_by_name('search_query').send_keys(song_name)        #searching song given by user
    driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()   
    time.sleep(1)                                                           #waiting for page to load complete
    #below code will find very first video and play it
    driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img').click()
    time.sleep(8)                                                           #waiting for ad if any
    try:                                                                    #if any youtube ad start plying this will close it otherwise pass
        driver.find_element_by_class_name("ytp-ad-skip-button-icon").click()
    except:
        pass
    
elif "translate" in response:               #checking if "translate" keyword is present in speech and if it is then translate 
    print_speak("Speak something that you want to translate after this")
    trans_text=speech_to_text()             #calling function to convert speech into text
    print_speak("translating " + trans_text + " in hindi")

    translator=Translator(to_lang="Hindi")         #specifying translating language and function in a variable
    translation=translator.translate(trans_text)   #translating given speech in hindi
    print(translation)                             #printing translated text

    myobj = gTTS(text=translation, lang='hi', slow=False)  #coverting translated text into speech
    myobj.save("welcome.mp3")                      #saving speech into a mp3 file
    os.system("welcome.mp3")                       #playing our translated mp3 file
    time.sleep(6)                                  #waiting for playing file to end
    os.system('TASKKILL /F /IM vlc.exe')           #ending task after playing playing translated file
