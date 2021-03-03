from .logger import Logger
import requests
import speech_recognition as SpeechRecognition
import os
from gtts import gTTS
import playsound

class Assistant:
  __name = ''
  __trigger_word = ''
  __console = None
  __recognizer = None
  def __init__(self, trigger_word = 'Ehy', name = 'Howard', console = Logger(True)):
    # Name configuration
    if bool(name.strip()):
      self.__name = name
    # Trigger word configuration
    if bool(trigger_word.strip()):
      self.__trigger_word = trigger_word
    # Save logger
    if console:
      self.__console = console
    self.__recognizer = SpeechRecognition.Recognizer()
    self.__console.log(f'Vocal assistant successfully inited. Trigger him by saying "{ self.__trigger_word } { self.__name }"')
  
  # Listening function
  def listen(self):
    with SpeechRecognition.Microphone() as MicSource:
      try:
        audio = self.__recognizer.listen(MicSource)
        data = self.__recognizer.recognize_google(audio)
        return data
      except SpeechRecognition.RequestError:
        self.__console.warning('Vosk still needed to be configured')
        # Use Vosk
      except SpeechRecognition.UnknownValueError:
        self.__console.warning('Error: Cannot understand what you just said')
      return -1

  def say(self, things_to_say = "Sorry I didn't understand what you said"):
    things_to_say = str(things_to_say)
    tts = gTTS(text=things_to_say, lang='en')
    tts.save('audio.mp3') 
    playsound.playsound('audio.mp3')
    os.remove('audio.mp3')

  def run(self):
      while True:
        listened = self.listen()
        response = listened
        # response = requests.get('https://example.com', params={ 'user_request': listened })
        # Rather than listened make a REST call to the server that'll parse the result
        if type(response) == str:
          self.say(response)
        else:
          self.say()