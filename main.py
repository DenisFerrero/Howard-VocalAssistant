from lib.assistant import Assistant
import os

VA_triggerWord = os.getenv('TRIGGER_WORD', 'Hey')
VA_name = os.getenv('ASSISTANT_NAME', 'John')
VA_server = os.getenv('SERVER', '')
VA_gender = os.getenv('ASSISTANT_GENDER', 'female')
debug = os.getenv('DEBUG', 'False')

vocalAssistant = Assistant(VA_triggerWord, VA_name, VA_gender, VA_server, debug == 'True')
vocalAssistant.run()