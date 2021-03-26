from lib.assistant import Assistant
import os

# Read settings from configuration file
VA_settings = Assistant.readConfig()
VA_triggerWord = VA_settings[0]
VA_name = VA_settings[1]
VA_gender = VA_settings[2]
# Read server from ENV variable
VA_server = os.getenv('SERVER', '')

vocalAssistant = Assistant(VA_triggerWord, VA_name, VA_gender, VA_server)
vocalAssistant.run()