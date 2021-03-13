from .logger import Logger
import requests
import speech_recognition as SpeechRecognition
# Offline recognizer
import json
from vosk import Model, KaldiRecognizer
import pyttsx3

class Assistant:
  __name = ''
  __trigger_word = ''
  __console = None
  __recognizer = None
  __offline_recognizer = None
  __offline_speaker = None
  __server = None
  __debug = False
  def __init__(self, trigger_word = 'Ehy', name = 'Howard', gender = 'female', server = '', debug = False):
    # Name configuration
    self.__name = name
    # Trigger word configuration
    self.__trigger_word = trigger_word
    # Logger
    self.__console = Logger()
    # Set debug logging level
    self.__debug = debug
    # Init online and offline recognition
    self.__recognizer = SpeechRecognition.Recognizer()
    with SpeechRecognition.Microphone(sample_rate=44100) as MicSource:
      # Calibrate Microphone for ambient noises
      self.__recognizer.adjust_for_ambient_noise(MicSource)
    self.__offline_recognizer = KaldiRecognizer(Model("./lib/model-sm-en"), 44100)
    self.__offline_speaker = pyttsx3.init()
    # Setting VocalAssistant gender
    if gender.lower() == 'female':
      voices = self.__offline_speaker.getProperty('voices')
      self.__offline_speaker.setProperty('voice', voices[1].id)
    self.__console.log(f'Vocal assistant successfully inited. Trigger him by saying "{ self.__trigger_word } { self.__name }"')
    self.say(f"Hello I'm { self.__name } your Vocal assistant, you can activate me by saying { self.__trigger_word } { self.__name }")
  
  # Listening function
  def listen(self, log_error = False):
    # Using mic
    with SpeechRecognition.Microphone(sample_rate=44100) as MicSource:
      try:
        audio = self.__recognizer.listen(MicSource, 5, 5)
        # Convert audio to text using Google
        data = self.__recognizer.recognize_google(audio)
        if self.__debug:
          self.__console.log(f'You said { data }')
        return data.lower()
      except SpeechRecognition.RequestError:
        # Convert audio to text using Vosk (Offline)
        if audio and self.__offline_recognizer.AcceptWaveform(audio.frame_data):
          res = json.loads(self.__offline_recognizer.Result())
          if self.__debug:
            self.__console.log(f'You said { res["text"] }')
          return res['text'].lower()
        else:
          if self.__debug:
            self.__console.warning('Error: Cannot understand what you said')
          return -1
        # Use Vosk
      except SpeechRecognition.UnknownValueError:
        if self.__debug:
          self.__console.warning('Error: Cannot understand what you just said')
      except SpeechRecognition.WaitTimeoutError:
        pass
      return -1

  # Vocal assistant say things
  def say(self, things_to_say = "Sorry I didn't understand what you said"):
    things_to_say = str(things_to_say)
    try:
      self.__offline_speaker.say(things_to_say)
      self.__offline_speaker.runAndWait()
    except:
      self.__console.warning(f'Error while { self.__name } trying to speak')

  def run(self):
      while True:
        # Listened if the vocal assistant is triggered
        listened = self.listen()
        if listened != -1 and f'{ self.__trigger_word } { self.__name }'.lower() in listened:
          # Send request to a server by using API or SocketIO
          if type(self.__server) == str and len(self.__server) > 0:
            response = requests.get(self.__server, params={ 'user_request': listened })
          # Default response
          else:
            response = f'You said {listened}'
          if type(response) == str:
            # Play the response
            self.say(response)
          else:
            # Cannot understand what you said
            self.say()