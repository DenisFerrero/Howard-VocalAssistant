from .logger import Logger
import speech_recognition as SpeechRecognition

class Assistant:
  __name = ''
  __trigger_word = ''
  __plugins = []
  __console = None
  __recognizer = None
  def __init__(self, name = 'Howard', trigger_word = 'Ehy', plugin = [], console = Logger(True)):
    # Name configuration
    if bool(name.strip()):
      self.__name = name
    # Trigger word configuration
    if bool(trigger_word.strip()):
      self.__trigger_word = trigger_word
    # Save plugins
    for single_plugin in plugin:
      self.__plugins.append(single_plugin)
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
        self.__console.info(f'Audio listened: {data}')
      except SpeechRecognition.RequestError:
        self.__console.warning('Vosk still needed to be configured')
        # Use Vosk
      except SpeechRecognition.UnkhownValueError:
        self.__console.warning('Error: Cannot understand what you just said')